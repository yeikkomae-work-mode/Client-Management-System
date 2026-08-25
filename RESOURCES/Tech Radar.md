# 📡 Tech Radar

**Owner:** `cto` agent · **Created:** 2026-08-25 · **Last updated:** 2026-08-25

Every tool, technique, or automation Eikko evaluates lands here with a verdict and a reason, so nothing gets re-litigated three months later.

**Twin copy in Notion:** [📡 Tech Radar](https://app.notion.com/p/3c7811e21c7f81d2814bef36e02b62f4), inside the [🎛️ VA Command Center](https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b). **This local file is what `cto` reads at runtime**; the Notion page is for reading off-laptop. Update both when a verdict changes.

> **Recovery note, 2026-08-25.** This file was rebuilt from its Notion twin. The original build (commit `eb89532` on branch `claude/cto-agent-and-csuite-reconciliation`) never reached GitHub — that session's shell couldn't authenticate, and the branch and commit do not exist in this repo or on the remote. The Notion writes from that session *did* land, so the content below is the CTO build's real output, not a reconstruction from memory. Anything that existed only in the lost commit is gone.

## The cost/radar boundary — read this before adding a row

This file answers **"should this exist at all?"** — adopt, trial, hold, kill. It does **not** hold cost figures.

| Question | Owner | Lives in |
|---|---|---|
| Cost, who pays, renewal date, lapse risk | **`cfo`** | Notion Tools & Subscriptions + `OUTPUT/Monthly Reports/Tools & Subscriptions Register.md` |
| Should this exist at all — adopt/trial/hold/kill | **`cto`** | This file |

The **Cost** criterion below is a *pointer* to CFO's register, not a second number. When a verdict needs a cost, read it from the register and cite it — never restate it here as a figure this file owns, and never let the two drift. CFO's register carries a `Radar verdict` column that reads from this file. **Neither agent writes the other's field.**

## Statuses

| Status | Means |
|---|---|
| ✅ ADOPT | In use, or should be. Earns its cost, fits the stack, stood up fast, fails loudly. |
| 🧪 TRIAL | Worth testing under a defined scope. **Must have a review-by date.** |
| ⏸️ HOLD | Interesting, not now. Revisit when the named condition changes. |
| ❌ KILL | Evaluated and rejected. Recorded so it stays rejected. |
| ❓ UNCLEAR | In use but not independently verified. A flag, not a verdict. |

## The four criteria

Every verdict states all four — never a bare verdict, never one without numbers.

1. **Cost** — monthly cost, and what it displaces. Recurring spend with nothing retired fails. *(Read the figure from CFO's register; cite, don't restate.)*
2. **Stack fit** — does it connect to Apollo / Smartlead / PlusVibe / Instantly / Pipedrive / HubSpot / Notion / Fathom / Zapmail / InboxKit / Apify / Claude Code?
3. **Time-to-value** — standing up inside one weekend, or it's HOLD.
4. **Fragility** — what breaks, and how would Eikko know? Penalized hardest.

---

## Baseline — current stack (seeded 2026-08-25)

Traces to `.claude/agents/_shared/connector-status.md`. Nothing was independently re-tested during seeding — this is what's *documented*, not a fresh audit.

### In production

| Tool | Jurisdiction | Status | Notes |
|---|---|---|---|
| Apollo | Client (Satlas, Krishna) | ✅ ADOPT | Raw API key, not MCP. Chris Caffera has no documented key — gap. |
| Smartlead | Client (Albert Scott) | ✅ ADOPT | Yoni's account only. |
| PlusVibe | Client (Satlas) | ✅ ADOPT | ⚠️ MCP connector points at the wrong account — never use it for Satlas. |
| Instantly | Client (Starfix) | ✅ ADOPT | Separate account from Satlas's dead one. |
| Pipedrive | Client (Albert Scott) | ✅ ADOPT | CRM for Yoni. |
| Notion | Internal | ✅ ADOPT | This workspace. Satlas team workspace still unconnected. |
| Fathom | Internal | ✅ ADOPT | Live since Aug 13. Displaced Fireflies. |
| Gmail ×5 | Internal | ✅ ADOPT | 1 native + 4 custom OAuth. Read + draft only. |
| Claude Code + 13 agents | Internal | ✅ ADOPT | The system itself. *(Was "11 agents" at seeding; roster reconciled to 13 on 2026-08-25 — see `.claude/agents/README.md`.)* |
| Porkbun | Client (Satlas) | ✅ ADOPT | Verified 2026-08-22, 25 domains. |
| InboxKit | Client (Satlas) | ✅ ADOPT | Live 2026-08-22. Cost not documented — gap, now tracked in CFO's register. |
| Zapmail | Client (Satlas) | ✅ ADOPT | Health 22.65/100, **0/30 mailboxes warmed** — a live problem, not a tooling one. |
| Hostinger | Client (Starfix) | ✅ ADOPT | 3 tokens, never independently tested. |

### Needs a decision

| Tool | Status | Reasoning |
|---|---|---|
| Higgsfield | ⏸️ HOLD | MCP live but free plan, **0 credits** — every generate call fails. Fails cost until a plan is chosen and stack fit until there's a real use case. Revisit when Eikko names the work it would do. |
| HubSpot | ⏸️ HOLD | Connector exists, unauthorized. Adopt when a client actually runs on it. |
| Slack | ⏸️ HOLD | Exists, unauthorized, no current need. |
| Fireflies | ❌ KILL | Displaced by Fathom. Reopen only if transcript quality degrades. |
| Instantly (Satlas) | ❌ KILL | Migrated off; key dead 2026-08-13. Do not rewire. |
| MillionVerifier | ✅ ADOPT (manual) | Manual 2FA by design. Accepted as a manual step, not a gap. |
| Lemlist | ❓ UNCLEAR | Browser-only. Still in active use for Caffera? |
| LinkedIn | ⏸️ HOLD | No API. Drafting only — unattended posting gets flagged. Hard ceiling. |
| Asana / ClickUp / Trello | ❌ KILL | Tasks live in markdown + Sheets. Would displace nothing, add a sync surface. |

### Installed but unrecorded — verify

These show as live MCP connectors in Cowork sessions but have **no row in Connector Status**. That's drift.

| Tool | Status | Why flagged |
|---|---|---|
| Apify | ❓ UNCLEAR | Real scraping capability including YouTube transcripts — could remove the manual paste step. Credit-metered, unrecorded. Deserves a proper verdict. |
| Canva · Miro · Zoom · Google Drive/Calendar · GitHub · Zapier | ❓ UNCLEAR | Present in session, absent from the source of truth. Each needs a row or a documented "not in use." |

### Skills & capability

| Item | Status | Reasoning |
|---|---|---|
| Design/frontend skills bundle (5 skills, installed 2026-08-18) | 🧪 TRIAL — **review by 2026-09-30** | Cost $0, Claude Code-native, zero setup. Open question: which client work actually consumes them? Nothing by the review date means clutter, not capability. |
| Cold email deliverability depth | ✅ ADOPT | Already the core competency. Zapmail's 0/30 warmed reading says depth here pays immediately. |

---

## Evaluations

*New verdicts append below, newest first.*

### 2026-08-25 — Scheduled automations (`daily-eod-sync`, `project-builder-check`) → ❌ KILL

- **Cost:** $0 either way.
- **Stack fit:** n/a — the question was whether they existed at all.
- **Time-to-value:** n/a.
- **Fragility:** **This is the entire verdict.** Both were documented as running. Neither existed. `ARCHIVE - Inactive Automations/README.md` claimed `daily-eod-sync` was "the only one actually running"; `PROJECTS/README - Builder Pipeline.md` claimed `project-builder-check` ran every 3 hours. Verified live against the scheduled-task system on 2026-08-25: **neither task exists, and `PROJECTS/Pending|In-Progress|Done|Failed` were never even created.** An unattended automation that silently doesn't run is worse than no automation — it produces false confidence in a status page.

**Decision (Eikko, 2026-08-25):** delete both doc sets rather than rebuild. Everything runs interactively. See `OUTPUT/End-of-Day Reports/System - End of Day Log.md`.

**Standing rule this establishes:** a scheduled task is only real once it appears in the scheduled-task list *after* creation, and that verification is reported. Documentation is not evidence.
