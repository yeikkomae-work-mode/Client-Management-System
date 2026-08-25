# PRD Template — Yoni Sales & Marketing Command Center (Phase 1)

Use for anything nontrivial: a new agent, a new automation, a new client system, or a structural change to this folder. Skip for quick fixes, single-file edits, or routine logging. See `ABOUT ME/Operating Instructions.md`.

**Date:** 2026-08-25
**Requested by:** Eikko (relaying Yoni's notes, verbatim source pasted into chat 2026-08-25)

## Problem

Yoni currently has an "Outbound Command Center" dashboard and a separate "Overdue Pipedrive Activities" dashboard — both referenced in the Notion Task Tracker (`Refine "Outbound Command Center" dashboard`, `Enhance "Overdue Pipedrive Activities" artifact`) as already live and set to refresh daily. **Neither is reachable from this Claude account** — they were built under Yoni's own separate Claude Code account, and no URL for either is recorded anywhere in this workspace or Notion. Confirmed with Eikko 2026-08-25.

Yoni's notes describe both specific fixes to that existing dashboard (Blue Dot meeting filter, bounce-rate list, unexplained "100/100 inboxes" and "Pipedrive Sync" boxes, unclear "Deliverability Watch List" domains) and a much larger reframing: a multi-channel **Sales & Marketing Command Center** with SmartLead, LinkedIn, Pipedrive, SEO, and SmartScout as clickable top-level sections, plus a Claude activity/audit log and a General/software-infrastructure registry.

Since the original artifact can't be edited in place, this has to be a fresh build under Eikko's account — which is also the only way it can plug into the Calendly/Smartlead-triage automation already migrated to n8n today (`Albert Scott — Reply & Booking Automation`, https://eikko.app.n8n.cloud/workflow/H5tFVaQm6MWayvv4) and its Google Sheets run log (`Albert Scott - n8n Automation Log`).

## Success criteria

- Yoni can open one dashboard and answer, at a glance: what happened yesterday (Smartlead sends, Interested replies) and what needs his attention today (overdue Pipedrive follow-ups, filterable by himself vs. Rachel).
- The SmartLead section matches Smartlead's own campaign list well enough to be immediately familiar, but is sortable/filterable in ways Smartlead's own UI isn't.
- The "100/100 inboxes" discrepancy is either resolved (dashboard shows the true count with an explanation of any exclusions) or explicitly flagged as needing Yoni's input if the API genuinely won't return more than 100.
- Every domain shown carries a plain-English reason when it's flagged (replacing the unexplained "Deliverability Watch List" label).
- Yoni can filter overdue Pipedrive activities by owner (Yoni / Rachel) and see lead, due date, activity type, owner per row.
- A Claude Activity Log exists showing every lead Claude categorized/updated/moved, filterable by date, action type, lead, and campaign — with drill-down to the triggering email and the category applied. This is populated from the same Google Sheet the n8n workflow already writes to.
- The BlueDot box and "Pipedrive Sync" box are either given a clear, actionable purpose or dropped from the main view.
- Passwords are never rendered in the page; credential entries link out to wherever they actually live (1Password, Notion, etc.) instead.

## Scope (this phase)

1. **Main dashboard** — yesterday's Smartlead sends + Interested replies, outstanding/overdue Pipedrive task counts, owner filter (Yoni/Rachel).
2. **SmartLead section** — campaign list (creation-order default, sort/filter by status/date/emails sent/reply rate/bounce rate), per-campaign metrics, inbox health (with the 100 vs. ~111 count resolved or explicitly flagged), domain list with plain-English flag reasons.
3. **Pipedrive section** — overdue/due-today/upcoming activities, filterable by owner, click-through to lead/contact detail.
4. **Claude Activity / Automation Log** — reads the `Albert Scott - n8n Automation Log` Google Sheet (both tabs) already wired into the n8n workflow; filterable by date, action type, lead, campaign.
5. Resolve or remove: BlueDot box, "Pipedrive Sync" box, "Deliverability Watch List" label — pending Yoni's answers in Open Questions below.

## Non-goals (this phase — explicitly deferred)

- **LinkedIn Outreach section** — no API/automation connector exists yet (`connector-status.md`: "LinkedIn — no API path, browser-assisted only"). Needs its own scoping pass once there's a real data source.
- **SEO section** — AIOSEO login exists (per Notion "SEO Logins") but no data pipeline into it yet.
- **SmartScout section** — no connector or prior integration found anywhere in this workspace. Needs Yoni to confirm what SmartScout access looks like before this is buildable.
- **General / Software & Infrastructure registry** — this is a data-gathering exercise (costs, seats, renewal dates, ownership) that only Yoni/Eikko can populate accurately; Claude can build the table structure but not the inventory itself sight-unseen.
- Rebuilding or migrating anything that lives on Yoni's own Claude account — out of reach, not attempted.

## Constraints

- Pipedrive and Smartlead connectors are already verified live per `connector-status.md` (Smartlead scoped to the Albert Scott/Yoni account only).
- Google Sheets access for the automation log goes through the same Google Drive access already used to create `Albert Scott - n8n Automation Log` today (file ID `1cEXs1sX0_Zdy08xq2iBvYmziOLd68OI-yeygzBR1BaU`).
- This is a fresh Artifact under Eikko's account — not an edit to the inaccessible original. Say so plainly to Yoni so he isn't looking for his old dashboard's URL.
- Follow `ABOUT ME/Operating Instructions.md` — no destructive/irreversible action (e.g. changing live Pipedrive records) without sign-off; this build only reads data and renders it.
- No plaintext passwords or API keys in the rendered page, per Yoni's own note.

## Plan

1. Resolve the three open questions below with Yoni (inbox count, Pipedrive Sync meaning, BlueDot's real purpose) — blocking for an accurate build, not something to guess.
2. Confirm Rachel's identifier in Pipedrive (user ID or email) so the Yoni/Rachel owner filter actually works.
3. Build the Main dashboard + SmartLead section + Pipedrive section as one Artifact, reading live from the Pipedrive and Smartlead connectors.
4. Wire the Claude Activity Log tab to the existing Google Sheet — this is the most "ready to build" piece since the data source already exists.
5. Set up the daily-refresh mechanism (a Routine that re-reads live data and republishes the Artifact), matching the "refreshes daily" behavior the old dashboard already had.
6. Review with Eikko before sharing the link with Yoni.

## Open questions

- **Inbox count**: does Smartlead's API cap list results at 100, or are ~11 inboxes genuinely excluded/inactive? Needs one live API check once this is picked up (not answerable from documentation alone).
- **"Pipedrive Sync" box**: what did it actually show? No description survives anywhere in this workspace — needs Yoni to describe or screenshot it, or it gets dropped per his own instruction ("if it does not provide useful information... it may not need to be prominent").
- **BlueDot**: same — what was the box doing? Per Yoni's note, the likely right call is dropping it from the main dashboard and treating BlueDot purely as a future input into Pipedrive updates, not a dashboard section — but confirm before building either way.
- **Rachel's Pipedrive identity**: user ID/email needed for the owner filter to work correctly.
- Does Yoni want this new artifact to fully replace references to the old one, or coexist while the old one (on his own account) keeps running?

---

**Sign-off:** ⬜ Approved to build — Eikko
