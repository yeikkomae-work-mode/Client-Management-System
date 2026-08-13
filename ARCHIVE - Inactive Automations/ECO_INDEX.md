# ECO System Index
**Master Reference for All ECO Files**  
**Last Updated:** 2026-08-06 00:15 PHT  
**Sync Status:** ✅ All Files Current

---

## How to Use This Index

Each section below links to a file with a one-sentence description of what it contains.

**In Claude Chat:** Mention the file, e.g., `@ECO_CLIENTS.md tell me when Chris is available`  
**In Claude Code:** `cat ECO_*.md | grep "search-term"`  
**For quick reference:** Use the table below

---

## File Directory

### 📊 STATUS & OVERVIEW

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_MASTER_STATUS.md** | Full system overview: active automations, browser profiles, monitoring, workflows | 4.2KB | 2026-08-06 00:15 |
| **ECO_README.md** | Quick start guide for new users or Claude Code CLI access | 6.1KB | 2026-08-06 00:15 |
| **ECO_SYNC_VERIFICATION.md** | Verification checklist proving all files are synced and current | 5.3KB | 2026-08-06 00:15 |
| **ECO_INDEX.md** | This file — master reference and navigation | 3.2KB | 2026-08-06 00:15 |

### 👥 PEOPLE & CLIENTS

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_CLIENTS.md** | Client registry with names, zones, working hours, tools, and status | 1.8KB | 2026-08-05 11:38 |

**Quick Reference:**
- Chris Caffera (Fractio): 2pm-11pm PHT
- Chris Drew (Satlas): 1pm-4pm PHT
- Yoni (Albertscott): 9pm-5am PHT
- Krishna (Peru campaign): Async, Global
- Chris Soriano: Project-based

### ⚙️ WORKFLOWS & AUTOMATIONS

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_WORKFLOWS.md** | Active workflows: LinkedIn posting (v1.0), morning email briefing (active), Lemwarm monitoring (active) | 3.1KB | 2026-08-05 11:50 |

**Active Automations:**
- 8:00 AM PHT: Morning Email Briefing (`eco-morning-email-briefing`)
- 9:00 AM PHT: Lemwarm Health Check (`lemwarm-alex-daily-monitor`)

### 📧 EMAIL & MONITORING

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_EMAIL_INTELLIGENCE.md** | Complete email monitoring config: VIP watchers, Fractio tracking, webinar handling, auto-filters | 3.6KB | 2026-08-05 11:50 |

**Monitored Accounts:**
- Gmail: yeikkomae@gmail.com
- Outlook: eikko ybanez

**VIP Watchers:** Chris Caffera, Chris Drew, Chris Soriano, Yoni, Krishna  
**Special Tracking:** Fractio (@fractio.co, Fatin Kwasny)

### 🔌 DATA & CONNECTIONS

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_LIVE_DATA.md** | Data source connections: live APIs (Smartlead, Pipedrive, Apollo), manual inputs (HubSpot, Lemlist), streaming (Gmail, Calendar) | 2.4KB | 2026-08-05 11:38 |

**Connected Tools:**
- Live: Smartlead, Pipedrive, TimeDoctors, Apollo
- Manual: HubSpot, Lemlist, LinkedIn
- Streaming: Gmail, Calendar

### 📝 SESSION LOGS & HISTORY

| File | Purpose | Size | Last Updated |
|------|---------|------|--------------|
| **ECO_SESSION_LOG_20260805.md** | Today's session summary: setup progress, files created, pending tasks | 2.1KB | 2026-08-05 11:38 |

---

## Quick Reference Map

### By Use Case

**"What's my status today?"**
→ `ECO_MASTER_STATUS.md`

**"What are my automations?"**
→ `ECO_WORKFLOWS.md` or `ECO_MASTER_STATUS.md` section "Active Executions"

**"Tell me about [client]"**
→ `ECO_CLIENTS.md`

**"Why didn't I get an email alert?"**
→ `ECO_EMAIL_INTELLIGENCE.md`

**"What tools are connected?"**
→ `ECO_LIVE_DATA.md`

**"Is everything synced?"**
→ `ECO_SYNC_VERIFICATION.md`

**"How do I use this system?"**
→ `ECO_README.md` (new user) or `ECO_INDEX.md` (reference)

### By Time Sensitivity

**Need to know NOW:**
1. `ECO_MASTER_STATUS.md` — system overview (30 sec read)
2. `ECO_CLIENTS.md` — client hours/contact info (1 min read)

**Before a meeting:**
1. `ECO_CLIENTS.md` — client details
2. `ECO_WORKFLOWS.md` — what's active with them
3. Recent emails in Gmail/Claude Chat

**Troubleshooting:**
1. `ECO_SYNC_VERIFICATION.md` — check status
2. `ECO_SESSION_LOG_*.md` — review history
3. Ask Claude: "Is [task] running?"

---

## Scheduled Tasks & Automation Reference

```
🕘 8:00 AM PHT Daily
   └─ eco-morning-email-briefing
      Monitors: Gmail + Outlook
      Alerts on: Chris, clients, Fractio, webinars
      
🕘 9:00 AM PHT Daily
   └─ lemwarm-alex-daily-monitor
      Tracks: alex's deliverability score (70%)
      Alerts at: 90%+ and 100%
```

---

## File Access Methods

### In Claude Chat
**Direct mention:**
```
@ECO_CLIENTS.md what's Chris Caffera's timezone?
@ECO_WORKFLOWS.md is LinkedIn posting active?
```

**Ask Claude:**
```
Show me my active automations
List all my scheduled tasks
What's my Lemwarm score?
```

### In Claude Code CLI
```bash
# List all ECO files
ls -la ~/Claude\ Code/ECO_*.md

# Search for content
grep -r "Chris Caffera" ~/Claude\ Code/
grep "ACTIVE" ~/Claude\ Code/ECO_*.md

# View a specific file
cat ~/Claude\ Code/ECO_MASTER_STATUS.md
```

### For Next Session
All files persist in `/Users/eikkoyu/Claude Code/`  
Just ask: "Where are we with ECO?" or reference any file

---

## Status Dashboard

| System | Status | Last Check | Next Action |
|--------|--------|-----------|------------|
| Morning Email Briefing | ✅ Active | 2026-08-06 00:15 | Runs 8 AM PHT tomorrow |
| Lemwarm Monitor | ✅ Active | 2026-08-06 00:15 | Runs 9 AM PHT tomorrow |
| Gmail Monitoring | ✅ Active | Now | Continuous |
| Outlook Monitoring | ✅ Active | Now | Continuous |
| LinkedIn Workflow | 🟡 Refining | 2026-08-05 11:50 | Awaiting approval |
| File Sync | ✅ Complete | 2026-08-06 00:15 | All 8 files current |

---

## File Sizes & Sync Timing

```
ECO_MASTER_STATUS.md          4.2 KB  ←─┐
ECO_README.md                 6.1 KB    │
ECO_SYNC_VERIFICATION.md      5.3 KB    │
ECO_INDEX.md                  3.2 KB    │
ECO_CLIENTS.md                1.8 KB    │
ECO_WORKFLOWS.md              3.1 KB    │ Auto-synced
ECO_LIVE_DATA.md              2.4 KB    │ whenever updates
ECO_SESSION_LOG_20260805.md   2.1 KB  ←─┘

Total: ~28 KB (fast sync)
Location: /Users/eikkoyu/Claude Code/
Access: Instant from Claude Chat or CLI
```

---

## Workflow to Add/Update a File

1. **Create or edit** the ECO_*.md file
2. **Tell Claude:** "Save this to Claude Code"
3. **Files auto-update** in `/Users/eikkoyu/Claude Code/`
4. **Accessible immediately** from Claude Chat or Claude Code CLI
5. **Persists across sessions** — always there for your next chat

---

## When to Reference Each File

### Daily
- **ECO_MASTER_STATUS.md** — "What's my status?"

### Weekly
- **ECO_CLIENTS.md** — "Planning meetings this week"
- **ECO_WORKFLOWS.md** — "Is LinkedIn post going out?"

### Monthly
- **ECO_SESSION_LOG_*.md** — "What did we accomplish?"
- **ECO_SYNC_VERIFICATION.md** — "Is everything still synced?"

### As-Needed
- **ECO_EMAIL_INTELLIGENCE.md** — "Why isn't [client] in my briefing?"
- **ECO_LIVE_DATA.md** — "Are my tools still connected?"
- **ECO_README.md** — "How do I use [feature]?"

---

## Support & Maintenance

**Nothing required from you** — ECO runs automatically.

**If you want to:**
- Add a client → Update `ECO_CLIENTS.md`
- Add monitoring → Update `ECO_EMAIL_INTELLIGENCE.md`
- Change schedule → Ask Claude to update the task
- Debug an issue → Check `ECO_SYNC_VERIFICATION.md` first

**To resume a task:**
```
In Claude Chat: "Resume eco-morning-email-briefing"
In Claude Code: Check status with grep or ask Claude
```

---

## Entry Points by Role

### First Time User
1. Read: `ECO_README.md`
2. Skim: `ECO_MASTER_STATUS.md`
3. Check: `ECO_CLIENTS.md` (your people)

### Returning User
1. Scan: `ECO_MASTER_STATUS.md` (what's active)
2. Ask Claude: "Any updates since yesterday?"
3. Check: Relevant file (see "By Use Case" above)

### Claude Code User
1. Run: `cat ECO_README.md` (setup reference)
2. Use: `grep` to search across files
3. Check: `ECO_SYNC_VERIFICATION.md` for status

### Automation Troubleshooter
1. Check: `ECO_SYNC_VERIFICATION.md` (is it active?)
2. Review: `ECO_SESSION_LOG_*.md` (what happened?)
3. Ask Claude: "Debug [task name]"

---

## Navigation Shortcuts

**All ECO files at:**
```
/Users/eikkoyu/Claude Code/ECO_*.md
```

**Quick view all:**
```bash
ls -lh ~/Claude\ Code/ECO_*.md
cat ~/Claude\ Code/ECO_MASTER_STATUS.md  # System overview
cat ~/Claude\ Code/ECO_README.md         # Quick start
```

**Search everything:**
```bash
grep -r "your-search" ~/Claude\ Code/ECO_*.md
```

**Check sync status:**
```bash
cat ~/Claude\ Code/ECO_SYNC_VERIFICATION.md
```

---

## Summary

**You have:**
- ✅ 8 synced documentation files
- ✅ 2 active daily automations
- ✅ 2 configured browser profiles
- ✅ 5 clients tracked
- ✅ 3 workflows (2 active, 1 refining)

**Located at:** `/Users/eikkoyu/Claude Code/`  
**Accessible from:** Claude Chat + Claude Code CLI  
**Status:** Production ready  
**Last verified:** 2026-08-06 00:15 PHT

**Next briefing:** Tomorrow 8:00 AM PHT

---

*This index was created to help you navigate ECO. Everything is synced and ready to use.*
