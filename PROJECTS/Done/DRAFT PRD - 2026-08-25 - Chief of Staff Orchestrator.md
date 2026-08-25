# PRD — Master-list fix + Chief of Staff Orchestrator

**Date:** 2026-08-25
**Requested by:** Eikko
**Status:** ✅ Built 2026-08-25 — build log appended below, filed to `PROJECTS/Done/`

> **⚠️ Provenance note, read this first.** The build prompt referenced this file at
> `PROJECTS/DRAFT PRD - 2026-08-25 - Chief of Staff Orchestrator.md` and said to read it, then
> append a build log and move it to `PROJECTS/Done/`. **That file did not exist** — `PROJECTS/`
> contained only `Active/`, `Prospective/`, and `README - Builder Pipeline.md` at the time of
> the build. The Problem / Success criteria / Scope / Plan sections below are therefore
> **reconstructed from the build prompt itself**, not from a draft Eikko wrote and signed off.
> They are an accurate record of what was built and why, but they are not a pre-build document
> and should not be read as one. If a real draft exists somewhere outside this repo, this file
> should be reconciled against it.

## Problem

Two related problems, one structural and one operational.

**1. The master list wasn't a master list.** `PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md` was
named like a cross-client rollup, but its own header read *"Master Task List - Albert Scott
Operations"* and all 16 of its sections were Yoni/Albert Scott work.
`.claude/agents/project-manager.md` called it "the cross-client master list," which was false.
No genuinely cross-client task file existed anywhere, so no agent could honestly answer *"what's
on my plate."* The `project-manager` agent's own 2026-08-13 setup audit had already identified
this as "the biggest structural gap" — it had just never been acted on.

**2. There was no front door.** Ten specialist agents existed, each good at its own lane, with
no layer above them that decided which lane a request belongs in, sequenced multi-step work,
checked results before they reached Eikko, or made sure the session's decisions got written down
somewhere durable. In practice that meant Eikko doing the routing himself, and work happening in
chat windows that never got logged.

## Success criteria

- `git log --follow` still traces the Yoni list's history through the rename.
- Zero stale references to the old filename anywhere in the repo.
- Every item in the new cross-client file traces to a real line in a real source file, cited.
- Clients with thin or absent tracking are written down as coverage gaps, not left blank and
  not filled with invented entries.
- Routing logic exists in exactly one file; every other file points at it rather than copying it.
- All four verification scenarios pass when actually run, not asserted.

## Scope

**Phase 1 — fix the cross-client task-list gap**
- `git mv` the Yoni-only file to an honest name; contents otherwise untouched.
- Update every reference to the old filename repo-wide.
- Build a genuine cross-client rollup from the 8 per-client EOD logs, `PROJECTS/Active/*`, and
  `CLIENT PROFILES/Important info.md`.
- Correct `project-manager.md`'s false cross-client claim; date-stamp its stale audit block.

**Phase 2 — build the orchestrator**
- `.claude/agents/chief-of-staff.md` (model: opus).
- A routing section in the root `CLAUDE.md` that points at that file rather than restating it.
- `.claude/commands/cos.md`.
- Roster updates in `.claude/agents/README.md` and `.claude/commands/agent-manager.md`.

## Non-goals

- Re-running the daily rollup as a live habit. The file now exists; the practice of running it
  every morning still doesn't, and this build didn't create it.
- Touching the `backend/` + `frontend/` dashboard app, or the generated `.claude-dashboard/`
  data beyond the renamed path string.
- Resolving any of the client-side open items the rollup surfaced. Surfacing ≠ fixing.
- Deleting anything.

## Constraints

- `TEMPLATES/01 Automation Daily Routine/ECO - Chief of Staff Guide.md` describes a **superseded
  5-agent system**. This build does not extend it and must not be confused with it.
- `.claude/agents/_shared/connector-status.md` stays the single source of truth for connectors.
  Nothing built here may carry its own copy of tool statuses.
- Existing agent-file conventions (YAML frontmatter: `name`, `description`, `tools`, `model`)
  must be matched exactly.
- Authority rules from `ABOUT ME/Operating Instructions.md` apply to the build itself and must
  be encoded into what gets built.

## Plan

1. Rename with `git mv`; update all references; verify zero stale hits.
2. Build the cross-client rollup from source; verify every citation resolves.
3. Fix `project-manager.md`; commit Phase 1.
4. Build the four Phase 2 artifacts.
5. Run all four verification scenarios; commit Phase 2.
6. Append this build log; file to `Done/`; flag the two open items for Eikko.

---

**Sign-off:** ⬜ *Not obtained — see the provenance note above. This build ran from a direct
instruction in the session, not from an approved PRD in `Pending/`.*

---
---

# Build log — 2026-08-25

## Phase 1

**Renamed.** `PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md` → `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md`
via `git mv`. Git recorded it as a pure rename (0 content changes), so `--follow` history
survives intact.

**References updated — 14 files:**

| File | What changed |
|---|---|
| `README.md` | 3 refs → now names both files distinctly (rollup vs. Yoni-only) |
| `ABOUT ME/CLAUDE.md` | keep-in-sync list now points at the rollup, with Yoni's file as the client-scoped case |
| `CLIENT PROFILES/Yoni - Profile (Albert Scott).md` | → `YONI-TASK-LIST-ACTIVE.md` |
| `.claude/agents/project-manager.md` | 4 refs — see below |
| `.claude/agents/meeting-summarizer.md` | now splits client-specific vs. cross-client destinations |
| `PHASE-2.5-START-HERE.txt`, `-DEPLOYMENT.md`, `-CHECKLIST.md`, `-README.md` | test-command paths and one sample log string |
| `ARCHIVE - .../5-agent-version-superseded/ops.md`, `clients.md`, `strategy.md` | paths corrected so nothing points at a dead file, each with an inline note saying what the line used to read |
| `.claude-dashboard/dashboard-data.json`, `dashboard-data.js`, `central-command-hosted.html` | 288 occurrences of the path string |

**Judgment calls worth knowing about:**

- **The archive was updated, not left alone.** `ARCHIVE - Inactive Automations/5-agent-version-superseded/`
  is a historical record, and rewriting history is normally wrong. But three of its files were
  *pointing at a path that no longer exists*, and two of them repeated the same false
  "cross-client" label this build set out to kill. Paths were corrected and each edit carries an
  inline note stating what the line originally said — the record is preserved, the dead pointer
  isn't.
- **The dashboard data files were string-replaced, not regenerated.** `.claude-dashboard/scan.py`
  generates them and would have refreshed the paths correctly — but it also stamps `systemRoot`
  and `generatedAt`, and running it in a session whose root isn't Eikko's machine would have
  written a wrong `systemRoot` and a large spurious diff. Only the path string changed. Next
  real `scan.py` run will regenerate them cleanly either way.

**Built:** `PROJECTS/Active/MASTER-TASK-LIST-CROSS-CLIENT.md` — 102 line items across 8 clients,
every one citing its source file and last-touched date, plus a coverage table, a stale/blocked
section with day counts, and a hard-deadlines section.

Per-client counts at build time:

| Client | Open items | Last EOD entry |
|---|---|---|
| Yoni (Albert Scott) | 21 | 2026-08-19 |
| Chris Caffera (Fractio + HPG) | 20 | 2026-08-14 |
| Cüneyt (Starfix) | 14 | 2026-08-21 |
| Chris Drew (Satlas) | 11 | 2026-08-22 |
| Penji | 11 | 2026-08-24 |
| Krishna | 3 | 2026-08-10 |
| Edward Lehner | 3 | 2026-08-12 |
| Chris Soriano | 1 | **never** |
| *(cross-cutting)* Stale/blocked | 12 | — |
| *(cross-cutting)* Hard deadlines | 6 | — |

**Coverage gaps written down rather than papered over:**
- **Chris Soriano** — no real EOD entry has ever been written; the file is 100% template
  placeholders. His profile describes the engagement as sporadic/as-needed, so an empty log is
  *consistent with* no work being assigned and is **not** evidence of missed work. Both readings
  are stated; neither is presented as the answer.
- **Krishna** — log stops 2026-08-10, 15 days silent, with one blocker (Philippines copy awaiting
  his sign-off) unmoved since Aug 7.
- **Chris Caffera** — the log carries its own `2026-08-15 → 2026-08-24 — ⚠️ NOT LOGGED` block.
  Every Caffera item is at last-known state, not verified current state, and says so.
- **Edward Lehner** — one entry ever, and the Upwork offer the whole engagement depends on
  expired 2026-08-19 with no recorded outcome.

**`project-manager.md`** — "Where tasks actually live" now names both files correctly and states
plainly that the old cross-client claim was wrong. The 2026-08-13 setup audit is retitled
**HISTORICAL — superseded 2026-08-25** with a blockquote saying which of its findings have since
been acted on, so a future session can't read week-old findings as current.

**Phase 1 verification:** re-grepped for the old filename — zero stale references remain. The six
surviving mentions are all deliberate "renamed from / path corrected" annotations; no reference
resolves to a dead path. All 16 source paths cited in the rollup resolve to real files, and 16
headline claims were spot-checked against the exact text in their source. One item was **cut**
during verification: a duplicated "Hillary/Referral Finance unlaunched" line filed under Yoni
with no citation — it's a Chris Drew/Satlas item and appears once, cited, in his section.

## Phase 2

Built four things. **Routing logic lives in exactly one file** — `.claude/agents/chief-of-staff.md`
— and every other file points at it. Two copies of a routing table means one of them is wrong
within a week, and that failure mode is the reason this system has a single connector-status file
in the first place.

1. **`.claude/agents/chief-of-staff.md`** (`model: opus`) — identity as the front door that routes
   rather than does; a routing table with one row per specialist, each derived from that agent's
   own file; owns-outcomes-not-handoffs (name the sequence → delegate → sanity-check → report
   once); the authority table verbatim; the connector rule as *read at runtime, never copy
   statuses here*; folder separation; and the session-memory protocol (when to checkpoint, where
   each kind of thing goes, the contradiction rule). The escape hatch is placed **first**, before
   the routing table, so a "just…" request never reads past it.

2. **Root `CLAUDE.md`** — new *"How sessions in this folder open"* section that points at the
   agent file instead of restating the table, carries the escape hatch, and notes that delegation
   happens from the main thread (a subagent can't spawn one). Build discipline and the agent
   roster were left intact; the orchestrator was added above the front/back-office split and
   `/cos` added to the slash-command list.

3. **`.claude/commands/cos.md`** — matches `agent-manager.md`'s format. No args → read the rollup
   and report deadlines, stale items, per-client counts, and coverage gaps, then ask. With args →
   resolve scope (including client nicknames), produce the plan, check the authority table
   *before* delegating, execute, verify, report once, checkpoint.

4. **Roster updates** — `.claude/agents/README.md` and `.claude/commands/agent-manager.md` both
   list chief-of-staff as an orchestrator above the split, not inside either. "10-agent team"
   wording updated to "10 specialists behind an orchestrator" in `README.md`, `ABOUT ME/CLAUDE.md`,
   `ABOUT ME/Operating Instructions.md`, and the header line of `_shared/connector-status.md`
   (that file's tool rows were not touched).

## Phase 2 verification — run, not asserted

**1. Cross-client — "what's on my plate."** Routes to `project-manager` (the row matches, and the
agent's own `description` independently claims the phrase). That agent's file now points at
`MASTER-TASK-LIST-CROSS-CLIENT.md` first. Reading it surfaced 3 lapsed/overdue deadlines
(Edward's expired offer, Penji's Dripify trial, Caffera's Apollo export) and 12 stale/blocked
items with day counts — every one citing a source file. **Pass.**

**2. Single-client write — "log today's Satlas work: paused two campaigns pending domain fixes."**
"Satlas" resolved to Chris Drew. Classified against the authority table as an in-repo file write
→ auto, report it. Wrote a dated 2026-08-25 entry to
`OUTPUT/End-of-Day Reports/Chris Drew - End of Day Log.md`. Blast radius measured by md5-summing
all 2,086 files before and after: **exactly one file changed.** No other client's files touched.
**Pass.** Note: the report didn't say *which* two campaigns or which domains — the entry records
that as unspecified rather than guessing, and flags the Zapmail decision as a lead to check, not
a fact.

**3. Fabrication check — "pull my HubSpot deals."** Read `_shared/connector-status.md`: HubSpot is
**🟡 Not connected** — the connector exists in the registry but needs Eikko to authorize it in
claude.ai connector settings. Independently confirmed by searching the live tool surface: no
HubSpot MCP server is connected this session (the search returns Pipedrive and Apollo instead).
Fallback per the file's own rule: authorize the connector, or pull manually in the browser.
**No deal data was invented. Pass.**

**4. Guardrail check — "send the follow-up to Krishna."** Classified as client-facing → **STOP,
show the plan, wait for an explicit yes.** Not drafted-and-sent, and not delegated first: the
agent file requires stopping *before* handing off, so the request never reaches `copywriter` or
`reply-handler` in a state where it could fire. Belt and braces — those two are draft-only by
their own files anyway. Reading Krishna's log to learn what the follow-up would even be about is
a read, which is auto. **Pass.**

## Things the PRD didn't anticipate

1. **The PRD itself was missing.** See the provenance note at the top. `PROJECTS/Done/` also
   didn't exist and had to be created — see the flagged item below.
2. **The dashboard app hardcodes the ten agent names in three places** —
   `backend/services/file-watcher.js`, `backend/routes/agents-tracking.js`, and `backend/db.js`
   each carry a literal 10-name array. Adding an 11th agent file means `chief-of-staff` will not
   appear in the Agents Office UI, and `db.js` uses `INSERT OR IGNORE`, so an existing database
   wouldn't pick it up even if the array were extended. **Not fixed** — that app was outside this
   build's scope and changing it unasked would be scope creep. Flagged here so it's a decision,
   not a surprise.
3. **The root `CLAUDE.md` files `inbox-triage` under Back-office**, while `.claude/agents/README.md`,
   the agent's own file ("front-office #1"), and the build prompt all place it in Front-office.
   The instruction was to add to the roster, not rewrite it, so this was **left as-is and flagged**
   rather than silently corrected. The chief-of-staff routing table has it under Front-office,
   matching the agent's own file.
4. **`CLIENT PROFILES/Important info.md` is 20 days stale** (header says 2026-08-05) and several
   of its per-client rate blocks still read "(TBD)" where a rate is confirmed elsewhere —
   `billing-auditor.md` had already flagged the same disagreement on 2026-08-13. The rollup uses
   it for working hours and says so; the disagreement is noted in the file rather than resolved.
5. **Cross-referencing surfaced one real conflict between clients**, now visible in one place for
   the first time: Penji's offer letter specifies an 8am–5pm full-time schedule with a contractual
   obligation to be online at shift time, which does not co-exist cleanly with Yoni's 9pm–5am
   block, Chris Caffera's 2pm–11pm block, and an active Cüneyt trial. Surfaced, not resolved —
   it's Eikko's call.
