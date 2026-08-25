---
description: List available client-management agents and what each one does
argument-hint: "[agent-name] (optional — shows detail on one agent)"
---

If `$ARGUMENTS` is empty, list all agents below with a one-line description each — the orchestrator first, then grouped Front-office / Back-office.

If `$ARGUMENTS` names an agent, read `.claude/agents/$ARGUMENTS.md` (fuzzy-match on name) and summarize its scope, tools, model, and any per-client rules it contains.

## Orchestrator (not part of the front/back-office split)

- **chief-of-staff** — Front door for the 10 specialists: routes, sequences multi-step work, sanity-checks results, checkpoints session memory. Doesn't do client work itself. Holds the routing table, authority rules, and session-memory protocol. Run `/cos`.

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

To use one, either invoke it directly with the Agent tool by name, or just describe the task — sessions in this folder default to chief-of-staff mode and route for you (see the root `CLAUDE.md`), and Claude Code will also auto-pick a specialist from its description when the match is obvious.

Delegation happens from the main thread — a subagent can't spawn another subagent — so chief-of-staff is the mode the main thread runs in, not a dispatcher to hand off to.
