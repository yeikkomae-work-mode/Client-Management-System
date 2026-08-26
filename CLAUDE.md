# Claude Code Agent Reference

## Build discipline

Anything nontrivial (new agent, new automation, new client system, structural folder change) gets a short PRD first — `TEMPLATES/PRD Template.md` — with Eikko's sign-off before building. Quick fixes, single-file edits, and routine logging (EOD reports, meeting files) skip this. Full operating rules: `ABOUT ME/Operating Instructions.md`.

Approved PRDs can also be dropped in `PROJECTS/Pending/` for unattended building — see `PROJECTS/README - Builder Pipeline.md`.

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

## Strategy

- **cio** — Access, credentials, scopes, data security; which inbox/sender belongs to which client; filing pasted Slack/WhatsApp threads

## Specialized

- **Explore** — Fast code search (find files, grep symbols)
- **Plan** — Implementation strategy & architecture
- **general-purpose** — Complex multi-step research

## Slash Commands

- `/code-review` — Review current diff for bugs and improvements
- `/simplify` — Simplify changed code
- `/claude-api` — Reference Claude API and models
- `/run` — Launch and test the app
