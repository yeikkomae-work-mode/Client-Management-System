---
description: List available client-management agents and what each one does
argument-hint: "[agent-name] (optional — shows detail on one agent)"
---

If `$ARGUMENTS` is empty, list all 13 agents below with a one-line description each — the front door first, then the C-suite, then the operators grouped Front-office / Back-office.

If `$ARGUMENTS` names an agent, read `.claude/agents/$ARGUMENTS.md` (fuzzy-match on name) and summarize its scope, tools, model, and any per-client rules it contains.

**13 agents: 1 front door · 3 C-suite · 9 operators.**

## Front door (not part of the front/back-office split)

- **chief-of-staff** — Eikko's second-in-command. Runs day-to-day business administration and internal operations directly; routes client work to the specialists, sequences it, sanity-checks results, checkpoints session memory. Holds the routing table, authority rules, and session-memory protocol. Run `/chief-of-staff`.

## C-suite (domain orchestrators)

- **cmo** — Marketing orchestrator. Intake, mode selection, phase gates, owns the client Marketing Brief. Outbound / SEO / Brand run as modes inside one file
- **cfo** — Cost, billing, rates, billable hours, tool subscriptions, renewals, Notion finance data. Owns the Tools & Subscriptions register
- **cto** — Tool adopt/trial/hold/kill verdicts and the drift check between documented and actual state. Owns `RESOURCES/Tech Radar.md`

## Front-office operators (Client-facing work)

- **lead-prospector** — Apollo searches, campaign create/pause, list building
- **copywriter** — Cold email sequences, LinkedIn posts, campaign copy
- **reply-handler** — Inbound campaign replies, objection handling, Calendly bookings
- **market-scout** — Competitor research, industry trends
- **inbox-triage** — Email triaging, reply drafting across multiple accounts

## Back-office operators (Operations & management)

- **project-manager** — Task rollups, tracking, daily/weekly task management
- **file-organizer** — Folder structure, deduplication, file hygiene
- **onboarding-guide** — New client setup, folder structure, onboarding checklist
- **meeting-summarizer** — Call transcripts → minutes & action items

**Retired 2026-08-25:** `billing-auditor` → absorbed by `cfo`; `seo-agent` / `brand-agent` / `outbound-agent` → folded into `cmo` as modes.

To use one, either invoke it directly with the Agent tool by name, or just describe the task — sessions in this folder default to Chief of Staff mode and route for you (see the root `CLAUDE.md`), and Claude Code will also auto-pick a specialist from its description when the match is obvious.

Delegation happens from the main thread — a subagent can't spawn another subagent — so the Chief of Staff is the mode the main thread runs in, not a dispatcher to hand off to.
