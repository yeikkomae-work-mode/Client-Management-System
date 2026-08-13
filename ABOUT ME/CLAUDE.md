# Client Management System — CLAUDE.md

**What this is:** A three-part personal client management system (automation, plugin, app) for managing 6 active clients + 1 prospective with centralized task tracking, communication monitoring, campaign metrics, and daily recap generation.

**Desired outcome:** A single workspace where Eikko can see all client work, yesterday's recap, upcoming meetings, task deadlines, and log daily progress without information scattered across WhatsApp, email, Slack, and multiple CRMs.

---

## Key Context (Read This Every Session)

- **User:** Eikko Ybanez (yeikkomae@gmail.com, eikko@satlas.com.au)
- **7 Active Clients:** Chris Caffera (FT, Fractio, personal assistant), Chris Drew (FT, Satlas lead gen), Yoni (FT, Albert Scott outreach), Krishna (PT, 3hrs/wk lead gen), Chris Soriano (PT, as-needed data entry/research), Penji (signed Aug 10, Agency Advisor — hours/rate TBD), Cüneyt (trial, Starfix cold email/deliverability + lead gen, 20hrs @ $7/hr, signed Aug 13)
- **1 Prospective:** Edward Lehner (talk-through/focus accountability partner, $5/hr — Upwork offer pending, expires Aug 19, 2026)
- **1 Closed (not selected):** Top Acquisitions / Nick Adasi (Aug 13, 2026) — open to reconsidering if a second role opens, no active follow-up
- **Main blindspots:** WhatsApp pile-up, calendar conflicts, task deadlines, campaign metrics scattered across tools
- **Critical feature:** Yesterday's recap on app open (tasks done, missed messages, campaign metrics, meeting summaries)
- **Work logging:** New feature needed — "Working on X → Done: accomplished Y" replaces manual time tracking
- **Timezone:** PHT (Philippines) — Note: Yoni's hours are 9pm-5am PHT
- **Campaign Monitoring (Chris Drew - Satlas):** 
  - Active monitoring of Zapmail (10 domains, 30 mailboxes), InboxKit (15 domains total: 10 active with 30 mailboxes + 5 backup), and Plusvibe
  - Domain portfolio: 25 total domains managed via Porkbun (Batch 1: May 2026, Batch 2: July 2026)
  - Infrastructure: 60 total mailboxes, 180+ email accounts across platforms
  - See: DOMAIN_INVENTORY.md for complete breakdown

---

## Folder Map

```
Client-Management-System/
├── Pre-build context.md                    # System design & planning
├── Important info.md                       # Client details, rates, contact info
├── CLAUDE.md                               # This file (project overview)
├── End-of-Day Reports/                     # Daily work logs per client
│   ├── Chris Caffera - End of Day Log.md
│   ├── Chris Drew - End of Day Log.md
│   ├── Yoni - End of Day Log.md
│   ├── Krishna - End of Day Log.md
│   ├── Chris Soriano - End of Day Log.md
│   └── README.md
├── ~ATTACHMENTS~/                          # Screenshots, exports, misc files
├── ~ARCHIVE~/                              # Old versions, dead ends
└── Build-out/
    ├── 01 Automation Daily Routine/        # ✓ COMPLETE
    │   ├── Good Morning Prompt.md
    │   ├── Work Logger Prompt.md
    │   ├── Meeting Transcript Processor.md
    │   ├── Manual Metrics Input.md
    │   ├── Connected Tools Status.md
    │   └── How to Use - Daily Workflow.md
    ├── 02 Plugin Client Templates/         # ✓ COMPLETE
    │   ├── Template - Client Onboarding.md
    │   ├── Template - Daily Task Checklist.md
    │   ├── Template - Campaign Metrics.md
    │   ├── Template - Message Check.md
    │   ├── Template - Meeting Summary.md
    │   └── How to Use - Plugin Templates.md
    └── 03 App Dashboard & Work Logger/     # ✓ COMPLETE
        ├── app.html
        ├── How to Use - App.md
        └── Data Schema.md
```

---

## What Each Folder Does

### 01 Automation Daily Routine
**Purpose:** Repeatable daily workflow Eikko runs (or can be triggered) to check all clients, log work, and generate recap.

**Includes:**
- Daily task checklist per client (what to check, in what order)
- Work logger prompt (what Eikko is working on → goal)
- Recap generator (compile yesterday's work from logs + API data)
- Meeting summary processor (transcript → summary + action items)

### 02 Plugin Client Templates
**Purpose:** Reusable templates Eikko can apply to new clients or repeat workflows.

**Includes:**
- Client onboarding template (capture all needed info)
- Daily task template (generic checklist for any client)
- Campaign metrics template (flexible per tool)
- Email/message check template
- Meeting-to-summary workflow

### 03 App Dashboard & Work Logger
**Purpose:** The actual app Eikko uses daily (HTML/data view).

**Includes:**
- Data schema (how client/task/metric data is stored)
- Recap view (yesterday's work, organized by client)
- Current work logger (goal input → accomplishment output)
- Meeting summary view
- Task deadline tracker
- Campaign performance snapshot
- UI/UX specs

---

## Working Rules

- **Logs:** Manual logs written by user OR they can ask Claude to compile them
- **Important info:** Store key facts about clients and projects in `Important info.md`. Check it each session. Add to it when something new comes up.
- **Attachments:** Screenshots, meeting recordings, exports, misc files go in `~ATTACHMENTS~/`
- **Archive:** Old versions, replaced files, dead ends → `~ARCHIVE~/`. Don't delete.
- **Build-out:** Each numbered folder = one sub-system. Do work inside its folder.
- **Separate chats:** Use a separate Claude chat for research or context-condensing. Bring back only what matters.
- **Accuracy matters:** Campaign metrics and meeting summaries are critical; double-check before finalizing.
- **Keep everything in sync, by default:** Whenever work happens for a client — a campaign built/launched, a meeting processed, a task completed or paused — update that client's tracking files in the same turn, without waiting to be asked. This includes: the client's End-of-Day log, `LATEST-COMPLETED-WORK.md`, `Daily-Lead-Summary.md`, `Smartlead-Pipedrive-Sync-Log.md`, `[Client]-Projects-Active.md`, `MASTER-TASK-LIST-ACTIVE.md`, and the live Task Tracker Google Sheet. Treat "update the files" as the default outcome of doing work, not a separate request.
- **Notion VA Command Center is the source of truth Eikko actually looks at — keep it current, not just the local files:** https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b (workspace: "eikko mae ybanez's Space"). It has four parts: Front-Office Agents log, Back-Office Agents log, a Clients database (status/tools/next action per client), and a Connector Status page. Whenever any of these change, update the Notion page in the same turn, don't just update the local markdown and stop:
  - A client's status, rate, or next action changes → update their row in the Clients database.
  - A connector gets authorized, breaks, or gets fixed → update both the Notion Connector Status page AND `.claude/agents/_shared/connector-status.md` (they must always match — the local file is what agents actually read at runtime, the Notion page is what Eikko checks by eye).
  - Any of the 10 agents (`.claude/agents/`) actually completes real work (not a dry run) → log it under the relevant Front-Office or Back-Office section.
  - A prospective client closes (signed or rejected) → update their Clients database row and, if rejected, set Status to "Paused" (no "Closed" option exists in the schema — Paused is the closest fit) with the outcome noted in Next Action.
  - Treat "the Notion page is stale" as a bug to fix immediately when noticed, not a backlog item.

---

## Quick Links & Notes

**Next action:** Review Pre-build context.md. Confirm it's complete. Then start building folder specs.

**Questions waiting on Eikko:**
1. Should the app pull from APIs directly (Hubspot, Pipedrive, PlusVibe) or use manual metric logging?
2. Which platform provides meeting transcripts? (Calendly, Google Meet, Zoom, etc.)
3. Any other workflows or tools we missed?
4. Mobile or desktop-only for the app?

---

**Last updated:** 2026-08-13
