import chokidar from 'chokidar';
import path from 'path';
import fs from 'fs';
import { dbRun, dbGet, dbAll } from '../db.js';

// Agent names to monitor
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

// Paths to monitor
let WATCH_PATHS = [];
let watcher = null;
let isInitialized = false;

/**
 * Initialize the file watcher
 * @param {string} baseDir - The Cowork Client-Management-System directory
 */
export function initializeWatcher(baseDir) {
  if (isInitialized) {
    console.log('File watcher already initialized');
    return;
  }

  // Paths to monitor for agent output files
  WATCH_PATHS = [
    path.join(baseDir, 'PROJECTS', 'Active'),
    path.join(baseDir, 'OUTPUT', 'End-of-Day Reports'),
    baseDir // Also watch root for [agent-name]-RUN-*.md files
  ];

  console.log('Initializing file watcher for paths:', WATCH_PATHS);

  // Create watcher with ignores
  watcher = chokidar.watch(WATCH_PATHS, {
    persistent: true,
    ignoreInitial: true,
    ignored: [/(^|[\/\\])\.|\.DS_Store/, /node_modules/, /.git/],
    awaitWriteFinish: {
      stabilityThreshold: 2000,
      pollInterval: 100
    }
  });

  // File added or modified
  watcher.on('add', (filePath) => {
    console.log(`[FileWatch] File added: ${filePath}`);
    processFileChange(filePath, 'add');
  });

  watcher.on('change', (filePath) => {
    console.log(`[FileWatch] File modified: ${filePath}`);
    processFileChange(filePath, 'change');
  });

  watcher.on('error', (error) => {
    console.error('[FileWatch] Error:', error);
  });

  watcher.on('ready', () => {
    console.log('[FileWatch] Watcher ready and monitoring');
    isInitialized = true;
  });
}

/**
 * Process a file change and record agent run
 * @param {string} filePath - Path to the modified file
 * @param {string} changeType - 'add' or 'change'
 */
async function processFileChange(filePath, changeType) {
  try {
    // Only process .md files
    if (!filePath.endsWith('.md')) {
      return;
    }

    // Detect which agent caused this change
    const detectedAgent = detectAgent(filePath);
    if (!detectedAgent) {
      console.log(`[FileWatch] Could not detect agent for file: ${filePath}`);
      return;
    }

    // Get file stats
    const stats = fs.statSync(filePath);
    const fileSize = stats.size;
    const mtime = new Date(stats.mtime);

    // Check for errors in file content
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const hasErrors = checkForErrors(fileContent);
    const success = !hasErrors && fileSize > 50; // File should have content

    // Record in database
    const result = await recordAgentRun({
      agent_name: detectedAgent,
      timestamp: mtime,
      status: success ? 'completed' : (hasErrors ? 'error' : 'completed'),
      output_file: filePath,
      file_size: fileSize,
      success: success ? 1 : 0,
      details: `File ${changeType}d: ${path.basename(filePath)}`,
      error_message: hasErrors ? 'Errors detected in output' : null
    });

    console.log(`[FileWatch] Recorded run for ${detectedAgent}:`, result);

  } catch (error) {
    console.error('[FileWatch] Error processing file change:', error);
  }
}

/**
 * Detect which agent created/modified a file
 * @param {string} filePath - Path to the file
 * @returns {string|null} - Agent name or null
 */
function detectAgent(filePath) {
  const fileName = path.basename(filePath);
  const dirPath = path.dirname(filePath);

  // Strategy 1: Check for [agent-name]-RUN-[timestamp].md pattern
  for (const agent of AGENT_NAMES) {
    const runPattern = new RegExp(`${agent}-RUN-\\d+`);
    if (runPattern.test(fileName)) {
      return agent;
    }
  }

  // Strategy 2: Look for agent name in file path
  for (const agent of AGENT_NAMES) {
    if (filePath.toLowerCase().includes(agent)) {
      return agent;
    }
  }

  // Strategy 3: Check file content for agent signature
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    for (const agent of AGENT_NAMES) {
      // Look for headings with agent name or tags
      const patterns = [
        new RegExp(`# ${agent}`, 'i'),
        new RegExp(`Agent: ${agent}`, 'i'),
        new RegExp(`\\[${agent}\\]`, 'i')
      ];
      if (patterns.some(p => p.test(content))) {
        return agent;
      }
    }
  } catch (e) {
    // Ignore read errors
  }

  return null;
}

/**
 * Check file content for error indicators
 * @param {string} content - File content
 * @returns {boolean} - True if errors detected
 */
function checkForErrors(content) {
  const errorPatterns = [
    /ERROR:/i,
    /FAILED:/i,
    /failed/i,
    /error occurred/i,
    /exception/i,
    /could not/i,
    /unable to/i
  ];

  // Also check if file has actual content (not just headers)
  const hasContent = content.trim().length > 100;

  return errorPatterns.some(pattern => pattern.test(content)) || !hasContent;
}

/**
 * Record an agent run in the database
 * @param {object} runData - Run data
 * @returns {Promise} - Result of insert
 */
export async function recordAgentRun(runData) {
  try {
    // Check if we already have a recent run for this agent
    const recentRun = await dbGet(
      `SELECT * FROM agent_runs
       WHERE agent_name = ? AND datetime(timestamp) > datetime('now', '-5 minutes')
       ORDER BY timestamp DESC LIMIT 1`,
      [runData.agent_name]
    );

    if (recentRun) {
      console.log(`[DB] Recent run already exists for ${runData.agent_name}, updating...`);
      // Update existing run
      return await dbRun(
        `UPDATE agent_runs
         SET status = ?, output_file = ?, file_size = ?, success = ?,
             details = ?, error_message = ?, updated_at = CURRENT_TIMESTAMP
         WHERE id = ?`,
        [
          runData.status,
          runData.output_file,
          runData.file_size,
          runData.success,
          runData.details,
          runData.error_message,
          recentRun.id
        ]
      );
    }

    // Insert new run
    return await dbRun(
      `INSERT INTO agent_runs
       (agent_name, timestamp, status, output_file, file_size, success, details, error_message)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
      [
        runData.agent_name,
        runData.timestamp || new Date(),
        runData.status,
        runData.output_file,
        runData.file_size,
        runData.success,
        runData.details,
        runData.error_message
      ]
    );
  } catch (error) {
    console.error('[DB] Error recording agent run:', error);
    throw error;
  }
}

/**
 * Close the watcher
 */
export async function closeWatcher() {
  if (watcher) {
    await watcher.close();
    console.log('[FileWatch] Watcher closed');
    isInitialized = false;
  }
}

/**
 * Get status of the watcher
 */
export function getWatcherStatus() {
  return {
    initialized: isInitialized,
    watching: WATCH_PATHS,
    agentsMonitored: AGENT_NAMES.length
  };
}
