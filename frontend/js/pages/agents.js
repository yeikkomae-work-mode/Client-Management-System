/**
 * Agents Page - Initializes and manages the Agents Office view
 */

import AgentsOffice from '../components/agents-office.js';

let agentsOffice = null;

/**
 * Initialize the agents page
 */
export async function initAgentsPage() {
  try {
    console.log('[Page] Initializing Agents page...');

    // Create and initialize the AgentsOffice component
    agentsOffice = new AgentsOffice('agentsContainer', getApiBaseUrl());
    await agentsOffice.init();

    // Setup page controls
    setupPageControls();

    console.log('[Page] Agents page ready');
  } catch (error) {
    console.error('[Page] Error initializing agents page:', error);
    showErrorMessage('Failed to load agents page. Make sure the backend server is running.');
  }
}

/**
 * Setup page control buttons and features
 */
function setupPageControls() {
  const refreshBtn = document.getElementById('agentsRefreshBtn');
  if (refreshBtn) {
    refreshBtn.addEventListener('click', async () => {
      refreshBtn.disabled = true;
      refreshBtn.textContent = 'Refreshing...';
      try {
        await agentsOffice.refresh();
        refreshBtn.textContent = 'Refresh';
      } finally {
        refreshBtn.disabled = false;
      }
    });
  }

  // Auto-refresh toggle (if available)
  const autoRefreshToggle = document.getElementById('autoRefreshToggle');
  if (autoRefreshToggle) {
    autoRefreshToggle.addEventListener('change', (e) => {
      agentsOffice.autoRefreshEnabled = e.target.checked;
    });
  }
}

/**
 * Show error message
 */
function showErrorMessage(message) {
  const container = document.getElementById('agentsContainer');
  if (container) {
    container.innerHTML = `
      <div style="padding: 40px; text-align: center;">
        <div style="font-size: 48px; margin-bottom: 16px;">⚠️</div>
        <div style="font-size: 18px; font-weight: 600; color: var(--text-0); margin-bottom: 8px;">
          Connection Error
        </div>
        <div style="color: var(--text-2); margin-bottom: 16px;">
          ${message}
        </div>
        <div style="font-size: 12px; color: var(--text-2);">
          <p>Backend server should be running at: <code>${getApiBaseUrl()}</code></p>
          <p style="margin-top: 8px;">
            To start the server:
          </p>
          <pre style="background: rgba(0,0,0,0.1); padding: 12px; border-radius: 6px; text-align: left; overflow-x: auto;">
cd backend
npm install
npm start
          </pre>
        </div>
      </div>
    `;
  }
}

/**
 * Get API base URL from environment or default
 */
function getApiBaseUrl() {
  // Check if running on localhost (development)
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return 'http://localhost:3001';
  }

  // Check for environment variable
  if (window.__API_BASE_URL__) {
    return window.__API_BASE_URL__;
  }

  // Default
  return 'http://localhost:3001';
}

/**
 * Export API for external use
 */
export function getAgentsOffice() {
  return agentsOffice;
}

// Auto-initialize if this is the agents page
if (document.currentScript) {
  const pageType = document.currentScript.dataset.page;
  if (pageType === 'agents') {
    document.addEventListener('DOMContentLoaded', () => {
      initAgentsPage();
    });
  }
}
