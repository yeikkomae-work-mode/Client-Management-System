---
description: List available client-management agents and what each one does
argument-hint: "[agent-name] (optional — shows detail on one agent)"
---

If `$ARGUMENTS` is empty, list all agents below with a one-line description each, grouped Front-office / Back-office.

If `$ARGUMENTS` names an agent, read `.claude/agents/$ARGUMENTS.md` (fuzzy-match on name) and summarize its scope, tools, model, and any per-client rules it contains.

## Front-office (Client-facing work)

- **lead-prospector** — Apollo searches, campaign create/pause, list building
- **copywriter** — Cold email sequences, LinkedIn posts, campaign copy
- **reply-handler** — Inbound campaign replies, objection handling, Calendly bookings
- **market-scout** — Competitor research, industry trends

## Back-office (Operations & management)

- **inbox-triage** — Email triaging, reply drafting across multiple accounts
- **project-manager** — Task rollups, tracking, daily/weekly task management
- **cfo** — Money: monthly close, cash-flow & runway, debt payoff, tool/subscription cost, invoice prep
- **billing-auditor** — Time tracking, invoices, monthly P&L *(superseded by `cfo`; removal pending Eikko's go-ahead)*
- **file-organizer** — Folder structure, deduplication, file hygiene
- **onboarding-guide** — New client setup, folder structure, onboarding checklist
- **meeting-summarizer** — Call transcripts → minutes & action items

To use one, either invoke it directly with the Agent tool by name, or just describe the task — Claude Code will route to the right agent based on its description.
