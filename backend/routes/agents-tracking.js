import express from 'express';
import { dbAll, dbGet } from '../db.js';
import fs from 'fs';

const router = express.Router();

// Agent names for consistency
const AGENT_NAMES = [
  'project-manager',
  'inbox-triage',
  'copywriter',
  'reply-handler',
  'lead-prospector',
  'market-scout',
  'meeting-summarizer',
  'onboarding-guide',
  'billing-auditor',
  'file-organizer'
];

/**
 * GET /api/agents/track/status
 * Get current status of all agents
 */
router.get('/status', async (req, res) => {
  try {
    const agents = [];

    for (const agentName of AGENT_NAMES) {
      const metadata = await dbGet(
        'SELECT * FROM agent_metadata WHERE agent_name = ?',
        [agentName]
      );

      const latestRun = await dbGet(
        `SELECT * FROM agent_runs
         WHERE agent_name = ?
         ORDER BY timestamp DESC LIMIT 1`,
        [agentName]
      );

      const status = calculateAgentStatus(latestRun);
      const successRate = await calculateSuccessRate(agentName);

      agents.push({
        name: agentName,
        category: metadata?.category || 'unknown',
        icon: metadata?.icon || '❓',
        description: metadata?.description || '',
        status: status,
        lastRun: latestRun?.timestamp || null,
        successRate: successRate,
        totalRuns: latestRun ? await countTotalRuns(agentName) : 0,
        outputFile: latestRun?.output_file || null,
        fileSize: latestRun?.file_size || null
      });
    }

    res.json({
      success: true,
      timestamp: new Date(),
      agents: agents,
      summary: {
        totalAgents: agents.length,
        activeNow: agents.filter(a => a.status === 'running').length,
        completedToday: agents.filter(a => isToday(a.lastRun)).length,
        averageSuccessRate: (agents.reduce((sum, a) => sum + a.successRate, 0) / agents.length).toFixed(1)
      }
    });
  } catch (error) {
    console.error('[API] Error fetching agent status:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

/**
 * GET /api/agents/track/:name/history
 * Get run history for a specific agent
 */
router.get('/:name/history', async (req, res) => {
  try {
    const { name } = req.params;
    const limit = parseInt(req.query.limit) || 50;
    const offset = parseInt(req.query.offset) || 0;

    const runs = await dbAll(
      `SELECT * FROM agent_runs
       WHERE agent_name = ?
       ORDER BY timestamp DESC
       LIMIT ? OFFSET ?`,
      [name, limit, offset]
    );

    const totalCount = await dbGet(
      'SELECT COUNT(*) as count FROM agent_runs WHERE agent_name = ?',
      [name]
    );

    res.json({
      success: true,
      agent: name,
      totalRuns: totalCount?.count || 0,
      limit: limit,
      offset: offset,
      runs: runs || []
    });
  } catch (error) {
    console.error('[API] Error fetching agent history:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

/**
 * GET /api/agents/track/:name/latest-output
 * Get latest output content for a specific agent
 */
router.get('/:name/latest-output', async (req, res) => {
  try {
    const { name } = req.params;

    const latestRun = await dbGet(
      `SELECT * FROM agent_runs
       WHERE agent_name = ?
       ORDER BY timestamp DESC LIMIT 1`,
      [name]
    );

    if (!latestRun) {
      return res.status(404).json({
        success: false,
        error: 'No runs found for this agent'
      });
    }

    // Try to read the output file
    let content = null;
    let error = null;

    if (latestRun.output_file && fs.existsSync(latestRun.output_file)) {
      try {
        content = fs.readFileSync(latestRun.output_file, 'utf-8');
        // Limit content to 50KB for API response
        if (content.length > 50000) {
          content = content.substring(0, 50000) + '\n\n[Output truncated - file too large]';
        }
      } catch (e) {
        error = e.message;
      }
    }

    res.json({
      success: true,
      agent: name,
      run: {
        id: latestRun.id,
        timestamp: latestRun.timestamp,
        status: latestRun.status,
        success: latestRun.success,
        outputFile: latestRun.output_file,
        fileSize: latestRun.file_size,
        details: latestRun.details
      },
      content: content,
      readError: error
    });
  } catch (error) {
    console.error('[API] Error fetching latest output:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

/**
 * GET /api/agents/track/activity-feed
 * Get recent activity across all agents
 */
router.get('/activity-feed/recent', async (req, res) => {
  try {
    const limit = parseInt(req.query.limit) || 20;

    const activities = await dbAll(
      `SELECT agent_runs.*, agent_metadata.icon, agent_metadata.category
       FROM agent_runs
       LEFT JOIN agent_metadata ON agent_runs.agent_name = agent_metadata.agent_name
       ORDER BY agent_runs.timestamp DESC
       LIMIT ?`,
      [limit]
    );

    res.json({
      success: true,
      timestamp: new Date(),
      activities: activities || []
    });
  } catch (error) {
    console.error('[API] Error fetching activity feed:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

/**
 * GET /api/agents/track/stats
 * Get aggregate statistics
 */
router.get('/stats/aggregate', async (req, res) => {
  try {
    const stats = await dbGet(
      `SELECT
        COUNT(DISTINCT agent_name) as total_agents,
        COUNT(*) as total_runs,
        SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful_runs,
        SUM(file_size) as total_data_processed,
        AVG(file_size) as avg_file_size
       FROM agent_runs`
    );

    const today = await dbAll(
      `SELECT agent_name, COUNT(*) as runs_today
       FROM agent_runs
       WHERE DATE(timestamp) = DATE('now')
       GROUP BY agent_name`
    );

    const hourly = await dbAll(
      `SELECT agent_name, COUNT(*) as count, DATETIME(timestamp, 'start of hour') as hour
       FROM agent_runs
       WHERE datetime(timestamp) > datetime('now', '-24 hours')
       GROUP BY agent_name, hour
       ORDER BY hour DESC`
    );

    res.json({
      success: true,
      timestamp: new Date(),
      aggregate: stats || {},
      runsToday: today || [],
      last24Hours: hourly || []
    });
  } catch (error) {
    console.error('[API] Error fetching stats:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

// ============ Helper functions ============

/**
 * Calculate agent status based on latest run
 */
function calculateAgentStatus(latestRun) {
  if (!latestRun) {
    return 'idle'; // Never run
  }

  const now = new Date();
  const lastRunTime = new Date(latestRun.timestamp);
  const diffMinutes = (now - lastRunTime) / (1000 * 60);

  if (diffMinutes < 5) {
    return 'running';
  } else if (diffMinutes < 60) {
    return 'completed';
  } else {
    return 'idle';
  }
}

/**
 * Calculate success rate for an agent
 */
async function calculateSuccessRate(agentName) {
  try {
    const result = await dbGet(
      `SELECT
        COUNT(*) as total,
        SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful
       FROM agent_runs
       WHERE agent_name = ?`,
      [agentName]
    );

    if (!result || result.total === 0) {
      return 100; // Default to 100% if no runs
    }

    return Math.round((result.successful / result.total) * 100);
  } catch (error) {
    console.error('Error calculating success rate:', error);
    return 0;
  }
}

/**
 * Count total runs for an agent
 */
async function countTotalRuns(agentName) {
  try {
    const result = await dbGet(
      'SELECT COUNT(*) as count FROM agent_runs WHERE agent_name = ?',
      [agentName]
    );
    return result?.count || 0;
  } catch (error) {
    console.error('Error counting runs:', error);
    return 0;
  }
}

/**
 * Check if timestamp is from today
 */
function isToday(timestamp) {
  if (!timestamp) return false;
  const date = new Date(timestamp);
  const today = new Date();
  return date.toDateString() === today.toDateString();
}

export default router;
