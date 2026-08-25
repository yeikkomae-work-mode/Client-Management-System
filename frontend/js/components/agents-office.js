/**
 * Agents Office Visualization Component
 * Displays 10 agents at desks with status, activity, and performance metrics
 */

export class AgentsOffice {
  constructor(containerId, apiBaseUrl = 'http://localhost:3001') {
    this.container = document.getElementById(containerId);
    this.apiBaseUrl = apiBaseUrl;
    this.agents = [];
    this.activities = [];
    this.modal = null;
    this.refreshInterval = null;
    this.autoRefreshEnabled = true;
  }

  /**
   * Initialize and render the office
   */
  async init() {
    try {
      console.log('[AgentsOffice] Initializing...');
      await this.loadAgentStatus();
      this.render();
      this.attachEventListeners();
      this.startAutoRefresh();
      console.log('[AgentsOffice] Ready');
    } catch (error) {
      console.error('[AgentsOffice] Init error:', error);
      this.showError('Failed to initialize agents office');
    }
  }

  /**
   * Load agent status from API
   */
  async loadAgentStatus() {
    try {
      const response = await fetch(`${this.apiBaseUrl}/api/agents/track/status`);
      const data = await response.json();

      if (data.success) {
        this.agents = data.agents;
        console.log(`[AgentsOffice] Loaded ${this.agents.length} agents`);
      }
    } catch (error) {
      console.error('[AgentsOffice] Error loading agent status:', error);
      throw error;
    }
  }

  /**
   * Load recent activity
   */
  async loadActivityFeed(limit = 10) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/api/agents/track/activity-feed/recent?limit=${limit}`);
      const data = await response.json();

      if (data.success) {
        this.activities = data.activities;
        console.log(`[AgentsOffice] Loaded ${this.activities.length} activities`);
      }
    } catch (error) {
      console.error('[AgentsOffice] Error loading activity feed:', error);
    }
  }

  /**
   * Render the entire office view
   */
  render() {
    if (!this.container) {
      console.error('[AgentsOffice] Container not found');
      return;
    }

    this.container.innerHTML = `
      <div class="agents-office">
        ${this.renderHeader()}
        ${this.renderStats()}
        ${this.renderGrid()}
        ${this.renderActivityFeed()}
        ${this.renderModal()}
      </div>
    `;
  }

  /**
   * Render header with title and info
   */
  renderHeader() {
    const activeCount = this.agents.filter(a => a.status === 'running').length;

    return `
      <div class="office-header">
        <div class="office-title">Agents Office 🏢</div>
        <div class="office-subtitle">
          ${this.agents.length} agents deployed
          <div class="status-badge">
            ${activeCount} active now
          </div>
        </div>
      </div>
    `;
  }

  /**
   * Render quick stats row
   */
  renderStats() {
    const summary = {
      totalAgents: this.agents.length,
      activeNow: this.agents.filter(a => a.status === 'running').length,
      completedToday: this.agents.filter(a => this.isToday(a.lastRun)).length,
      avgSuccess: Math.round(
        this.agents.reduce((sum, a) => sum + a.successRate, 0) / Math.max(this.agents.length, 1)
      )
    };

    return `
      <div class="office-stats">
        <div class="stat-card">
          <div class="stat-value">${summary.activeNow}</div>
          <div class="stat-label">Active Now</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">${summary.completedToday}</div>
          <div class="stat-label">Completed Today</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">${summary.avgSuccess}%</div>
          <div class="stat-label">Avg Success</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">${summary.totalAgents}</div>
          <div class="stat-label">Total Agents</div>
        </div>
      </div>
    `;
  }

  /**
   * Render agent grid
   */
  renderGrid() {
    // Sort agents: front-office first, then by name
    const sorted = [...this.agents].sort((a, b) => {
      if (a.category !== b.category) {
        return a.category === 'front-office' ? -1 : 1;
      }
      return a.name.localeCompare(b.name);
    });

    const cards = sorted.map(agent => this.renderAgentCard(agent)).join('');

    return `
      <div class="agents-grid">
        ${cards}
      </div>
    `;
  }

  /**
   * Render a single agent card
   */
  renderAgentCard(agent) {
    const statusClass = `status-${agent.status}`;
    const successColor = this.getSuccessColor(agent.successRate);

    return `
      <div class="agent-desk ${statusClass} clickable" data-agent="${agent.name}">
        <div class="agent-status-dot"></div>

        <div class="agent-header">
          <div class="agent-icon">${agent.icon}</div>
          <div class="agent-name-block">
            <div class="agent-name">${this.formatName(agent.name)}</div>
            <span class="agent-category-tag">${agent.category}</span>
          </div>
        </div>

        <div class="agent-stats">
          <div class="agent-stat">
            <span class="agent-stat-label">Success</span>
            <span class="agent-stat-value">${agent.successRate}%</span>
          </div>
          <div class="agent-stat">
            <span class="agent-stat-label">Total Runs</span>
            <span class="agent-stat-value">${agent.totalRuns}</span>
          </div>
        </div>

        <div class="agent-status-info ${agent.status}">
          <span class="agent-status-label">${this.capitalizeStatus(agent.status)}</span>
          <span class="agent-last-run">${this.formatLastRun(agent.lastRun)}</span>
        </div>

        <div class="agent-description">${agent.description}</div>

        <button class="agent-view-details">View Details →</button>
      </div>
    `;
  }

  /**
   * Render activity feed section
   */
  renderActivityFeed() {
    if (this.activities.length === 0) {
      return `
        <div class="activity-section">
          <div class="activity-title">Recent Activity</div>
          <p style="color: var(--text-2); font-size: 12px;">No recent activity</p>
        </div>
      `;
    }

    const items = this.activities.map(activity => {
      const statusClass = activity.success ? 'success' : 'error';
      return `
        <div class="activity-item">
          <div class="activity-icon">${this.getAgentIcon(activity.agent_name)}</div>
          <div class="activity-content">
            <div class="activity-agent">${this.formatName(activity.agent_name)}</div>
            <div class="activity-detail">${activity.details || 'Completed run'}</div>
          </div>
          <div class="activity-time">${this.formatActivityTime(activity.timestamp)}</div>
        </div>
      `;
    }).join('');

    return `
      <div class="activity-section">
        <div class="activity-title">Recent Activity</div>
        <div class="activity-list">
          ${items}
        </div>
      </div>
    `;
  }

  /**
   * Render modal (hidden by default)
   */
  renderModal() {
    return `
      <div class="modal-overlay" id="agentModal">
        <div class="modal-content">
          <div class="modal-header">
            <div class="modal-title">
              <div class="modal-agent-name" id="modalAgentName">Agent Name</div>
              <div class="modal-agent-category" id="modalAgentCategory">Category</div>
            </div>
            <button class="modal-close-btn" id="modalCloseBtn">✕</button>
          </div>

          <div class="modal-body" id="modalBody">
            <!-- Dynamically populated -->
          </div>

          <div class="modal-footer">
            <button class="modal-btn" id="modalRefreshBtn">Refresh Data</button>
            <button class="modal-btn primary" id="modalCloseBottomBtn">Close</button>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * Show agent details modal
   */
  async showAgentDetails(agentName) {
    try {
      // Fetch detailed data
      const [statusResponse, historyResponse, outputResponse] = await Promise.all([
        fetch(`${this.apiBaseUrl}/api/agents/track/status`),
        fetch(`${this.apiBaseUrl}/api/agents/track/${agentName}/history?limit=10`),
        fetch(`${this.apiBaseUrl}/api/agents/track/${agentName}/latest-output`)
      ]);

      const statusData = await statusResponse.json();
      const historyData = await historyResponse.json();
      const outputData = await outputResponse.json();

      const agent = statusData.agents.find(a => a.name === agentName);
      if (!agent) return;

      // Build modal content
      const modalBody = document.getElementById('modalBody');
      modalBody.innerHTML = `
        <div class="modal-section">
          <div class="modal-section-title">Current Stats</div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">Status</span>
            <span class="modal-stat-value">${this.capitalizeStatus(agent.status)}</span>
          </div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">Success Rate</span>
            <span class="modal-stat-value">${agent.successRate}%</span>
          </div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">Total Runs</span>
            <span class="modal-stat-value">${agent.totalRuns}</span>
          </div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">Last Run</span>
            <span class="modal-stat-value">${this.formatLastRun(agent.lastRun)}</span>
          </div>
        </div>

        <div class="modal-section">
          <div class="modal-section-title">File Info</div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">File Size</span>
            <span class="modal-stat-value">${this.formatBytes(agent.fileSize)}</span>
          </div>
          <div class="modal-stat-row">
            <span class="modal-stat-label">Output File</span>
            <span class="modal-stat-value" style="font-size: 11px; word-break: break-all;">
              ${agent.outputFile ? agent.outputFile.split('/').pop() : 'N/A'}
            </span>
          </div>
        </div>

        <div class="modal-section modal-history">
          <div class="modal-section-title">Run History</div>
          ${historyData.runs.map((run, i) => `
            <div class="run-item">
              <div class="run-time">${new Date(run.timestamp).toLocaleString()}</div>
              <span class="run-status ${run.success ? 'success' : 'error'}">
                ${run.success ? 'Success' : 'Error'}
              </span>
              <div style="font-size: 11px; color: var(--text-2); margin-top: 4px;">
                ${this.formatBytes(run.file_size)}
              </div>
            </div>
          `).join('')}
        </div>

        ${outputData.content ? `
          <div class="modal-section modal-output">
            <div class="modal-section-title">Latest Output Preview</div>
            <div class="output-preview">${this.escapeHtml(outputData.content)}</div>
          </div>
        ` : ''}
      `;

      // Update header
      document.getElementById('modalAgentName').textContent = this.formatName(agentName);
      document.getElementById('modalAgentCategory').textContent = `${agent.category} • ${agent.description}`;

      // Show modal
      document.getElementById('agentModal').classList.add('active');
    } catch (error) {
      console.error('[AgentsOffice] Error showing agent details:', error);
      this.showError('Failed to load agent details');
    }
  }

  /**
   * Attach event listeners
   */
  attachEventListeners() {
    // Agent card clicks
    document.querySelectorAll('.agent-desk.clickable').forEach(card => {
      card.addEventListener('click', (e) => {
        const agentName = card.dataset.agent;
        this.showAgentDetails(agentName);
      });
    });

    // Modal close buttons
    const modal = document.getElementById('agentModal');
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.remove('active');
        }
      });

      document.getElementById('modalCloseBtn')?.addEventListener('click', () => {
        modal.classList.remove('active');
      });

      document.getElementById('modalCloseBottomBtn')?.addEventListener('click', () => {
        modal.classList.remove('active');
      });

      document.getElementById('modalRefreshBtn')?.addEventListener('click', async () => {
        const agentName = document.getElementById('modalAgentName').textContent;
        // Find actual agent name from formatted name
        const actualName = this.agents.find(a => this.formatName(a.name) === agentName)?.name;
        if (actualName) {
          await this.showAgentDetails(actualName);
        }
      });
    }
  }

  /**
   * Start auto-refresh interval
   */
  startAutoRefresh() {
    if (this.refreshInterval) clearInterval(this.refreshInterval);

    // Refresh every hour
    this.refreshInterval = setInterval(async () => {
      if (this.autoRefreshEnabled) {
        console.log('[AgentsOffice] Auto-refreshing...');
        await this.loadAgentStatus();
        await this.loadActivityFeed();
        this.render();
        this.attachEventListeners();
      }
    }, 60 * 60 * 1000); // 1 hour
  }

  /**
   * Refresh now
   */
  async refresh() {
    console.log('[AgentsOffice] Manual refresh');
    await this.loadAgentStatus();
    await this.loadActivityFeed();
    this.render();
    this.attachEventListeners();
  }

  /**
   * Show error message
   */
  showError(message) {
    if (!this.container) return;
    this.container.innerHTML = `
      <div style="padding: 20px; text-align: center; color: var(--red);">
        <div style="font-size: 18px; margin-bottom: 8px;">❌</div>
        <div>${message}</div>
      </div>
    `;
  }

  /**
   * Destroy and cleanup
   */
  destroy() {
    if (this.refreshInterval) {
      clearInterval(this.refreshInterval);
    }
  }

  // ===== Helper Methods =====

  formatName(agentName) {
    return agentName
      .split('-')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  }

  capitalizeStatus(status) {
    return status.charAt(0).toUpperCase() + status.slice(1);
  }

  formatLastRun(timestamp) {
    if (!timestamp) return 'Never';

    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;

    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h ago`;

    const diffDays = Math.floor(diffHours / 24);
    if (diffDays < 7) return `${diffDays}d ago`;

    return date.toLocaleDateString();
  }

  formatActivityTime(timestamp) {
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);

    if (diffMins < 1) return 'now';
    if (diffMins < 60) return `${diffMins}m`;

    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h`;

    return date.toLocaleDateString();
  }

  formatBytes(bytes) {
    if (!bytes) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 10) / 10 + ' ' + sizes[i];
  }

  getSuccessColor(rate) {
    if (rate >= 90) return 'var(--green)';
    if (rate >= 70) return 'var(--amber)';
    return 'var(--red)';
  }

  getAgentIcon(agentName) {
    const agent = this.agents.find(a => a.name === agentName);
    return agent?.icon || '❓';
  }

  isToday(timestamp) {
    if (!timestamp) return false;
    const date = new Date(timestamp);
    const today = new Date();
    return date.toDateString() === today.toDateString();
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

export default AgentsOffice;
