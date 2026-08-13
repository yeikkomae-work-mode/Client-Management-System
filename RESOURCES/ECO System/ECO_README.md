# ECO: Eikko's Chief of Staff System
**Version:** 1.0  
**Last Updated:** 2026-08-06  
**Status:** ✅ Production Ready

**Note (Aug 13):** every `ECO_MASTER_STATUS.md` / `ECO_*.md` reference below points to files that have since moved to `ARCHIVE - Inactive Automations/` at the root of Client-Management-System (they described automations that are now disabled). See that folder's README for current status, and `TEMPLATES/01 Automation Daily Routine/ECO - Chief of Staff Guide.md` for the up-to-date consolidated guide.

---

## What is ECO?

ECO is your personal AI Chief of Staff system. It monitors emails, tracks sales metrics, manages automations, and delivers intelligent briefings — all synced and accessible from Claude Chat, Claude Code CLI, or your desktop.

Think of it as having a hyper-organized assistant running in the background.

---

## Quick Start (30 seconds)

### In Claude Chat
Just ask:
```
What's my status today?
Check email for Chris's updates
Show me Lemwarm score
```

ECO reads from these files automatically.

### In Claude Code CLI
```bash
cd ~/Claude\ Code/
cat ECO_MASTER_STATUS.md           # System overview
grep "Chris Caffera" ECO_CLIENTS.md # Find client info
cat ECO_EMAIL_INTELLIGENCE.md      # Email config
```

### Scheduled Automations
They just work. No action needed:
- **8:00 AM PHT** → Morning email briefing (Gmail + Outlook)
- **9:00 AM PHT** → Lemwarm health check (alex's score)

---

## File Guide

| File | What It Does | When to Read |
|------|-------------|--------------|
| **ECO_MASTER_STATUS.md** | Full system snapshot + all active automations | Daily status check |
| **ECO_README.md** | This file — quick reference | First time setup |
| **ECO_CLIENTS.md** | Client registry, hours, contact methods | Planning meetings, context |
| **ECO_WORKFLOWS.md** | Active workflows + automation schedules | Understanding what's running |
| **ECO_EMAIL_INTELLIGENCE.md** | Email monitoring config + filters | Troubleshooting email issues |
| **ECO_LIVE_DATA.md** | Tool connections (API, manual, streaming) | Checking data freshness |
| **ECO_SESSION_LOG_*.md** | Historical session summaries | Audit trail + context |
| **ECO_SYNC_VERIFICATION.md** | Verification checklist + handoff | System health checks |

---

## What's Running Right Now

### ✅ Automations Active

**ECO Morning Email Briefing** (Task: `eco-morning-email-briefing`)
- Runs: 8:00 AM PHT daily
- Monitors: Gmail (yeikkomae@gmail.com) + Outlook (eikko ybanez)
- Alerts on: Chris Caffera, Chris Drew, Chris Soriano, Yoni, Krishna
- Special tracking: Fractio emails, webinars (auto-calendar)
- Filters out: Promotions, social, updates
- **Next run:** Tomorrow at 8:00 AM PHT

**Lemwarm Health Monitor** (Task: `lemwarm-alex-daily-monitor`)
- Runs: 9:00 AM PHT daily
- Tracks: alex's deliverability score
- Alerts at: 90%+ and 100%
- Current score: 70% (warming)
- **Next run:** Tomorrow at 9:00 AM PHT

### 🟡 Workflows Refining

**LinkedIn Content Posting** (Fractio / Chris Caffera)
- Status: v1.0, refining
- Cadence: Weekly posts
- Content: Pricing models, AI economics, CPA disruption
- Platform: LinkedIn (as Fatin Kwasny, Fractio founder)
- **Next:** Auto-trigger when Chris approves

### 🟢 Browser Profiles Ready

- **Fractio.co** → eikko.ybanez@fractio.co (LinkedIn, Lemlist, Lemwarm, Apollo)
- **Personal VA** → yeikkomae@gmail.com (Gmail, Outlook, Calendar)

---

## Your Clients (At a Glance)

| Client | Zone | Hours | Tools | Status |
|--------|------|-------|-------|--------|
| **Chris Caffera** (Fractio) | PH | 2pm-11pm | HubSpot, Lemlist, LinkedIn, Apollo | 🔴 Active LinkedIn |
| **Chris Drew** (Satlas) | AU | 1pm-4pm | Apollo | 🟢 Live |
| **Yoni** (Albertscott) | PH | 9pm-5am | Smartlead, Pipedrive, TimeDoctors | 🟢 Live |
| **Krishna** (Peru Campaign) | Global | Async | Apollo | 🟢 Live |
| **Chris Soriano** | Global | Project | Email | 🟡 As-needed |

---

## Email Monitoring at a Glance

**Who ECO Watches For:**
- Chris Caffera (all emails)
- Chris Drew (all emails)
- Chris Soriano (project context)
- Yoni (account updates)
- Krishna (campaign progress)

**Special Tracking:**
- Fractio: @fractio.co domain + Fatin Kwasny mentions + "Fractio" keyword
- Webinars: Auto-extracts details + creates calendar events

**What ECO Ignores:**
- Promotional emails
- Social notifications
- Update digests

---

## Common Tasks

### "I need to prep a meeting with [client]"
```bash
grep -A5 "[client]" ECO_CLIENTS.md
cat ECO_EMAIL_INTELLIGENCE.md | grep -i chris
```

### "What's happening with sales this week?"
Ask in Claude Chat:
```
Summarize this week's emails from my clients
Show me Apollo pipeline for Chris Drew
```

### "Check if alex's Lemwarm is ready"
```bash
# Next check: 9 AM PHT tomorrow
# Current score: 70%
# Target: 90%+ for campaigns
cat ECO_MASTER_STATUS.md | grep -i lemwarm
```

### "Update client info"
1. Edit `ECO_CLIENTS.md`
2. Ask Claude to sync: "Save these changes to ECO_CLIENTS.md"
3. Done — automations read the updated file

---

## Customization & Adjustments

### Change Briefing Time
In Claude Chat:
```
Update eco-morning-email-briefing to 7 AM PHT
```

### Add a New Client to Monitoring
1. Edit `ECO_CLIENTS.md` → add client row
2. Edit `ECO_EMAIL_INTELLIGENCE.md` → add email/domain under Priority 1
3. Ask Claude: "Update eco-morning-email-briefing to include [client]"

### Pause an Automation
```
Stop eco-morning-email-briefing
Stop lemwarm-alex-daily-monitor
```

### View Recent Emails
In Claude Chat (using Gmail API):
```
Show me unread emails from Chris Caffera
Find webinar invitations in my inbox
```

---

## Troubleshooting

### "I didn't get a morning briefing"
1. Check time: Should arrive at 8 AM PHT
2. In Claude Chat, ask: "Check if eco-morning-email-briefing ran"
3. Verify Gmail/Outlook are connected

### "Lemwarm alert didn't fire"
1. Check current score: https://app.lemwarm.com/teams/tea_frti7zwCWCFtBAYtZ/dashboard/usm_CwAQK7dHWRJqaahFh
2. Alert triggers at 90%+ or 100% only
3. Current score: Check `ECO_MASTER_STATUS.md`

### "I'm missing emails from a client"
1. Add email to VIP list in `ECO_EMAIL_INTELLIGENCE.md`
2. Update the morning briefing task
3. Or: Create a Gmail/Outlook label manually

### "Need to test without waiting for scheduled time"
In Claude Chat:
```
Run eco-morning-email-briefing now
Run lemwarm-alex-daily-monitor now
```

---

## Integration Points

**ECO connects to:**
- Gmail (real-time monitoring)
- Outlook (real-time monitoring)
- Google Calendar (auto-event creation)
- Apollo (Chris Drew, Krishna)
- Lemwarm (alex's score)
- Lemlist (Fractio email outreach)
- LinkedIn (Fatin's account)

**ECO is accessible from:**
- Claude Chat (this session)
- Claude Code CLI (claude mcp)
- Next-session resumption (files persist)

---

## Pro Tips

1. **Search files fast:**
   ```bash
   grep -r "your-search-term" ~/Claude\ Code/
   ```

2. **Keep history:**
   Every session logs to `ECO_SESSION_LOG_YYYYMMDD.md`

3. **Add notes:**
   Update any ECO_*.md file, ask Claude to sync

4. **Use in prompts:**
   ```
   @ECO_CLIENTS.md tell me if Chris is available
   ```

---

## Support & Maintenance

**If something breaks:**
1. Check `ECO_SYNC_VERIFICATION.md` for status
2. Review `ECO_SESSION_LOG_*.md` for context
3. Ask Claude: "What went wrong with eco-morning-email-briefing?"

**To add a new workflow:**
1. Document in `ECO_WORKFLOWS.md`
2. Create scheduled task in Claude Chat
3. Link in `ECO_CLIENTS.md`
4. Sync all files

---

## Next Steps

✅ **Already Done:**
- Email monitoring active (8 AM briefing)
- Lemwarm tracking active (9 AM alert)
- All clients registered
- All platforms connected
- All files synced

🟡 **Recommended:**
- Set up Gmail filter (optional, 2 min)
- Set up Outlook rule (optional, 2 min)
- Check first morning briefing tomorrow

📋 **When You're Ready:**
- Tell Claude to automate LinkedIn posting
- Add new clients as they join
- Create additional monitoring workflows

---

## Quick Links

- **Email Config:** `ECO_EMAIL_INTELLIGENCE.md`
- **Active Workflows:** `ECO_WORKFLOWS.md`
- **System Status:** `ECO_MASTER_STATUS.md`
- **Sync Check:** `ECO_SYNC_VERIFICATION.md`
- **Lemwarm Dashboard:** https://app.lemwarm.com/teams/tea_frti7zwCWCFtBAYtZ/dashboard/usm_CwAQK7dHWRJqaahFh

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-08-06 | Initial ECO system live |

---

**Status:** ✅ Production Ready  
**Last Verified:** 2026-08-06 00:15 PHT  
**Next Briefing:** Tomorrow 8:00 AM PHT  

Welcome to ECO. Your system is running smoothly.
