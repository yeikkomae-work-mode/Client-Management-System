# Tech Radar

**Owner:** `cto` agent · **Created:** 2026-08-25 · **Twin copy in Notion:** [📡 Tech Radar](https://app.notion.com/p/3c7811e21c7f81d2814bef36e02b62f4), inside the [🎛️ VA Command Center](https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b). This local file is what the agent reads at runtime; the Notion copy is for reading off-laptop. Update both.

Every tool, technique, or automation Eikko evaluates lands here with a verdict and a reason. **Check this file before evaluating anything** — if it's already here, the prior verdict stands until something specific changes.

This file is **append-only**. Never delete or rewrite a row; supersede it with a new dated row and note what changed.

## Statuses

| Status | Means |
|---|---|
| ✅ **ADOPT** | In use, or should be. Earns its cost, fits the stack, stood up fast, fails loudly if it breaks. |
| 🧪 **TRIAL** | Worth testing under a defined scope. **Must have a review-by date** — a trial without one is a bookmark. |
| ⏸️ **HOLD** | Interesting but not now. Usually fails time-to-value, or the stack isn't ready. Revisit when the named condition changes. |
| ❌ **KILL** | Evaluated and rejected. Recorded so it doesn't get re-litigated in three months. |
| ❓ **UNCLEAR** | In use or installed, but the status isn't independently verified. Not a verdict — a flag that something needs checking. |

## The four criteria (every verdict states all four)

1. **Cost** — monthly cost, and what it displaces. Recurring spend with nothing retired and no revenue line fails. **Confirmed 2026-08-25: every client tool below is client-paid. Eikko's entire business expense base is ₱7,600/mo — Claude ₱7,000 + Apple iCloud ₱600.** The cost column here is a pointer; `cfo` owns the actual spend register.
2. **Stack fit** — does it connect to Apollo / Smartlead / PlusVibe / Instantly / Pipedrive / HubSpot / Notion / Fathom / Zapmail / InboxKit / Apify / Claude Code?
3. **Time-to-value** — standing up inside one weekend, or it's HOLD.
4. **Fragility** — what happens when it breaks, and how would Eikko know? Penalized hardest.

---

## Baseline — the current stack (seeded 2026-08-25)

Statuses below trace to `.claude/agents/_shared/connector-status.md` (last verified 2026-08-25) and the folder itself. Nothing here was independently re-tested during seeding — this is a snapshot of what's *documented*, not a fresh audit.

### Core stack — in production

| Tool | Jurisdiction | Status | Cost | Notes |
|---|---|---|---|---|
| Apollo | Client (Satlas, Krishna) | ✅ ADOPT | — | Raw API key over Bash, not the MCP connector. Chris Caffera's segments have no documented key — **gap**. |
| Smartlead | Client (Albert Scott) | ✅ ADOPT | — | Scoped to Yoni's account only. |
| PlusVibe | Client (Satlas) | ✅ ADOPT | — | Raw API key + workspace_id. ⚠️ The MCP connector points at the *wrong* account — never use it for Satlas. Live fragility trap. |
| Instantly | Client (Starfix) | ✅ ADOPT | — | Separate account from Satlas's. Satlas's own Instantly is ⚫ deprecated, key dead. |
| Pipedrive | Client (Albert Scott) | ✅ ADOPT | — | CRM for Yoni. |
| Notion | Internal | ✅ ADOPT | — | VA Command Center. Satlas team workspace is a separate, unconnected one. |
| Fathom | Internal | ✅ ADOPT | — | Meeting sync live since Aug 13, files into `OUTPUT/Meetings/`. Displaced Fireflies. |
| Gmail ×5 | Internal | ✅ ADOPT | — | 1 native connector + 4 via custom OAuth script. Read + draft only, no send scope. |
| Claude Code + 11 agents | Internal | ✅ ADOPT | **₱7,000/mo — you pay** | The system itself, and 92% of your business expense base. Note: the Notion Finance Tracker row reading `Claude Max Plan - 8000` is wrong per the CFO PRD. |
| Apple iCloud | Internal | ✅ ADOPT | **₱600/mo — you pay** | The other 8% of your business expense base. |
| Porkbun | Client (Satlas) | ✅ ADOPT | domains | Verified 2026-08-22, 25-domain inventory pulled. |
| InboxKit | Client (Satlas) | ✅ ADOPT | ? | Live 2026-08-22, 15 domains / 30 mailboxes. Cost not documented — **gap**. |
| Zapmail | Client (Satlas) | ✅ ADOPT | ? | Reconnected 2026-08-22. Returned health 22.65/100, **0/30 mailboxes warmed** — that's a live problem, not a tooling one. |
| Hostinger | Client (Starfix) | ✅ ADOPT | domains | 3 domain-scoped tokens, never independently tested. |

### Flagged — needs a decision

| Tool | Jurisdiction | Status | Cost | Verdict reasoning |
|---|---|---|---|---|
| Higgsfield | Internal | ⏸️ HOLD | Free plan, **0 credits** | MCP live, read-only tools work, every generate_* call fails. Fails **cost** until a plan is chosen and **stack fit** until there's a real use case — no creative deliverable currently depends on it. Revisit when Eikko names the work it would do. |
| HubSpot | Client | ⏸️ HOLD | — | Connector exists, unauthorized. Fails nothing — just hasn't been needed. Adopt when a client actually runs on HubSpot. |
| Slack | Internal | ⏸️ HOLD | — | Same: exists, unauthorized, no current need. |
| Fireflies | Internal | ❌ KILL | — | Displaced by Fathom (Aug 13). Reopen only if Fathom's transcript quality degrades. |
| Instantly (Satlas) | Client | ❌ KILL | — | Migrated off early Aug; key tested dead 2026-08-13. Do not rewire. |
| MillionVerifier | Client | ✅ ADOPT (manual) | — | Manual 2FA by design, no automation path. Accepted as a manual step, not a gap to fix. |
| Lemlist | Client (Caffera) | ❓ UNCLEAR | ? | Browser-only, no connector. Metrics live in `OUTPUT/Campaign Tracking/`. Is this still in active use? |
| LinkedIn | Client | ⏸️ HOLD | — | No API path. Drafting only — unattended posting gets flagged by LinkedIn. Hard ceiling, not a tooling gap. |
| Asana / ClickUp / Trello | Internal | ❌ KILL | — | Tasks live in markdown + Sheets. Adding a PM tool would displace nothing and add a sync surface. |

### Installed but unrecorded — verify

These appear as live MCP connectors in Cowork sessions but have **no row in `connector-status.md`**. That's drift: either they belong there, or they shouldn't be relied on.

| Tool | Status | Why it's flagged |
|---|---|---|
| Apify | ❓ UNCLEAR | Real scraping capability (incl. YouTube transcripts) but credit-metered and unrecorded. Worth a proper verdict — could remove the manual transcript-paste step. |
| Canva · Miro · Zoom · Google Drive/Calendar · GitHub · Zapier | ❓ UNCLEAR | Present in session, absent from the source of truth. Each needs either a row or a documented "not in use." |

### Automations — verified 2026-08-25 ⚠️

| Item | Status | Reasoning |
|---|---|---|
| `daily-eod-sync` | ❌ **DOES NOT EXIST** | `ARCHIVE - Inactive Automations/README.md` calls it "the only one actually running." The scheduler has zero registered tasks. Your EOD logs have not been syncing. |
| `project-builder-check` (Builder Pipeline) | ❌ **DOES NOT EXIST** | `PROJECTS/README - Builder Pipeline.md` claims every 3 hours. Never ran once — `Pending/`, `In-Progress/`, `Done/`, `Failed/` are all empty. **Do not drop a PRD in `Pending/` expecting a build.** |
| Morning briefing · Lemwarm monitor · PlusVibe monitor | ❌ KILL (already dead) | Disabled ~Aug 6, correctly documented as archived. |

Two status docs currently assert automations that do not exist. That is worse than having none — see `PROJECTS/RECONCILIATION - 2026-08-25 - C-Suite Agent Layer.md`, step 5.

### Skills & capability

| Item | Jurisdiction | Status | Reasoning |
|---|---|---|---|
| Design/frontend skills bundle (`design-taste-frontend`, `emil-design-eng`, `animation-vocabulary`, `apple-design`, `impeccable-anti-slop-catalog`) | Skill | 🧪 TRIAL — **review by 2026-09-30** | Installed 2026-08-18 account-wide. Cost $0, stack fit is Claude Code-native, time-to-value zero. Open question: which client work actually consumes them? If nothing has used them by the review date, they're clutter, not capability. |
| Cold email deliverability (warmup, domain health) | Skill | ✅ ADOPT | Already the core competency. Zapmail's 0/30 warmed reading suggests depth here pays immediately. |

---

## Evaluations

*New entries append below, newest first. Format: date · item · jurisdiction · verdict · the four criteria · review-by if TRIAL.*

<!-- no evaluations yet — the baseline above is a seed, not a set of verdicts -->
