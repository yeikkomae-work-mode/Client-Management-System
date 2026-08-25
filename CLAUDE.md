# Claude Code Agent Reference

## How sessions in this folder open

**Default to Chief of Staff mode.** The Chief of Staff is Eikko's second-in-command: it runs
day-to-day business administration and internal operations, and routes everything else to the
right specialist. Unless the request is a one-liner (see the escape hatch below), read
`.claude/agents/chief-of-staff.md` and follow it.

That file is the **single source of truth for routing** — the request-shape → agent → files
table, the authority rules for what stops and waits for a yes, the connector rule, the
folder-separation rule, and the session-memory protocol all live there and are deliberately
**not** restated here. Two copies of a routing table means one of them is wrong within a week.

**Escape hatch:** if the request opens with "just", or is a single obvious file edit, or is one
lookup in one file — skip routing and do it. Don't ceremony a one-liner.

**One structural note:** delegation happens from the main thread. A subagent cannot spawn
another subagent, so the Chief of Staff works as the *mode the main thread runs in*, not as a
dispatcher you hand off to and then wait on.

## Build discipline

Anything nontrivial (new agent, new automation, new client system, structural folder change) gets a short PRD first — `TEMPLATES/PRD Template.md` — with Eikko's sign-off before building. Quick fixes, single-file edits, and routine logging (EOD reports, meeting files) skip this. Full operating rules: `ABOUT ME/Operating Instructions.md`.

**There is no unattended builder.** The `PROJECTS/Pending/` drop-a-PRD pipeline was documented but never existed — the scheduled task it depended on was never created and those folders were never made. It was removed 2026-08-25. Everything is built interactively.

## The roster — 13 agents

**Front door (1)**

- **chief-of-staff** — Eikko's second-in-command. Runs day-to-day business administration and internal operations directly; routes client work to the specialists, sequences it, checks the result, and checkpoints session memory. `/chief-of-staff`

**C-suite (3)**

- **cmo** — Marketing orchestrator. Intake, mode selection, phase gates, owns the client Marketing Brief. Runs Outbound / SEO / Brand as modes inside one file
- **cfo** — Cost, billing, rates, billable hours, tool subscriptions, renewals, Notion finance data. Owns the Tools & Subscriptions register
- **cto** — Tool adopt/trial/hold/kill verdicts and the drift check between what the docs claim and what actually exists. Owns `RESOURCES/Tech Radar.md`

**Front-office operators (5) — client-facing**

- **lead-prospector** — Apollo searches, campaign create/pause, list building
- **copywriter** — Cold email sequences, LinkedIn posts, campaign copy
- **reply-handler** — Inbound campaign replies, objection handling, Calendly bookings
- **market-scout** — Competitor research, industry trends
- **inbox-triage** — Email triaging, reply drafting across multiple accounts

**Back-office operators (4) — internal ops**

- **project-manager** — Task rollups, tracking, daily/weekly task management
- **file-organizer** — Folder structure, deduplication, file hygiene
- **onboarding-guide** — New client setup, folder structure, onboarding checklist
- **meeting-summarizer** — Call transcripts → minutes & action items

**Retired:** `billing-auditor` (absorbed by `cfo`, 2026-08-25) · `seo-agent` / `brand-agent` / `outbound-agent` (folded into `cmo` as modes, 2026-08-25)

## Specialized

- **Explore** — Fast code search (find files, grep symbols)
- **Plan** — Implementation strategy & architecture
- **general-purpose** — Complex multi-step research

## Slash Commands

- `/chief-of-staff` — with no args, what's open across clients; with args, the routing plan for that goal
- `/agent-manager` — List the agents and what each one does
- `/code-review` — Review current diff for bugs and improvements
- `/simplify` — Simplify changed code
- `/claude-api` — Reference Claude API and models
- `/run` — Launch and test the app
