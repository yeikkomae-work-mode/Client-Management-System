# Eikko's Client Management System

**Organized workspace for managing active, trial, and prospective clients, a Claude Code agent system (10 specialists behind a chief-of-staff orchestrator), automation, campaigns, and personal business operations.**

Last updated: Aug 15, 2026 | Status: 🟢 Organized — agent system rebuilt, Fathom meeting sync live, PRD-first build discipline + unattended builder pipeline added

---

## 📂 Folder Structure

### **ABOUT ME**
Your personal profile and system overview.
- `CLAUDE.md` — System overview & working rules
- `GETTING STARTED.md` — Quick-start guide
- `Operating Instructions.md` — Added Aug 15, updated same day for the "Global instructions" field specifically. Paste into Claude Settings → Cowork → **Global instructions** (account-level, applies to every session). Opens with a session-bootstrap step (auto-connect this folder, read `CLAUDE.md`/`README.md` unprompted, cross-check Notion VA Command Center) so new sessions stop losing context — then covers PRD-first, pushback/no-yes-man, aggressive note-taking, reversibility.

Root-level `CLAUDE.md` is a lighter agent quick-reference that Claude Code reads automatically each session — see **Agent System** below.

### **CLIENT PROFILES**
One consolidated profile per client (10 files).
- `Important info.md` — Master reference (rates, contact, payment info)
- `Chris Caffera - Profile.md` — Personal Assistant ($7/hr, 20h/week, 2pm-11pm)
- `Chris Drew - Profile (Satlas).md` — Satlas Lead Gen, full engagement history, infrastructure & campaign playbook ($200 AUD/mo, 1pm-4pm)
- `Yoni - Profile (Albert Scott).md` — Albert Scott Outreach, full workflow reference incl. key people, tools, reply taxonomy, copy rules ($5/hr, 5h/day, 9pm-5am PHT)
- `Krishna - Profile.md` — Free Lead Gen (3h/week, flexible)
- `Chris Soriano - Profile.md` — Data Entry (as-needed, sporadic)
- `Penji - Profile.md` + `Penji - Agency Advisor Quick Reference.md` — Signed Aug 10, role confirmed Aug 13 (Agency Advisor — Outbound Outreach Specialist)
- `Cüneyt - Profile (Starfix).md` — Trial client (20h @ $7/hr), started Aug 13
- `Edward Lehner - Profile.md` — Prospective client, Talk-Through / Focus Accountability Partner role (Upwork)

### **SKILLS**
Your skills documentation and competencies (empty — ready for expansion).

### **PROJECTS**
Active and prospective projects organized by status.
- **Active/** — Live task lists:
  - `MASTER-TASK-LIST-CROSS-CLIENT.md` — the genuine cross-client rollup: every client's open items in one place, each citing its source file
  - `YONI-TASK-LIST-ACTIVE.md` — Yoni / Albert Scott operations task list (renamed from `MASTER-TASK-LIST-ACTIVE.md` on 2026-08-25 — it was never cross-client)
  - `CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG10.md` — Chris Caffera's weekly task list
  - `ACTION-PLAN-UNCATEGORIZED-MESSAGES.md` / `YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md` — Message triage tracking
  - `LATEST-COMPLETED-WORK.md` — Most recent completed work summary
  - `Penji - Agency Outreach Automation Workflow.md` — Phased automation design for Penji's sourcing→enrichment→outreach→CRM pipeline
- **Prospective/** — `NEW CLIENTS - ONBOARDING PIPELINE.md`, tracking Cüneyt's trial and the now-closed Top Acquisitions opportunity
- **Pending/ · In-Progress/ · Done/ · Failed/** — Added Aug 15. Autonomous builder pipeline: drop an approved PRD in `Pending/`, a scheduled task builds it unattended and files the result in `Done/` (or `Failed/` with a blocker note). See **Builder Pipeline** below and `PROJECTS/README - Builder Pipeline.md`.

### **TEMPLATES**
Reusable workflows and automation setup.
- **01 Automation Daily Routine/** — ECO system files, work logs, briefing prompts, `ECO - Chief of Staff Guide.md` (merged reference)
- **02 Plugin Client Templates/** — Checklists, meeting templates, campaign trackers
- **03 App Dashboard & Work Logger/** — Browser-based work logging app
- `PRD Template.md` — Added Aug 15. Used for any nontrivial build (new agent, automation, client system, structural change) — problem, success criteria, scope, plan, sign-off, before building.

### **OUTPUT**
Reports, data, metrics, and end-of-day summaries from your work.
- **End-of-Day Reports/** — Daily logs, one per client/prospect (10 files): Chris Caffera, Chris Drew, Yoni, Krishna, Chris Soriano, Penji, Cüneyt, Edward Lehner, Top Acquisitions (closed)
- **Meetings/** — One folder per client, one file per meeting, sourced live from Fathom (connected Aug 13). Each file has the meeting purpose, key takeaways, action items with owner + timestamp links, and either the full transcript or a note that it's available on request. Currently: Yoni (6), Chris Caffera (2), Cüneyt (1, trial agreement), Edward Lehner (2, hiring call + first session). See **Meeting Sync (Fathom)** below.
- **Campaign Tracking/** — Live campaign metrics & logs (24 files), including Satlas infrastructure & Plusvibe health, Peru/Philippines/US Silver Chain campaigns (Krishna), Capital Financing (Chris Drew), Starfix campaign tracking & sequences (Cüneyt), Penji's agency email sequence, and Chris Caffera's Lemlist metrics + engaged-lead call list
- **Monthly Reports/** — Monthly financial summaries & expense tracking
- **Data & Metrics/** — `Salary & Income Tracking.md` (revenue across all clients)

### **RESOURCES**
System files, tool documentation, and reference materials.
- **ECO System/** — Legacy Chief of Staff config, session logs & sync verification (11 files, several superseded — see **Agent System** below for what's actually current)
- **Tools & API Details/** — `Connected Tools Status.md`, `tools_api_details.md`, `google_accounts_details.md`, plus a Gmail multi-account client (custom OAuth script for the 3 non-primary Gmail accounts)
  - **OAuth Credentials/** — Google OAuth client secrets + tokens (Albert Scott, Fractio, Personal, Satlas) — ⚠️ sensitive, do not share
- **Workflows/** — Sync system guide, Smartlead↔Pipedrive automation docs (current + archived Python build), Yoni's live automation runbook, `automation_logs/`
- **Documentation/** — Reference guides, templates, how-tos (empty — ready for expansion)

### **ARCHIVE - Inactive Automations** (root level)
Stale automation/status docs kept for reference, not deleted. See its own `README.md` for exactly what's disabled and why — short version: only `daily-eod-sync` is still running; the original morning-briefing, Lemwarm monitor, and PlusVibe monitor tasks have been off since ~Aug 6.

### **.claude/agents/** (root level — the current agent system)
10 Claude Code specialist subagents in a front-office/back-office split, built Aug 13 replacing the earlier 5-agent ECO framework, plus the `chief-of-staff` orchestrator added Aug 25 as the front door to them. See **Agent System** below.

### **Top Acquisitions/** (root level)
Leftover sourcing file (`top-acquisitions-hvac-sourcing.md`) from the closed trial — candidate for archiving alongside the ECO cleanup.

---

## 🤖 Agent System (current — 10 specialists built Aug 13, orchestrator added Aug 25)

Sessions in this folder open in **chief-of-staff mode**: describe the goal and it routes, sequences, checks the result, and checkpoints what happened. Claude Code also auto-routes to a specialist when the match is obvious, and you can always call one directly ("Use the billing-auditor agent for this month's income review"). Full reference: `.claude/agents/README.md`. Quick list: `/agent-manager`.

**Orchestrator (above the split, not one of the ten):**
`chief-of-staff` — routes to the right specialist, owns multi-step outcomes, holds the authority rules and the session-memory protocol. `/cos`

**Front-office (client-facing — drafts only, nothing sends without your yes):**
`inbox-triage` · `copywriter` · `lead-prospector` · `reply-handler` · `market-scout`

**Back-office (internal ops):**
`project-manager` · `billing-auditor` · `onboarding-guide` · `file-organizer` · `meeting-summarizer`

**Shared reference:** `.claude/agents/_shared/connector-status.md` — single source of truth every agent reads before claiming a tool is live. Twin copy in Notion: 🎛️ VA Command Center.

**Slash commands:** `/cos` (chief of staff — what's open across clients, or a routing plan for a goal) · `/agent-manager` (list/inspect agents) · `/eod-sync <client>` (set up a recurring per-client EOD automation with Notion sync)

---

## 🎥 Meeting Sync (Fathom, connected Aug 13)

Every meeting you record in Fathom now gets pulled, matched to a client, and filed automatically by the `meeting-summarizer` agent.

**Where it goes:** `OUTPUT/Meetings/<Client Name>/YYYY-MM-DD - <title>.md` — separate from End-of-Day Reports, which stays a running daily log. Meeting files are the detailed backing record.

**What's in each file:** meeting purpose, key takeaways, topics, full action-item list with owner + clickable timestamp link back into the recording, and either the full transcript (for foundational meetings — hiring/terms calls, trial agreements, first sessions) or a note that it's available on request (for routine/recurring calls, to keep files lean).

**Client matching:** done by attendee/company name against `CLIENT PROFILES/*.md`. If a meeting doesn't clearly match anyone, you'll be asked rather than have it filed on a guess — this already happened once (an EDU12/Brightspace call turned out to be Edward Lehner's actual work).

**Current state:** 11 meetings backfilled at connection time — 6 Yoni, 2 Chris Caffera, 1 Cüneyt (trial agreement), 2 Edward Lehner (hiring + first session). Going forward, new Fathom recordings should be picked up each time you ask for a briefing/update, or you can say "check Fathom for new meetings" any time.

**Note:** the Cüneyt trial call was actually with someone named **Junaid**, not Cüneyt directly — worth confirming with the client profile whether these are the same person or Junaid is a separate contact at Starfix.

---

## 🏗️ Builder Pipeline (added Aug 15)

Drop a signed-off PRD, wake up to a finished build — adapted from Tina Huang's "autonomous builder" pattern.

**How it works:** write a PRD using `TEMPLATES/PRD Template.md`, check the sign-off box, drop it in `PROJECTS/Pending/`. The scheduled task `project-builder-check` (every 3 hours) picks it up, moves it to `In-Progress/`, builds exactly what's scoped, and files it in `Done/` with a build log appended — or in `Failed/` with a clear blocker note if it hits something ambiguous, destructive, or missing.

**Ground rules:** only approved PRDs get built. Nothing outside the PRD's stated scope gets touched. Destructive/irreversible steps always get flagged to `Failed/` for a real go-ahead rather than run unattended. Full detail: `PROJECTS/README - Builder Pipeline.md`.

**Related:** `ABOUT ME/Operating Instructions.md` — paste into Claude Settings → Cowork → **Global instructions** for account-wide PRD-first / pushback / reversibility rules, and the session-bootstrap fix that stops new sessions from losing this folder's context.

---

## 🎯 Quick Navigation

### **Starting Your Day**
1. Open: `ABOUT ME/CLAUDE.md` (system overview)
2. Open: `CLIENT PROFILES/Important info.md` (quick client reference)
3. Run in Claude Code → `good morning` (auto-generates briefing) — note: not on a live schedule, manual trigger only
4. Check: `TEMPLATES/03 App Dashboard & Work Logger/app.html` (open work logger)

### **Logging Work**
- Use the browser app: `TEMPLATES/03 App Dashboard & Work Logger/app.html`
- Or edit directly: `OUTPUT/End-of-Day Reports/[Client] - End of Day Log.md`
- Or run `/eod-sync <client>` to set up a recurring automated version

### **Checking Campaigns**
- Open: `OUTPUT/Campaign Tracking/[Campaign] - Campaign Log.md`
- Monitor: `OUTPUT/Campaign Tracking/Plusvibe Mailbox Health - Daily Monitor.md`

### **Checking Active Tasks**
- Everything, all clients: `PROJECTS/Active/MASTER-TASK-LIST-CROSS-CLIENT.md`
- Yoni / Albert Scott only: `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md`

### **Monthly Financial Review**
- Open: `OUTPUT/Monthly Reports/Monthly Income & Expense Review.md`

### **Using the Agent System**
- List all agents: `/agent-manager`
- Set up per-client EOD automation: `/eod-sync <client-name>`
- Full guide: `.claude/agents/README.md`

---

## 📊 Current Clients at a Glance

| Client | Rate | Hours | Status | Focus |
|--------|------|-------|--------|-------|
| Yoni (Albert Scott) | $5/hr | 5h/day (9pm-5am PHT) | ✅ Active | Outreach, Smartlead, Pipedrive |
| Chris Caffera | $7/hr | 20h/week (2pm-11pm) | ✅ Active | Personal Assistant, ICP, Apollo, Lemlist |
| Chris Drew (Satlas) | $200 AUD/mo | Variable (1pm-4pm) | ✅ Active | Lead Gen, Plusvibe, Capital Financing |
| Krishna | Free | 3h/week | ✅ Active | Lead Gen, Apollo, Silver Chain campaigns |
| Chris Soriano | $7/hr | As-needed | ✅ Active | Data Entry, Research, List building |
| Penji | TBD | TBD | ✅ Signed (Aug 10) | Agency Advisor — Outbound Outreach |
| Cüneyt (Starfix) | $7/hr | 20h trial | 🟡 Trial (started Aug 13) | Cold Email & Lead Gen, Deliverability |
| Edward Lehner | $5/hr billed | 5h/week | 🟠 Prospective | Talk-Through / Focus Accountability Partner |
| Top Acquisitions | — | — | 🔴 Closed (Aug 13) | Not selected |

---

## 🔧 System & Automation

### **Scheduled Automations — what's actually running**
Checked directly against the scheduled-tasks system, Aug 13:

| Task | Status |
|---|---|
| `daily-eod-sync` | ✅ **Active** — the only one currently running |
| `eco-morning-email-briefing` | ⏸ Disabled since ~Aug 6 |
| `lemwarm-alex-daily-monitor` | ⏸ Disabled since ~Aug 6 |
| `plusvibe-daily-mailbox-monitor` | ⏸ Disabled since ~Aug 6 |

Full detail and reactivation notes: `ARCHIVE - Inactive Automations/README.md`

### **Smartlead ↔ Pipedrive Automation**
- Current live workflow (MCP-connector based): `RESOURCES/Workflows/Smartlead-Pipedrive-Automation-Workflow.md`
- Original Python sync engine (fallback/reference, archived): `RESOURCES/Workflows/Smartlead-Pipedrive-Python-Build (Archived).md`
- Run logs: `RESOURCES/Workflows/automation_logs/`

### **Triggers You Can Use**
- `good morning` — Manual-trigger morning briefing
- `done for today` — Evening wrap-up with pending items
- `monthly income & expense review` — Full financial summary
- `/cos` — Chief of Staff: what's open across clients, or the routing plan for a goal you name
- `/agent-manager` — List/inspect the agents
- `/eod-sync <client>` — Set up recurring automated EOD sync for a client

---

## ⚙️ Connector Status (verified Aug 14 — see `.claude/agents/_shared/connector-status.md` for full detail)

**✅ Connected:**
Apollo (raw API key, Satlas/Chris Drew + separate key for Krishna) · Pipedrive (Yoni/Albert Scott) · Smartlead (Albert Scott account only) · Gmail ×4 (yeikkomae@gmail.com native; Satlas, Albert Scott, and Fractio via custom multi-account script, read+draft only) · Notion (eikko mae ybanez's Space) · PlusVibe (Chris Drew/Satlas, raw API key) · Instantly + Hostinger (Cüneyt/Starfix — separate account from Satlas's, don't confuse the two) · **Fathom** (live meeting sync — see **Meeting Sync** above)

**🟡 Needs authorizing / incomplete:**
HubSpot · Slack · Fireflies (no longer needed now that Fathom is live) · Porkbun (key present, missing paired secret)

**⚫ Dead / no connector (manual or browser-only):**
Instantly (Satlas — deprecated, migrated off) · Zapmail (dead key) · InboxKit (inconclusive, likely wrong path) · MillionVerifier (2FA, can't automate) · Lemlist (browser-only) · LinkedIn (no API path)

**Note:** Satlas team's own "Cold Email" Notion hub is a different workspace from the one connected here — still needs separate access.

---

## 📝 How to Use This System

### **Daily Workflow**
1. **Morning:** Run `good morning` for a manual briefing, or check your calendar directly
2. **Throughout day:** Log work in the app or edit end-of-day files — or let `/eod-sync` handle it per client
3. **End of day:** Run `done for today`, or rely on `daily-eod-sync` (the one automation still live)

### **Weekly Tasks**
- Monitor campaign health in Plusvibe / Starfix Instantly
- Check in on Cüneyt's trial progress (DKIM fix, upfront payment)
- Chase down connector gaps (HubSpot, Slack, Fireflies, Porkbun) when convenient

### **Monthly Tasks**
- Run `monthly income & expense review`

---

## 📋 File Organization Summary

```
Client-Management-System/
├── README.md (you are here)
├── CLAUDE.md (root — agent quick-reference, read by Claude Code each session)
├── .claude/
│   ├── agents/ (chief-of-staff.md + 10 specialist definitions + README + _shared/connector-status.md)
│   └── commands/ (cos.md, agent-manager.md, eod-sync.md)
├── ABOUT ME/
│   ├── CLAUDE.md
│   └── GETTING STARTED.md
├── CLIENT PROFILES/ (10 files — 9 clients/prospects + Important info.md)
├── SKILLS/ (empty)
├── PROJECTS/
│   ├── Active/ (6 files)
│   └── Prospective/
│       └── NEW CLIENTS - ONBOARDING PIPELINE.md
├── TEMPLATES/
│   ├── 01 Automation Daily Routine/
│   ├── 02 Plugin Client Templates/
│   └── 03 App Dashboard & Work Logger/
├── OUTPUT/
│   ├── End-of-Day Reports/ (10 files)
│   ├── Meetings/ (11 files across 4 client folders — live from Fathom)
│   ├── Campaign Tracking/ (24 files, incl. Capital Financing/ subfolder)
│   ├── Monthly Reports/
│   └── Data & Metrics/
├── RESOURCES/
│   ├── ECO System/ (11 files — legacy, see ARCHIVE for current status)
│   ├── Tools & API Details/ (incl. Gmail Multi-Account Client/, OAuth Credentials/)
│   ├── Workflows/ (7 files + automation_logs/)
│   └── Documentation/ (empty)
├── ARCHIVE - Inactive Automations/ (disabled automation docs, see its README.md)
└── Top Acquisitions/ (leftover sourcing file from closed trial)
```

---

## ✅ System Status

- **Folder structure:** 🟢 Organized — client profiles consolidated, stale automation docs archived (not deleted) Aug 13
- **Agent system:** 🟢 Rebuilt Aug 13 — 10 specialists in a front/back-office split replacing the 5-agent ECO framework, with a single connector-status source of truth. Aug 25: `chief-of-staff` orchestrator added as the front door; routing lives in that one file, everything else points at it
- **Automation:** 🟡 Only `daily-eod-sync` is actually running; morning briefing, Lemwarm monitor, PlusVibe monitor are disabled (re-enable via the `schedule` skill if needed — check for staleness first)
- **Client profiles:** 🟢 One consolidated file per client/prospect, 9 total
- **Connector status:** 🟡 Core lead-gen/CRM tools + Fathom connected; HubSpot, Slack, Fireflies, Porkbun need auth; several tools (Zapmail, Lemlist, LinkedIn, etc.) have no viable connector and stay manual
- **Client roster:** 🟢 6 active, 1 signed (Penji), 1 trial (Cüneyt), 1 prospective (Edward Lehner), 1 closed (Top Acquisitions)
- **Meeting sync:** 🟢 Fathom connected Aug 13 — 11 meetings backfilled into `OUTPUT/Meetings/`, new ones filed automatically going forward
- **Build discipline:** 🟢 Added Aug 15 — Operating Instructions doc (paste into Cowork Settings), PRD-first habit for nontrivial builds, and an unattended builder pipeline (`PROJECTS/Pending/` → `project-builder-check` every 3h → `Done/`/`Failed/`)

---

## 📞 Quick Reference

**Need to check:**
- Client rate/hours? → `CLIENT PROFILES/Important info.md`
- Which agent handles X? → `/agent-manager` or `.claude/agents/README.md`
- Is a tool actually connected? → `.claude/agents/_shared/connector-status.md`
- Campaign health? → `OUTPUT/Campaign Tracking/Plusvibe Mailbox Health - Daily Monitor.md`
- Active tasks, all clients? → `PROJECTS/Active/MASTER-TASK-LIST-CROSS-CLIENT.md`
- Active tasks, Yoni only? → `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md`
- Monthly finances? → `OUTPUT/Monthly Reports/Monthly Income & Expense Review.md`
- Which automations are actually live? → `ARCHIVE - Inactive Automations/README.md`

---

**Next step:** Open `ABOUT ME/CLAUDE.md`, run `/agent-manager` to see the current agent team, or run `good morning` in Claude Code.
