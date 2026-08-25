# Phase 2.5 Implementation Checklist

Verify that Phase 2.5 is fully installed and operational.

## Pre-Installation Checklist

- [ ] Node.js version 18+ installed
  ```bash
  node --version
  ```
  
- [ ] npm available
  ```bash
  npm --version
  ```

- [ ] Cowork directory exists
  ```bash
  ls -la "/Users/eikkoyu/Claude Code:Cowork/Client-Management-System/"
  ```

- [ ] Key folders present:
  - [ ] `PROJECTS/Active/`
  - [ ] `OUTPUT/End-of-Day Reports/`
  - [ ] `.claude/agents/`

## Installation Checklist

- [ ] Backend directory created
  ```bash
  ls -la backend/
  ```

- [ ] All backend files present:
  - [ ] `server.js`
  - [ ] `db.js`
  - [ ] `package.json`
  - [ ] `.env.example`
  - [ ] `.gitignore`
  - [ ] `services/file-watcher.js`
  - [ ] `routes/agents-tracking.js`

- [ ] All frontend files present:
  - [ ] `frontend/agents.html`
  - [ ] `frontend/css/agents-office.css`
  - [ ] `frontend/js/components/agents-office.js`
  - [ ] `frontend/js/pages/agents.js`

- [ ] Documentation files present:
  - [ ] `PHASE-2.5-README.md`
  - [ ] `PHASE-2.5-QUICKSTART.md`
  - [ ] `PHASE-2.5-FILES.md`
  - [ ] `PHASE-2.5-CHECKLIST.md` (this file)

- [ ] npm dependencies installed
  ```bash
  cd backend && npm install
  ```
  Look for: `added X packages`

- [ ] node_modules created
  ```bash
  ls backend/node_modules | head -10
  ```

## Startup Verification

- [ ] Backend starts without errors
  ```bash
  cd backend && npm start
  ```
  Look for:
  - `[Server] Agent Tracking System running on http://localhost:3001`
  - `[FileWatch] Watcher ready and monitoring`
  - No `ERROR:` messages

- [ ] Server responds to health check
  ```bash
  curl http://localhost:3001/health
  ```
  Expected response: `{"status":"ok",...}`

- [ ] Database created
  ```bash
  ls -la backend/agent-tracking.db
  ```

- [ ] Database tables exist
  ```bash
  sqlite3 backend/agent-tracking.db ".tables"
  ```
  Expected output: `agent_metadata agent_runs file_monitoring_cache`

## API Verification

All endpoints should return JSON with `"success": true`:

- [ ] `/health` endpoint
  ```bash
  curl http://localhost:3001/health | jq .
  ```

- [ ] Agent status endpoint
  ```bash
  curl http://localhost:3001/api/agents/track/status | jq .
  ```

- [ ] Activity feed endpoint
  ```bash
  curl http://localhost:3001/api/agents/track/activity-feed/recent | jq .
  ```

- [ ] Stats endpoint
  ```bash
  curl http://localhost:3001/api/agents/track/stats/aggregate | jq .
  ```

- [ ] Individual agent history (replace with actual agent name)
  ```bash
  curl http://localhost:3001/api/agents/track/lead-prospector/history | jq .
  ```

## Frontend Verification

- [ ] Open agents.html in browser
  ```
  file:///Users/eikkoyu/Claude\ Code:Cowork/Client-Management-System/frontend/agents.html
  ```

- [ ] Page loads without errors
  - [ ] "Agents Office 🏢" heading visible
  - [ ] 10 agent cards displayed in grid
  - [ ] Quick stats row visible (4 cards)

- [ ] Agent cards display correctly
  - [ ] Each card shows: agent name, category tag, status indicator, success rate
  - [ ] Status dot (colored circle) visible in top-right
  - [ ] "View Details →" button visible

- [ ] Click on an agent card
  - [ ] Modal opens
  - [ ] Shows: agent name, category, current stats
  - [ ] Shows run history list
  - [ ] Close button works

- [ ] Activity feed shows
  - [ ] At least one activity item
  - [ ] Agent name, details, and time visible

- [ ] Theme toggle works
  - [ ] Press Ctrl+D to toggle dark mode
  - [ ] Colors change appropriately

## File Detection Test

1. Modify a file in `/PROJECTS/Active/`:
   ```bash
   echo "# Test run $(date)" >> "/Users/eikkoyu/Claude Code:Cowork/Client-Management-System/PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md"
   ```

2. Wait 2-3 seconds

3. Check database for new entry:
   ```bash
   sqlite3 backend/agent-tracking.db "SELECT agent_name, timestamp FROM agent_runs ORDER BY timestamp DESC LIMIT 1;"
   ```

4. Expected: See an agent name and current timestamp

5. Refresh agents.html page
   - [ ] Agent's "Last Run" time updated
   - [ ] Activity feed shows new entry

## Configuration Verification

- [ ] `.env.example` present in backend/
  - [ ] Contains PORT, COWORK_DIR settings
  - [ ] Can be copied to `.env` for customization

- [ ] Database path is writable
  ```bash
  touch backend/agent-tracking.db
  ```
  Should not produce permission error

- [ ] File watch paths are readable
  ```bash
  ls -la "/Users/eikkoyu/Claude Code:Cowork/Client-Management-System/PROJECTS/Active/"
  ls -la "/Users/eikkoyu/Claude Code:Cowork/Client-Management-System/OUTPUT/End-of-Day Reports/"
  ```

## Database Verification

- [ ] Database file exists and has content
  ```bash
  du -h backend/agent-tracking.db
  ```
  Should show size >10KB

- [ ] Agent metadata populated
  ```bash
  sqlite3 backend/agent-tracking.db "SELECT COUNT(*) FROM agent_metadata;"
  ```
  Expected: `10` (for 10 agents)

- [ ] Agent metadata includes all 10 agents
  ```bash
  sqlite3 backend/agent-tracking.db "SELECT agent_name FROM agent_metadata ORDER BY agent_name;"
  ```
  Expected to see all of:
  - [ ] billing-auditor
  - [ ] copywriter
  - [ ] file-organizer
  - [ ] inbox-triage
  - [ ] lead-prospector
  - [ ] market-scout
  - [ ] meeting-summarizer
  - [ ] onboarding-guide
  - [ ] project-manager
  - [ ] reply-handler

## Browser Console Verification

Open browser DevTools (F12) → Console tab:

- [ ] No errors about CORS
- [ ] No 404 errors for files/assets
- [ ] No `fetch()` errors
- [ ] See console logs like `[AgentsOffice] Initialized...` or similar

## Performance Baseline

Check performance under normal conditions:

- [ ] Page load time: <2 seconds
- [ ] Agent cards render: <1 second
- [ ] Modal open on click: <1 second
- [ ] API response: <500ms
- [ ] No console errors or warnings

## Optional: Advanced Configuration

- [ ] Copy .env.example to .env
  ```bash
  cp backend/.env.example backend/.env
  ```

- [ ] Customize PORT in .env (if 3001 in use)

- [ ] Set LOG_LEVEL=debug for verbose logging

- [ ] Test with different API base URL

## Shutdown Verification

- [ ] Stop backend server (Ctrl+C in terminal)
  - [ ] See `[Server] Shutting down gracefully...`
  - [ ] See `[FileWatch] Watcher closed`
  - [ ] Clean exit (no errors)

- [ ] Verify database still intact after shutdown
  ```bash
  sqlite3 backend/agent-tracking.db "SELECT COUNT(*) FROM agent_runs;"
  ```
  Should return a number (not error)

## Documentation Review

- [ ] Read PHASE-2.5-QUICKSTART.md
  - [ ] Understand 3-step startup
  - [ ] Know how to test

- [ ] Skim PHASE-2.5-README.md
  - [ ] Understand architecture
  - [ ] Know API endpoints
  - [ ] Familiar with troubleshooting

- [ ] Review PHASE-2.5-FILES.md
  - [ ] Understand file organization
  - [ ] Know database schema
  - [ ] Reference for future customization

## Final Verification

Run this comprehensive test:

```bash
# Terminal 1: Start server
cd backend && npm start

# Terminal 2: Run tests
curl -s http://localhost:3001/health | jq .status
curl -s http://localhost:3001/api/agents/track/status | jq '.summary'
curl -s http://localhost:3001/api/agents/track/stats/aggregate | jq '.aggregate.total_agents'
```

Expected output:
```
"ok"
{
  "totalAgents": 10,
  "activeNow": 0-10,
  "completedToday": 0-10,
  "averageSuccessRate": "XX%"
}
10
```

## Troubleshooting Checklist

If something doesn't work:

- [ ] Check if Node.js is installed: `node --version`
- [ ] Check if port 3001 is in use: `lsof -i :3001`
- [ ] Check backend console for `[ERROR]` messages
- [ ] Check browser console (F12) for JavaScript errors
- [ ] Verify file paths are correct and readable
- [ ] Check database permissions: `ls -la backend/agent-tracking.db`
- [ ] Try fresh database: `rm backend/agent-tracking.db && npm start`
- [ ] Check network: `curl http://localhost:3001/health`

## Sign-Off

When all checkboxes are complete:

- [ ] Phase 2.5 is **READY FOR PRODUCTION**
- [ ] Backend is monitoring file changes
- [ ] Frontend visualizes agent status correctly
- [ ] Database is recording runs
- [ ] API endpoints respond correctly
- [ ] Documentation is complete and accessible

**Date Verified:** _______________  
**Verified By:** _______________  
**Notes:** _______________________________________________

---

## Next Steps

Once Phase 2.5 is verified:

1. **Phase 3**: Integrate Agents page link into Central Command dashboard
2. **Phase 4**: Add agent trends and historical charts
3. **Phase 5**: Implement notifications and alerts

Congratulations! 🎉 Phase 2.5 is live.
