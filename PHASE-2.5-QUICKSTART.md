# Phase 2.5 Quick Start

Get the Agent Tracking system running in 3 minutes.

## 1. Install Backend (30 seconds)

```bash
cd /Users/eikkoyu/Claude\ Code:Cowork/Client-Management-System/backend
npm install
```

## 2. Start Backend (10 seconds)

```bash
npm start
```

You should see:
```
[Server] Agent Tracking System running on http://localhost:3001
[FileWatch] Watcher ready and monitoring
```

**Leave this running in a terminal tab.**

## 3. Open Frontend (5 seconds)

Open this URL in your browser:

```
file:///Users/eikkoyu/Claude\ Code:Cowork/Client-Management-System/frontend/agents.html
```

You should see the Agents Office with 10 agent desks.

## Done ✓

**The system is now:**
- ✓ Monitoring `/PROJECTS/Active/` and `/OUTPUT/End-of-Day Reports/` for file changes
- ✓ Recording agent runs to database
- ✓ Serving live API at `http://localhost:3001/api/agents/track/status`
- ✓ Auto-refreshing dashboard every hour

## Test It

1. **Trigger a run:**
   - Make any change to a file in `/PROJECTS/Active/`
   - Wait ~2 seconds for detection
   - Refresh the agents page → should show updated "Last Run" time

2. **Check backend health:**
   ```bash
   curl http://localhost:3001/health
   ```

3. **Get all agent status:**
   ```bash
   curl http://localhost:3001/api/agents/track/status
   ```

## Stop Backend

Press `Ctrl+C` in the terminal running `npm start`.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `npm install` fails | Try: `sudo npm install` or update Node.js |
| Port 3001 in use | Change PORT in `.env` or kill process: `lsof -i :3001` |
| "Backend not responding" | Check server is running and at correct port |
| Files not detected | Check file is `.md` and in monitored folder |

## Detailed Docs

See `PHASE-2.5-README.md` for:
- Full API documentation
- Database schema
- File detection logic
- Development notes
- Production deployment

---

**Questions?** Check the console logs (prefixed with `[FileWatch]`, `[API]`, `[Server]`).
