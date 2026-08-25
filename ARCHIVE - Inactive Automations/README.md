# Archive — Inactive Automations & Scheduled Tasks

**Archived:** 2026-08-13
**Why:** These files document an automation setup (built ~Aug 5-6, 2026) that is no longer running. They're kept here for reference in case any of it gets reactivated or rebuilt later — nothing was deleted, just moved out of the active docs so current status pages don't lie.

---

## What's actually true right now

**Corrected 2026-08-25.** The table below was itself wrong. It was checked against the scheduled-tasks system on 2026-08-13 and asserted that `daily-eod-sync` was "still active — the only one actually running." A live check on 2026-08-25 found **no scheduled tasks in this system at all.** Not the disabled three, not `daily-eod-sync`, not `project-builder-check`. None of them exist as task definitions; there is nothing to re-enable.

| Task ID | Was for | Status as of 2026-08-25 |
|---|---|---|
| `eco-morning-email-briefing` | Gmail/Outlook morning digest | ❌ **Does not exist.** Last ran Aug 6; no task definition remains |
| `lemwarm-alex-daily-monitor` | Lemwarm deliverability score alerts | ❌ **Does not exist.** Last ran Aug 6; no task definition remains |
| `plusvibe-daily-mailbox-monitor` | PlusVibe mailbox health checks | ❌ **Does not exist.** Last ran Aug 6; no task definition remains |
| `remind-fatin-lemlist-mailboxes` | One-time reminder | Fired Aug 12, complete, no action needed |
| `chris-caffera-week-tasks-reminder` | Manual-trigger only | ❌ **Does not exist** |
| `daily-eod-sync` | Syncs chat activity into EOD logs | ❌ **Does not exist — and never did.** This row previously read "✅ Still active — this is the only one actually running." That was false |

**Decision (Eikko, 2026-08-25):** don't rebuild any of it. Everything runs interactively. `PROJECTS/README - Builder Pipeline.md` was deleted for the same reason. See `RESOURCES/Tech Radar.md` → Evaluations for the verdict and reasoning.

**The standing rule this produced:** a scheduled task is only real once it appears in the scheduled-task list *after* creation, and that verification is reported. Documentation is not evidence. Recorded in `.claude/agents/_shared/connector-status.md` → Standing rules.

The files below all describe the three disabled tasks as "✅ Active" / "Live" — that was accurate on Aug 5-6 but isn't anymore.

## Files in this archive

- `ECO_MASTER_STATUS.md` — system overview claiming the 3 automations + browser profiles were live
- `ECO_WORKFLOWS.md` — workflow definitions for morning briefing, Lemwarm monitor, LinkedIn posting
- `ECO_LIVE_DATA.md` — tool connection snapshot (Smartlead/Pipedrive/Apollo/etc. "live" status)
- `ECO_INDEX.md` — navigation index for the whole ECO status bundle above
- `ECO_EMAIL_INTELLIGENCE.md` — email monitoring/filtering config tied to the morning briefing task
- `ECO_SESSION_LOG_20260805.md` — historical session log from the original build
- `ECO_SYNC_VERIFICATION.md` — sync checklist confirming (at the time) the bundle above was current
- `ECO IS READY - GO LIVE NOW.md` — original activation announcement
- `PLUSVIBE MONITORING SETUP.md` — setup doc for the disabled PlusVibe monitor
- `Automation-Status.md` — dashboard claiming webhook/Calendly/domain-blocking automations were running (none of these ever showed up as actual scheduled tasks, so treat as aspirational/unverified)

## If you want to reactivate any of this

**Correction 2026-08-25:** this section previously said "the task definitions still exist (just disabled)" and that re-enabling them would work without rebuilding. **That is false** — no task definitions exist. Reactivating any of these means building them from scratch as new remote scheduled tasks, and re-checking the underlying setup (Lemwarm score, PlusVibe mailbox count, VIP contact list) first, since all of it is now weeks stale.

Eikko's decision on 2026-08-25 was **not** to rebuild. Don't reactivate anything here without revisiting that.

Still-current reference files that were **not** archived: `ECO_CLIENTS.md`, `ECO_README.md`, and the remaining setup/config guides in `TEMPLATES/01 Automation Daily Routine/` (notably `CLIENT ACCOUNT MAPPING - CRITICAL.md`) — those are general reference material, not status claims.

**Correction, 2026-08-25:** one of those `TEMPLATES/01 Automation Daily Routine/` guides *has* since been archived — `ECO - Chief of Staff Guide.md`, now in `5-agent-version-superseded/`. It wasn't a status claim, so the line above was right on its own terms, but it described the superseded 5-agent ECO system and shared a name with the orchestrator agent built 2026-08-25 — two "chief of staff" documents describing different systems is exactly the confusion this archive exists to prevent. That agent has since been renamed `chief-of-staff`, which removes the collision, but the guide stays archived on its own merits: it documents a 5-agent system that no longer exists. See that subfolder's README.
