# Eikko's Client Management System

**Organized workspace for managing 5 active clients, prospective clients, automation, campaigns, and personal business operations.**

Last reorganized: Aug 6, 2026 | Status: 🟢 Fully organized (root folder cleaned up)

---

## 📂 Folder Structure

### **ABOUT ME**
Your personal profile and system overview.
- `CLAUDE.md` — System overview & working rules
- `GETTING STARTED.md` — Quick-start guide

### **CLIENT PROFILES**
One consolidated profile per client (quick-reference details + full engagement history merged into a single file each — previously split across separate quick/detailed files for Chris Drew and Yoni, merged Aug 13).
- `Important info.md` — Master reference (rates, contact, payment info)
- `Chris Caffera - Profile.md` — Personal Assistant ($7/hr, 20h/week, 2pm-11pm)
- `Chris Drew - Profile (Satlas).md` — Satlas Lead Gen, full engagement history, infrastructure & campaign playbook ($200 AUD/mo, 1pm-4pm)
- `Yoni - Profile (Albert Scott).md` — Albert Scott Outreach, full workflow reference incl. key people, tools, reply taxonomy, copy rules ($5/hr, 5h/day, 9pm-5am PHT)
- `Krishna - Profile.md` — Free Lead Gen (3h/week, flexible)
- `Chris Soriano - Profile.md` — Data Entry (as-needed, sporadic)

### **SKILLS**
Your skills documentation and competencies (empty — ready for expansion).

### **PROJECTS**
Active and prospective projects organized by status.
- **Active/** — Live task lists & the smartlead-pipedrive-automation codebase:
  - `MASTER-TASK-LIST-ACTIVE.md` — Albert Scott operations task list (owner: Yoni & Aiko)
  - `ACTION-PLAN-UNCATEGORIZED-MESSAGES.md` — Uncategorized message resolution (assigned to Rachel, on hold)
  - `YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md` — Feedback log on uncategorized messages
  - `LATEST-COMPLETED-WORK.md` — Most recent completed work summary
  - `smartlead-pipedrive-automation/` — Live Python codebase (git repo) syncing Smartlead ↔ Pipedrive
- **Prospective/** — New client onboarding
  - `NEW CLIENTS - ONBOARDING PIPELINE.md` — Penji (final interview next week) & Top Acquisitions (paid trial, due Aug 11)

### **TEMPLATES**
Reusable workflows and automation setup.
- **01 Automation Daily Routine/** — ECO system files, work logs, briefing prompts
- **02 Plugin Client Templates/** — Checklists, meeting templates, campaign trackers
- **03 App Dashboard & Work Logger/** — Browser-based work logging app

### **OUTPUT**
Reports, data, metrics, and end-of-day summaries from your work.
- **End-of-Day Reports/** — Daily logs per client (Chris Caffera, Chris Drew, Yoni, Krishna, Soriano)
- **Campaign Tracking/** — Live campaign metrics & logs:
  - `Chris Drew - Satlas Infrastructure & Campaigns.md`, `Plusvibe Mailbox Health - Daily Monitor.md`, `PLUSVIBE MONITORING SETUP.md`, `Instantly to Plusvibe - Campaign Migration Guide.md`, `Peru Silver Chain Wholesalers - Campaign Log.md`
  - `DOMAIN_INVENTORY.md` — Chris Drew's domain inventory
  - `Daily-Lead-Summary.md`, `Smartlead-Pipedrive-Sync-Log.md` — Daily sync/lead activity
  - `Q4-Toy-Campaign-Call-Notes-Yoni.md`, `Yoni-Projects-Active.md` — Yoni's active campaign work
- **Monthly Reports/** — Monthly financial summaries & expense tracking
- **Data & Metrics/** — `Salary & Income Tracking.md` (revenue across all clients)

### **RESOURCES**
System files, tool documentation, and reference materials.
- **ECO System/** — Claude Code Chief of Staff configuration, setup, session logs & sync verification (17 files)
- **Tools & API Details/** — `Connected Tools Status.md`, `tools_api_details.md`, `google_accounts_details.md`
  - **OAuth Credentials/** — Google OAuth client secret JSONs (Albert Scott, Fractio, Personal, Satlas) — ⚠️ sensitive, do not share
- **Workflows/** — Sync system docs, deployment guide, implementation blueprint, monitoring workflows, and `automation_logs/` (raw automation run logs)
- **Documentation/** — Reference guides, templates, how-tos (empty — ready for expansion)

---

## 🎯 Quick Navigation

### **Starting Your Day**
1. Open: `ABOUT ME/CLAUDE.md` (system overview)
2. Open: `CLIENT PROFILES/Important info.md` (quick client reference)
3. Run in Claude Code → `good morning` (auto-generates briefing)
4. Check: `TEMPLATES/03 App Dashboard & Work Logger/app.html` (open work logger)

### **Logging Work**
- Use the browser app: `TEMPLATES/03 App Dashboard & Work Logger/app.html`
- Or edit directly: `OUTPUT/End-of-Day Reports/[Client] - End of Day Log.md`

### **Checking Campaigns**
- Open: `OUTPUT/Campaign Tracking/[Campaign] - Campaign Log.md`
- Monitor: `OUTPUT/Campaign Tracking/Plusvibe Mailbox Health - Daily Monitor.md`

### **Checking Active Tasks**
- Open: `PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md`

### **Monthly Financial Review**
- Open: `OUTPUT/Monthly Reports/Monthly Income & Expense Review.md`

### **Activating ECO (AI Assistant)**
- Full guide: `TEMPLATES/01 Automation Daily Routine/ECO - Chief of Staff Guide.md` (merged from 5 former companion docs Aug 13)
- Quick start: `RESOURCES/ECO System/ECO - COWORK QUICK START.md`
- Configuration: `TEMPLATES/01 Automation Daily Routine/ECO - YOUR CONFIGURATION.md`
- Current live-vs-inactive automation status: `ARCHIVE - Inactive Automations/README.md` — most of ECO's original automations (morning briefing, Lemwarm monitor, PlusVibe monitor) are disabled as of Aug 6; only `daily-eod-sync` runs today

---

## 📊 Current Clients at a Glance

| Client | Folder | Rate | Hours | Status | Focus |
|--------|--------|------|-------|--------|-------|
| Yoni | CLIENT PROFILES | $5/hr | 5h/day (9pm-5am PHT) | ✅ Active | Outreach, Smartlead, Pipedrive |
| Chris Caffera | CLIENT PROFILES | $7/hr | 20h/week (2pm-11pm) | ✅ Active | Personal Assistant, ICP, Apollo |
| Chris Drew | CLIENT PROFILES | $200 AUD/mo | Variable (1pm-4pm) | ✅ Active | Lead Gen, Satlas, Plusvibe |
| Krishna | CLIENT PROFILES | Free | 3h/week | ✅ Active | Lead Gen, Apollo, Email sequences |
| Chris Soriano | CLIENT PROFILES | $7/hr | As-needed | ✅ Active | Data Entry, Research, List building |

---

## 🚀 Prospective Clients (Active Onboarding)

- **Penji** — Final interview scheduled next week with CMO (PROJECTS/Prospective)
- **Top Acquisitions (Nick Adasi)** — Paid trial task (Aug 8-10, due Monday Aug 11 EOD UK time) (PROJECTS/Prospective)

---

## 🔧 System & Automation

### **ECO (Claude Code Chief of Staff)**
- 5-agent system: CLIENTS, COMMS, OPS, METRICS, STRATEGY
- Guide: `TEMPLATES/01 Automation Daily Routine/ECO - Chief of Staff Guide.md`; supporting files in `RESOURCES/ECO System/`
- Activation: Say "good morning", "done for today", or "monthly income & expense review" in Claude Code
- Note: most of the original scheduled automations are currently disabled — see `ARCHIVE - Inactive Automations/README.md` for current status

### **Smartlead ↔ Pipedrive Automation**
- Current live workflow (MCP-connector based): `RESOURCES/Workflows/Smartlead-Pipedrive-Automation-Workflow.md`
- Original Python sync engine (fallback/reference): `PROJECTS/Active/smartlead-pipedrive-automation/`, docs in `RESOURCES/Workflows/Smartlead-Pipedrive-Python-Build (Archived).md`
- Run logs: `RESOURCES/Workflows/automation_logs/`

### **Triggers You Can Use**
- `good morning` — Generate morning briefing (2pm PHT, manual trigger)
- `done for today` — Evening wrap-up with pending items
- `monthly income & expense review` — Full financial summary

### **Automated Alerts**
- 15 minutes before client sessions (configured per client timezone)
- Email checks every 6 hours
- No automatic goal warnings (manual only)

### **iMessage Notifications**
- **2pm PHT:** Morning briefing (calendar, emails, tasks, concerns)
- **5am PHT:** Evening wrap-up (accomplishments, hours, pending)
- Sent to: eikkomaeybanez@icloud.com & 09162013432

---

## ⚙️ Connected Tools & APIs

**Working (live data pulling):**
- ✅ Smartlead (Yoni prospects)
- ✅ Pipedrive (Yoni CRM)
- ✅ TimeDoctors (Yoni time tracking)
- ✅ Gmail (email)
- ✅ Google Calendar (scheduling)
- ✅ Google Tasks (task management)
- ✅ Google Drive (file storage)
- ✅ Apollo (Chris Drew, Krishna lead gen)

**Manual input only:**
- Hubspot (Chris Caffera)
- Lemlist (Chris Caffera)
- LinkedIn (Chris Caffera)

**Credentials on file:** OAuth client secrets for Albert Scott, Fractio, Personal, and Satlas Google accounts — see `RESOURCES/Tools & API Details/OAuth Credentials/`.

---

## 📝 How to Use This System

### **Daily Workflow**
1. **Morning (2pm PHT):** Run `good morning` for automated briefing
2. **Throughout day:** Log work in app or edit end-of-day files
3. **Evening (5am PHT):** Get iMessage wrap-up with summary
4. **End of day:** Run `done for today` for comprehensive recap

### **Weekly Tasks**
- Monday 10am: Chris Caffera meeting
- Monitor campaign health in Plusvibe daily
- Check email every 6 hours

### **Monthly Tasks**
- Run `monthly income & expense review`
- Financial summary and expense tracking
- Analyze metrics and performance

---

## 📋 File Organization Summary

```
Client-Management-System/
├── README.md (you are here)
├── ABOUT ME/
│   ├── CLAUDE.md
│   └── GETTING STARTED.md
├── CLIENT PROFILES/
│   ├── Important info.md
│   ├── Chris Caffera - Profile.md
│   ├── Chris Drew - Profile (Satlas).md
│   ├── Yoni - Profile (Albert Scott).md
│   ├── Krishna - Profile.md
│   └── Chris Soriano - Profile.md
├── SKILLS/ (empty)
├── PROJECTS/
│   ├── Active/
│   │   ├── MASTER-TASK-LIST-ACTIVE.md
│   │   ├── ACTION-PLAN-UNCATEGORIZED-MESSAGES.md
│   │   ├── YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md
│   │   ├── LATEST-COMPLETED-WORK.md
│   │   └── smartlead-pipedrive-automation/ (git repo)
│   └── Prospective/
│       └── NEW CLIENTS - ONBOARDING PIPELINE.md
├── TEMPLATES/
│   ├── 01 Automation Daily Routine/
│   ├── 02 Plugin Client Templates/
│   └── 03 App Dashboard & Work Logger/
├── OUTPUT/
│   ├── End-of-Day Reports/
│   ├── Campaign Tracking/ (16 files)
│   ├── Monthly Reports/
│   └── Data & Metrics/
└── RESOURCES/
    ├── ECO System/ (11 files)
    ├── Tools & API Details/
    │   └── OAuth Credentials/ (4 JSON secrets)
    ├── Workflows/ (6 files + automation_logs/)
    └── Documentation/ (empty)

ARCHIVE - Inactive Automations/ (root level — stale automation/status docs kept for reference, see its README.md)
```

---

## ✅ System Status

- **Folder structure:** 🟢 Fully organized — root folder cleaned of loose files; client profiles and overlapping automation docs merged/deduplicated Aug 13
- **ECO setup:** 🟡 Framework configured (5 agents, guide in place), but most scheduled automations (morning briefing, Lemwarm monitor, PlusVibe monitor) are **disabled** — only `daily-eod-sync` is currently running. See `ARCHIVE - Inactive Automations/README.md`.
- **Client profiles:** 🟢 One consolidated file per client (merged quick-reference + detailed versions)
- **Automation:** 🟡 smartlead-pipedrive sync codebase exists in `PROJECTS/Active/`; current live process is manual/MCP-connector driven (see Smartlead-Pipedrive-Automation-Workflow.md), not the Python cron/webhook system
- **API connections:** 🟡 Some tools connected (Gmail, Calendar, Drive, Smartlead, Pipedrive); several others (Apollo, Notion, Slack, etc.) still need OAuth authorization
- **Prospective clients:** 🟢 Penji & Top Acquisitions onboarding

---

## 📞 Quick Reference

**Need to check:**
- Client rate/hours? → `CLIENT PROFILES/Important info.md`
- Campaign health? → `OUTPUT/Campaign Tracking/Plusvibe Mailbox Health - Daily Monitor.md`
- Today's schedule? → Run `good morning` in Claude Code
- Active tasks? → `PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md`
- Monthly finances? → `OUTPUT/Monthly Reports/Monthly Income & Expense Review.md`
- Set up a tool? → `RESOURCES/Tools & API Details/`

---

**Next step:** Open `ABOUT ME/CLAUDE.md` or run `good morning` in Claude Code.
