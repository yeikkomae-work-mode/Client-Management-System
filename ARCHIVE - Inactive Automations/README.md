# Archive — Inactive Automations & Scheduled Tasks

**Archived:** 2026-08-13
**Why:** These files document an automation setup (built ~Aug 5-6, 2026) that is no longer running. They're kept here for reference in case any of it gets reactivated or rebuilt later — nothing was deleted, just moved out of the active docs so current status pages don't lie.

---

## What's actually true right now

Checked directly against the scheduled-tasks system on 2026-08-13:

| Task ID | Was for | Status |
|---|---|---|
| `eco-morning-email-briefing` | Gmail/Outlook morning digest | **Disabled** since ~Aug 6, last ran Aug 6 |
| `lemwarm-alex-daily-monitor` | Lemwarm deliverability score alerts | **Disabled** since ~Aug 6, last ran Aug 6 |
| `plusvibe-daily-mailbox-monitor` | PlusVibe mailbox health checks | **Disabled** since ~Aug 6, last ran Aug 6 |
| `remind-fatin-lemlist-mailboxes` | One-time reminder | Fired Aug 12, complete, no action needed |
| `chris-caffera-week-tasks-reminder` | Manual-trigger only | Never auto-fires, not really an "automation" |
| `daily-eod-sync` | Syncs chat activity into EOD logs | ✅ **Still active** — this is the only one actually running |

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

The task definitions still exist (just disabled) — re-enabling `plusvibe-daily-mailbox-monitor`, `lemwarm-alex-daily-monitor`, or `eco-morning-email-briefing` would bring them back without rebuilding from scratch. Worth re-checking the underlying setup (Lemwarm score, PlusVibe mailbox count, VIP contact list) still matches reality before flipping them back on, since some of it may be a week+ stale.

Still-current reference files that were **not** archived: `ECO_CLIENTS.md`, `ECO_README.md`, and the remaining setup/config guides in `TEMPLATES/01 Automation Daily Routine/` (notably `CLIENT ACCOUNT MAPPING - CRITICAL.md`) — those are general reference material, not status claims.

**Correction, 2026-08-25:** one of those `TEMPLATES/01 Automation Daily Routine/` guides *has* since been archived — `ECO - Chief of Staff Guide.md`, now in `5-agent-version-superseded/`. It wasn't a status claim, so the line above was right on its own terms, but it described the superseded 5-agent ECO system and shared a name with the `chief-of-staff` agent built 2026-08-25 — two "chief of staff" documents describing different systems is exactly the confusion this archive exists to prevent. See that subfolder's README.
