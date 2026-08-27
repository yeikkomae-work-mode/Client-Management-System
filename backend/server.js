import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import { initializeWatcher, getWatcherStatus, closeWatcher } from './services/file-watcher.js';
import agentsTrackingRouter from './routes/agents-tracking.js';
import campaignsRouter from './routes/campaigns.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const PORT = process.env.PORT || 3001;
// Portable: honour COWORK_DIR (set by scripts/setup-cloud-env.sh), else fall
// back to the repo root, which is always the parent of backend/.
const COWORK_BASE_DIR = process.env.COWORK_DIR || path.resolve(__dirname, '..');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '..', '.claude-dashboard')));

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date(),
    uptime: process.uptime(),
    watcher: getWatcherStatus()
  });
});

// API routes
app.use('/api/agents/track', agentsTrackingRouter);
app.use('/api/campaigns', campaignsRouter);

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    name: 'Agent Tracking System API',
    version: '1.0.0',
    endpoints: {
      health: 'GET /health',
      agentStatus: 'GET /api/agents/track/status',
      agentHistory: 'GET /api/agents/track/:name/history',
      agentOutput: 'GET /api/agents/track/:name/latest-output',
      activityFeed: 'GET /api/agents/track/activity-feed/recent',
      stats: 'GET /api/agents/track/stats/aggregate',
      campaignsData: 'GET /api/campaigns/data',
      campaignsSync: 'POST /api/campaigns/sync'
    }
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('[Server] Error:', err);
  res.status(err.status || 500).json({
    success: false,
    error: err.message || 'Internal server error'
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found'
  });
});

// Start server
async function startServer() {
  try {
    // Initialize the file watcher
    console.log('[Server] Initializing file watcher...');
    initializeWatcher(COWORK_BASE_DIR);

    // Start listening
    app.listen(PORT, () => {
      console.log(`[Server] Agent Tracking System running on http://localhost:${PORT}`);
      console.log(`[Server] Cowork Base Dir: ${COWORK_BASE_DIR}`);
      console.log('[Server] Use /health endpoint to check status');
    });

  } catch (error) {
    console.error('[Server] Failed to start:', error);
    process.exit(1);
  }
}

// Graceful shutdown
process.on('SIGINT', async () => {
  console.log('[Server] Shutting down gracefully...');
  await closeWatcher();
  process.exit(0);
});

process.on('SIGTERM', async () => {
  console.log('[Server] Terminating gracefully...');
  await closeWatcher();
  process.exit(0);
});

// Start the server
startServer();
