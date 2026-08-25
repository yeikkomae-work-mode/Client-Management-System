# Claude Code Agent Reference

## How sessions in this folder open

**Default to chief-of-staff mode.** Unless the request is a one-liner (see the escape hatch
below), route it rather than doing it: read `.claude/agents/chief-of-staff.md` and follow it.

That file is the **single source of truth for routing** — the request-shape → agent → files
table, the authority rules for what stops and waits for a yes, the connector rule, the
folder-separation rule, and the session-memory protocol all live there and are deliberately
**not** restated here. Two copies of a routing table means one of them is wrong within a week.

**Escape hatch:** if the request opens with "just", or is a single obvious file edit, or is one
lookup in one file — skip routing and do it. Don't ceremony a one-liner.

**One structural note:** delegation happens from the main thread. A subagent cannot spawn
another subagent, so chief-of-staff works as the *mode the main thread runs in*, not as a
dispatcher you hand off to and then wait on.

## Build discipline

Anything nontrivial (new agent, new automation, new client system, structural folder change) gets a short PRD first — `TEMPLATES/PRD Template.md` — with Eikko's sign-off before building. Quick fixes, single-file edits, and routine logging (EOD reports, meeting files) skip this. Full operating rules: `ABOUT ME/Operating Instructions.md`.

Approved PRDs can also be dropped in `PROJECTS/Pending/` for unattended building — see `PROJECTS/README - Builder Pipeline.md`.

## Orchestrator

- **chief-of-staff** — Front door for the 10-agent team: routes, sequences, checks the result, and checkpoints session memory. Doesn't do client work itself. `/cos`

## Front-office (Client-facing work)

- **lead-prospector** — Apollo searches, campaign create/pause, list building
- **copywriter** — Cold email sequences, LinkedIn posts, campaign copy
- **reply-handler** — Inbound campaign replies, objection handling, Calendly bookings
- **market-scout** — Competitor research, industry trends

## Back-office (Operations & management)

- **inbox-triage** — Email triaging, reply drafting across multiple accounts
- **project-manager** — Task rollups, tracking, daily/weekly task management
- **billing-auditor** — Time tracking, invoices, monthly P&L
- **file-organizer** — Folder structure, deduplication, file hygiene
- **onboarding-guide** — New client setup, folder structure, onboarding checklist
- **meeting-summarizer** — Call transcripts → minutes & action items

## Specialized

- **Explore** — Fast code search (find files, grep symbols)
- **Plan** — Implementation strategy & architecture
- **general-purpose** — Complex multi-step research

## Slash Commands

- `/cos` — Chief of Staff: with no args, what's open across clients; with args, the routing plan for that goal
- `/agent-manager` — List the agents and what each one does
- `/code-review` — Review current diff for bugs and improvements
- `/simplify` — Simplify changed code
- `/claude-api` — Reference Claude API and models
- `/run` — Launch and test the app
