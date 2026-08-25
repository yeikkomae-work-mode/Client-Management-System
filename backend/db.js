import sqlite3 from 'sqlite3';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Database path - store in backend directory
const DB_PATH = path.join(__dirname, 'agent-tracking.db');

// Create database connection
const db = new sqlite3.Database(DB_PATH, (err) => {
  if (err) {
    console.error('Error opening database:', err);
  } else {
    console.log('Connected to SQLite database at:', DB_PATH);
    initializeTables();
  }
});

// Enable foreign keys
db.run('PRAGMA foreign_keys = ON');

/**
 * Initialize database tables
 */
function initializeTables() {
  // Agent Runs table - tracks each agent execution
  db.run(`
    CREATE TABLE IF NOT EXISTS agent_runs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      agent_name TEXT NOT NULL,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
      status TEXT DEFAULT 'completed',
      output_file TEXT,
      duration_ms INTEGER,
      success INTEGER DEFAULT 1,
      file_size INTEGER,
      details TEXT,
      error_message TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      UNIQUE(agent_name, timestamp)
    )
  `, (err) => {
    if (err) {
      console.error('Error creating agent_runs table:', err);
    } else {
      console.log('agent_runs table initialized');
    }
  });

  // Agent Metadata table - tracks agent info
  db.run(`
    CREATE TABLE IF NOT EXISTS agent_metadata (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      agent_name TEXT UNIQUE NOT NULL,
      category TEXT,
      description TEXT,
      icon TEXT,
      last_seen_timestamp DATETIME,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `, (err) => {
    if (err) {
      console.error('Error creating agent_metadata table:', err);
    } else {
      console.log('agent_metadata table initialized');
      // Insert default agent metadata
      insertDefaultAgentMetadata();
    }
  });

  // File Monitoring Cache - tracks files we've already seen
  db.run(`
    CREATE TABLE IF NOT EXISTS file_monitoring_cache (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      file_path TEXT UNIQUE NOT NULL,
      last_modified DATETIME,
      file_size INTEGER,
      detected_agent TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `, (err) => {
    if (err) {
      console.error('Error creating file_monitoring_cache table:', err);
    } else {
      console.log('file_monitoring_cache table initialized');
    }
  });
}

/**
 * Insert default agent metadata
 */
function insertDefaultAgentMetadata() {
  const agents = [
    // Front-office (client-facing)
    { name: 'lead-prospector', category: 'front-office', icon: '🎯', description: 'Apollo searches, list building' },
    { name: 'copywriter', category: 'front-office', icon: '🎯', description: 'Email sequences, campaign copy' },
    { name: 'reply-handler', category: 'front-office', icon: '🎯', description: 'Campaign replies, objections' },
    { name: 'market-scout', category: 'front-office', icon: '🎯', description: 'Competitor research, trends' },
    // Back-office (operations)
    { name: 'inbox-triage', category: 'back-office', icon: '⚙️', description: 'Email triaging, drafting' },
    { name: 'project-manager', category: 'back-office', icon: '⚙️', description: 'Task tracking, rollups' },
    { name: 'billing-auditor', category: 'back-office', icon: '⚙️', description: 'Time tracking, invoices' },
    { name: 'file-organizer', category: 'back-office', icon: '⚙️', description: 'Folder structure, hygiene' },
    { name: 'onboarding-guide', category: 'back-office', icon: '⚙️', description: 'Client setup, checklists' },
    { name: 'meeting-summarizer', category: 'back-office', icon: '⚙️', description: 'Call minutes, action items' },
  ];

  agents.forEach((agent) => {
    db.run(
      `INSERT OR IGNORE INTO agent_metadata (agent_name, category, icon, description)
       VALUES (?, ?, ?, ?)`,
      [agent.name, agent.category, agent.icon, agent.description],
      (err) => {
        if (err) {
          console.error(`Error inserting agent metadata for ${agent.name}:`, err);
        }
      }
    );
  });
}

/**
 * Utility: Run a query and return promise
 */
export function dbRun(sql, params = []) {
  return new Promise((resolve, reject) => {
    db.run(sql, params, function (err) {
      if (err) {
        reject(err);
      } else {
        resolve({ id: this.lastID, changes: this.changes });
      }
    });
  });
}

/**
 * Utility: Get a single row
 */
export function dbGet(sql, params = []) {
  return new Promise((resolve, reject) => {
    db.get(sql, params, (err, row) => {
      if (err) {
        reject(err);
      } else {
        resolve(row);
      }
    });
  });
}

/**
 * Utility: Get all rows
 */
export function dbAll(sql, params = []) {
  return new Promise((resolve, reject) => {
    db.all(sql, params, (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows || []);
      }
    });
  });
}

export default db;
