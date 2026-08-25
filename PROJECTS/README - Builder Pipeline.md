# Autonomous Builder Pipeline

Drop a PRD, wake up to a finished build. Added 2026-08-15, adapted from Tina Huang's "autonomous builder" pattern.

## How it works

1. **Drop a PRD** into `PROJECTS/Pending/` — use `TEMPLATES/PRD Template.md`. File name: `YYYY-MM-DD - <short name>.md`.
2. A scheduled task (`project-builder-check`, every 3 hours) checks `Pending/` for new files.
3. When it finds one: moves it to `In-Progress/`, builds exactly what the PRD scopes (following the Operating Instructions — checks what already exists, doesn't touch anything outside scope), and logs what it did directly in the PRD file as it goes.
4. On success: the PRD (with a build log appended) moves to `Done/`, and the actual built files land wherever the PRD specified (an agent in `.claude/agents/`, a template in `TEMPLATES/`, a new client folder, etc.) — never inside `PROJECTS/Done/` itself.
5. On failure or a blocker it can't resolve alone (missing credential, ambiguous scope, something destructive it needs sign-off on): moves the PRD to `Failed/` with a note explaining exactly what's blocking it, instead of guessing.

## Folders

- `Pending/` — PRDs waiting to be picked up. Human-maintained — only Eikko drops files here.
- `In-Progress/` — Currently being built. Should normally be empty between runs.
- `Done/` — Completed PRDs with build logs appended. Historical record, not a place to re-run from.
- `Failed/` — Blocked PRDs with a clear note on what's needed to unblock. Check this periodically — nothing in here retries automatically.

## Rules

- Only PRDs that already have sign-off (`✅ Approved to build`) get picked up. An unsigned PRD sits in `Pending/` until approved.
- Anything the PRD didn't explicitly scope doesn't get touched — no scope creep during an unattended run.
- Destructive or irreversible steps implied by a PRD (deleting files, client-facing sends, financial actions) still get flagged and moved to `Failed/` for a real go-ahead rather than executed unattended, per `ABOUT ME/Operating Instructions.md`.

## Schedule

`project-builder-check` — every 3 hours, all day. Adjustable via the scheduled-tasks system if the cadence turns out to be too much or too little.
