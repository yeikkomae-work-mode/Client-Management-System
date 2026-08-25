# PRD — `cto` Agent (Chief Technology Officer)

**Date:** 2026-08-25
**Requested by:** Eikko
**Status:** ✅ **APPROVED & BUILT 2026-08-25** — Eikko approved in-session ("proceed with prompt"). Built directly rather than routed through `PROJECTS/Pending/`.
**Build prompt:** `PROJECTS/PROMPT - 2026-08-25 - CTO Agent Build (Claude Code).md` (kept for rebuild/reference)

---

## Problem

Weekends go into YouTube, newsletters, and tool discovery — and almost none of it survives the weekend. There's no place where "I saw this technique" becomes a verdict, and no record of what was already evaluated and rejected, so the same tools get re-litigated months later. Meanwhile the existing stack drifts: automations go stale silently (the #1 stated pain point — only `daily-eod-sync` still runs of four original scheduled tasks), and nothing owns noticing.

The 10-agent system covers execution. Nothing owns **technical judgment**: is this worth adopting, does it fit, what should I build next, and what's quietly broken.

## Success criteria

1. A weekend session ends with at least one entry written to `RESOURCES/Tech Radar.md` with a status and a reason — not a folder of unread links.
2. Re-asking about a previously evaluated tool returns the prior verdict and date instead of a fresh evaluation.
3. Every adopt/trial verdict states: monthly cost, what it displaces, stack-fit, and estimated stand-up time.
4. A monthly stack audit surfaces at least the known drift (dead scheduled tasks, `connector-status.md` staleness, unused agents) without being told what to look for.
5. Nothing is written into `.claude/`, client folders, or `PROJECTS/Pending/` without an explicit yes in-session.

## Scope

**Name:** `cto` · **Model:** `opus` · **Location:** `.claude/agents/cto.md`

### Four functions

**1. R&D scout — tech radar**
Evaluates a technique or tool against the real stack (Apollo, PlusVibe, Smartlead, Instantly, Pipedrive, HubSpot, Notion, Fathom, Zapmail, Apify, Claude Code) and returns one of:
`ADOPT` · `TRIAL` · `HOLD` · `KILL` — each with reasoning, never a bare verdict.

The four kill criteria, applied every time and stated explicitly in the verdict:

| Criterion | Question | Fails when |
|---|---|---|
| **Cost** | What's the monthly cost, and what does it displace? | Recurring spend with nothing retired and no revenue line |
| **Stack fit** | Does it connect to what's already live? | No path to Apollo / Smartlead / PlusVibe / Instantly / Pipedrive / Notion / Claude Code |
| **Time-to-value** | Can it be standing up inside one weekend? | Multi-week build → `HOLD`, not `ADOPT` |
| **Fragility** | What happens when it breaks, and how would I know? | Unmonitored automation, brittle scraper, undocumented credential → penalized hard |

**2. Architect — PRDs**
When something clears the bar, writes a PRD to `TEMPLATES/PRD Template.md` shape, sized to this system, referencing what already exists rather than reinventing it.

**3. Builder — after sign-off only**
Two-phase, hard gate in the middle: research → PRD → **stop, wait for explicit yes** → write the agent/skill/script. No exceptions, including "low-risk" files.

**4. Stack auditor**
Every session opens with a **lightweight drift check — 3 lines, not a full audit**: are the scheduled tasks still alive, how stale is `connector-status.md`'s last-verified date, is anything in `PROJECTS/Pending/` untouched >30 days. Full audit on request, which checks for silent decay: dead or stale scheduled tasks, `connector-status.md` drift against reality, agents never invoked, automations in `ARCHIVE - Inactive Automations/` that were never consciously killed, credentials with no documented owner. **Flags — never silently overwrites** `connector-status.md`, which stays a human-verified single source of truth.

### Jurisdiction

- **Internal ops stack** — agents, automations, scripts, Claude Code setup, folder system. Full jurisdiction.
- **Tools deployed for clients** — in scope, stricter gate: any recommendation must state client-side cost, who pays, migration risk, and rollback path. Recommendation only; never touches a live client account.
- **Skills to learn** — tracks capability gaps observed in the actual work (repeated manual steps in EOD reports, tasks that stall) and turns them into a learning path with a concrete first step.

### Inputs

1. **Pasted transcript** — the primary path. Eikko pastes a YouTube transcript; `cto` extracts the actual technique (not the video's summary), strips the sales pitch, and evaluates it. Explicitly instructed that YouTube URLs are not fetchable and to ask for the transcript rather than guessing at content from the title.
2. **Own web research** — given a topic, searches docs/forums/changelogs, which are better sourced than video.
3. **System gap reading** — reads the folder (EOD reports, task lists, campaign tracking) and proposes what to automate next, grounded in evidence of repeated manual work.

### Outputs

| Output | Path | Behavior |
|---|---|---|
| Tech Radar | `RESOURCES/Tech Radar.md` | Living table: tool, status, date evaluated, cost, verdict reasoning. Appended, never rewritten. Checked *before* evaluating anything, to avoid re-work. |
| Learning Log | `OUTPUT/Learning Log/YYYY-MM-DD.md` | Per-session: what was reviewed, what was kept, what was decided, open threads. Mirrors the EOD report pattern. |
| PRDs | `PROJECTS/Pending/` | Only on explicit approval — this folder feeds the unattended builder. |
| Notion | 🎛️ VA Command Center | Tech Radar twin **page** (not a database), same pattern as the Connector Status twin. Local file is what the agent reads at runtime; Notion copy is for Eikko to check off-laptop. |

## Non-goals

- **No client-market research** — that stays `market-scout`. `cto` looks inward at the stack; `market-scout` looks outward at client niches.
- **No implementation planning for code tasks** — that stays `Plan`. `cto` decides *whether and what*; `Plan` decides *how* once a build is approved.
- **No scheduled task this pass.** Deliberate: adding a recurring automation to fix "automations go stale silently" is exactly the trap. Run it manually for 2–3 weekends first; schedule only if it earns it.
- Does not touch live client accounts, campaigns, credentials, or send anything.
- Does not edit `connector-status.md` — flags drift for Eikko to verify.

## Constraints

- Must follow existing agent file format (frontmatter: `name`, `description`, `tools`, `model`) — see `.claude/agents/market-scout.md`.
- Must read `.claude/agents/_shared/connector-status.md` before claiming any tool is live.
- Must obey `ABOUT ME/Operating Instructions.md`: PRD-first, pushback over agreement, no fabricated metrics or connector status, reversibility gate before anything destructive.
- Tools: `Read, Grep, Glob, WebSearch, WebFetch, Write, Edit, Bash` — Write/Edit needed for radar + log + PRD; gated by the sign-off rule for anything else.
- Adds one new folder: `OUTPUT/Learning Log/`. Structural change, hence this PRD.

## Plan

1. Create `RESOURCES/Tech Radar.md` with header, criteria legend, and a table **seeded with the current stack** — Apollo, Smartlead, PlusVibe, Instantly, Pipedrive, HubSpot (not connected), Notion, Fathom, Gmail multi-account, Zapmail, Apify, Higgsfield (MCP live / 0 credits), Canva, Miro, Zoom, the design skills installed Aug 18, and anything in `ARCHIVE - Inactive Automations/`. Status + date + one-line why for each, sourced from `connector-status.md` — no invented statuses.
2. Create `OUTPUT/Learning Log/` with a `README.md` explaining the pattern.
3. Write `.claude/agents/cto.md` — full agent definition per above.
4. Update `.claude/agents/README.md` and root `CLAUDE.md` — add `cto` under a new **Strategy** heading (it's neither front- nor back-office).
5. Update root `README.md` agent system section: 10 agents → 11.
6. Optional: `/tech-radar` slash command for quick status lookups.
7. Notion: create the Tech Radar twin page inside 🎛️ VA Command Center, mirroring the seeded table.
8. Verification: dry-run on one real example — paste a transcript, confirm it produces a radar entry with all four criteria stated and correctly refuses to build anything without a yes.

## Resolved (was: open questions)

1. **Notion page** — a page inside 🎛️ VA Command Center, not a database. Consistent with the Connector Status twin; revisit if the radar outgrows a flat table.
2. **Client-tool recommendations** — allowed, *with* a written risk note: client-side cost, who pays, migration risk, rollback path. Still recommendation-only; never touches a live client account.
3. **Stack audit cadence** — lightweight auto-check at every session start (3 lines), full audit on request.
4. **Radar seeding** — yes, backfill the current stack so the agent starts with a real baseline and doesn't re-pitch tools already in use.

## Remaining risks

- **Scope creep.** Four functions in one agent is a lot. If in practice the radar and the audit fight for attention, split the auditor out rather than letting either get thin.
- **The radar rots too.** A tech radar is itself an artifact that goes stale — a `TRIAL` entry with no follow-up date is just a bookmark. Mitigation: every `TRIAL` entry must carry a review-by date, and the lightweight session check surfaces overdue ones.
- **No schedule means it may just not get used.** Accepted for now; revisit after 2–3 weekends.

---

**Sign-off:** ✅ Approved to build — Eikko, 2026-08-25

## Build record — 2026-08-25

| File | Change |
|---|---|
| `.claude/agents/cto.md` | **new** — agent definition, model `opus` |
| `RESOURCES/Tech Radar.md` | **new** — seeded with 30+ baseline rows from `connector-status.md` |
| `OUTPUT/Learning Log/README.md` | **new** — folder + session-log template |
| `.claude/commands/tech-radar.md` | **new** — `/tech-radar` lookup command |
| `.claude/agents/README.md` | 10-agent → 11-agent, Strategy section, CTO output paths |
| `CLAUDE.md` | Strategy section, `/tech-radar` in command list |
| `README.md` | 11 agents, Strategy block, Learning Log in folder structure |
| `.claude/commands/agent-manager.md` | Strategy group added |
| Notion | [📡 Tech Radar](https://app.notion.com/p/3c7811e21c7f81d2814bef36e02b62f4) created in 🎛️ VA Command Center |

Backups taken before edits: `CLAUDE.md.bak-2026-08-25`, `README.md.bak-2026-08-25`, `.claude/agents/README.md.bak-2026-08-25`. `connector-status.md` untouched by this build (its 2026-08-25 change was the Higgsfield row from a separate session).

## Cross-build conflicts found at build time — needs Eikko's call

Three other C-suite PRDs were drafted the same day in parallel sessions. Two collide with this one:

1. **CFO PRD** lists a **"tools register"** as one of its four outputs. The Tech Radar already carries a cost column per tool. Two registers of what Eikko pays for will drift. **Proposal:** CFO owns *spend* (what it costs, what it's charged to), CTO owns *verdict* (whether it should exist at all), and the CFO's register links to the radar rather than duplicating it.
2. **Chief of Staff PRD** is a routing/context front door for the agent roster. It must be updated to know `cto` exists (11 agents, not 10) — and there's an open question about whether the CoS or the CTO owns the session-open drift check. Currently both would do it.
3. **CMO PRD** — no overlap detected.
