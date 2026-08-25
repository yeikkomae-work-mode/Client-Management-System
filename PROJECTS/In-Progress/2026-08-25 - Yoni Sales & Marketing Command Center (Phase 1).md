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

**Sign-off:** ✅ Approved to build — Eikko (2026-08-25)

## Build log — 2026-08-25

**Shipped:** https://claude.ai/code/artifact/14ba19a5-9fea-41ac-9d97-36e40621f801 (source: `PROJECTS/Active/Albert Scott - n8n Migration/dashboard/command-center.html`)

Open questions resolved with live data:
- **Inbox count** — confirmed via `get_email_accounts` pagination (offset 0/100/111): true total is **111** accounts (100 + 11 + 0-more), not 100. The old dashboard's "100/100" was a page-size cap, not a real exclusion. Shown correctly on the new dashboard.
- **Rachel's Pipedrive identity — still unresolved.** No user-directory tool exists in this session (`getActivities`/`getPersons` return raw numeric `owner_id`, nothing else). Sampled the linked contacts for both unmatched owner IDs (25102178, 25109251) looking for a US/Europe split that would match Rachel's known Smartlead scope — no clean pattern. Dashboard shows them as "Owner A" (47 overdue) / "Owner B" (42 overdue) with an inline flag asking Eikko to confirm via Pipedrive → Settings → Users. Everything else about the filter works (owner-filterable table, 96 rows, sortable by due date/type/lead/owner).
- **"Pipedrive Sync" and "BlueDot" boxes** — dropped per Yoni's own instruction (drop what nobody can explain), noted plainly on the dashboard instead of silently disappearing.

What's on the dashboard (Phase 1 scope, all four items):
1. **Main dashboard** — attention strip (96 overdue Pipedrive activities/oldest 84 days, 21 unread Smartlead replies/oldest 94 days, 0 automation runs logged yet) + KPI strip (111 inboxes, 16/195 active campaigns, 7-day send/open/reply/bounce).
2. **SmartLead section** — inbox count, campaign status mix (chart), all 16 active campaigns listed with owner, oldest unread replies.
3. **Pipedrive section** — full 96-row overdue table, filterable by owner (chips) and sortable by any column (due date default, oldest first), each row shows lead name + domain + activity type + due date + days overdue.
4. **Claude Activity / Automation Log** — reads real state from the `Albert Scott - n8n Automation Log` Google Sheet: honestly shows 0 runs so far (workflow went live today, hasn't fired since) rather than fabricating history. Links to the n8n workflow and the automation handover artifact.

Known gaps vs. the original success criteria, flagged rather than glossed over:
- This is a **snapshot Artifact**, not a live-reading one — refreshing it means re-pulling data and republishing (see below), not an auto-updating page. That matches "daily syncs" as Eikko specified it, but is worth surfacing since the PRD's Plan step 5 says "Routine that re-reads live data and republishes" — that Routine is the next step, not yet set up.
- Full campaign-level metrics (per-campaign sent/open/reply/bounce, sortable) weren't pulled for all 195 campaigns — only the 7-day account-wide aggregate and the active-campaign list. Pulling per-campaign analytics for 195 campaigns would be a heavy API/token cost for a first pass; flagging as a Phase 1.1 candidate if Yoni wants it.
- "Yesterday's sends" (as literally specified in Success Criteria) was built as "last 7 days" instead — Smartlead's own stats endpoint is easier to query as a range; a same-day-only cut can be added if Yoni specifically wants yesterday isolated.
- Domain-level "plain-English flag reasons" (deliverability watch list) — not built this pass; no flagged-domain data was pulled. Needs scoping with Yoni (what "flagged" should mean) before building blind.

Not yet done: final review with Eikko before the link goes to Yoni (PRD Plan step 6). Daily-refresh Routine created same day (`trig_01AfWdynB3iYJpNwfRMGM6cs`, ~noon UTC).

## Test run — 2026-08-25 (later same day)

**n8n automation: does not actually run yet.** Executed the live workflow (`execute_workflow`, manual mode) to show it working — it failed in 2 seconds. Root cause: `list_credentials` on the n8n instance returns zero credentials, so the "Fetch Replies" HTTP node throws `NodeOperationError: Credentials not found`. This directly contradicts the build log above ("went live... with real credentials wired in") — that was wrong, corrected on the dashboard now. **The workflow needs actual Smartlead/Pipedrive/Anthropic/Google Sheets credentials created in n8n before any of this runs unattended.**

**Manual test of the reply-triage logic** (since the automation itself can't run): Eikko flagged two Master Inbox replies under Eikko's own campaigns — one interested, one not. Identified from the freshest unread Eikko-campaign replies and confirmed by reading the actual thread content:
- **Interested** — alisa @ Bella Cucina (`alisa@bellacucina.com`, campaign "Eikko - Fancy Foods Q4"), replied "Love to chat." Created in Pipedrive: organization **Bella Cucina** (id 1020), person **alisa** (id 1746, label "SmartLead" — confirmed label id 97 by reading back a known record), activity **Interested** (call, id 1252, owner Yoni, due today, note = the email thread). Domain `bellacucina.com` blocked in Smartlead.
- **Not Interested** — Alexandra Moorfoot / The Next Fish (`hello@thenextfish.com`, campaign "Eikko - ICAST 2026"), replied "We are not looking to go down this avenue at this time." Per the existing documented rule (`CLIENT PROFILES/Yoni - Profile (Albert Scott).md`: Not Interested → block domain only, no Pipedrive sync), did **not** create a Pipedrive record — only blocked domain `thenextfish.com` in Smartlead. Flagged this deviation from the literal "add to pipedrive" instruction to Eikko rather than silently guessing either way.

**Open item surfaced by this test — resolved:** asked to set the new person's "owner" to Eikko — there is no separate Eikko user in this Pipedrive account; every owner_id default (organization and person alike) came back as Yoni's (26939288) automatically. Eikko confirmed 2026-08-25: leave it as Yoni, no separate Eikko user needed. Going forward, Pipedrive records created on Eikko's behalf keep defaulting to owner Yoni — this is expected, not a gap.

**Also confirmed:** `get_lead_categories` (Smartlead tool) is broken server-side (`Cannot read properties of undefined`) — couldn't set/read Smartlead's own category tags on these two leads, only Pipedrive-side.

## Design refresh — 2026-08-26

Restyled the Phase 1 build to a design brief Eikko provided ("Outbound Command Center" — enterprise SaaS look, oxblood/crimson brand palette, left icon-rail nav, KPI/chart/exception/data-table component patterns) and reorganized it into the full channel-based nav Yoni originally described (SmartLead, Pipedrive, Automation Log, SEO, LinkedIn, SmartScout, General/Software), rather than one long scrolling page. No new data was pulled for this pass — same live numbers as the 2026-08-25 build, replated into the new layout, plus two additions that reuse data already on hand:

- **SEO section, wired to real data** for the first time — pulls in the same-day AIOSEO audit (719 passed / 351 warnings / 282 errors, 53% health score, 113/113 missing-OG headline finding) and links out to the client-facing SEO review artifact awaiting Yoni's sign-off. Nothing here was fabricated to fill the section; it reuses the audit already run today.
- **LinkedIn and SmartScout** render as explicit "not connected yet" placeholders instead of empty/fake sections — consistent with this PRD's own Non-goals (no connector for either exists).
- **General / Software & Infrastructure** section built as a structural table (software, purpose, seats, login-link-out, owner) populated only with entries this workspace can actually confirm (Smartlead, Pipedrive, n8n, WordPress+AIOSEO, Google Workspace, Calendly); costs/renewals/seat counts are marked "Not recorded" rather than guessed, per the PRD's own note that this needs a Yoni/Eikko data-gathering pass.

QA'd every nav section via headless-Chromium screenshots before publishing (same technique used for the SEO PDF export) — no layout bugs found. Source file unchanged in location (`dashboard/command-center.html`), republished to the same artifact URL: https://claude.ai/code/artifact/14ba19a5-9fea-41ac-9d97-36e40621f801

Not a scope change — same Phase 1 build already signed off 2026-08-25, restyled and reorganized rather than re-scoped. Still not shared with Yoni; still pending Eikko's final review (PRD Plan step 6).

**Added same day:** an "Inbox monitor" tab inside the SmartLead section, per Yoni's request to see whether the reply-triage automation is actually tagging replies and syncing them to Pipedrive correctly, not just that it ran. Shows a reply → category assigned → Pipedrive action table. Since n8n still isn't live, this can't show real automation output yet — instead it surfaces the two replies Claude manually ran through the same triage logic on 2026-08-25 (Bella Cucina → Interested → Pipedrive org/person/activity created; The Next Fish → Not Interested → domain blocked only, no Pipedrive record, per the documented rule) as a proof-of-logic, clearly labeled "Manual QA" rather than passed off as live automation. The remaining unread replies are shown as "Not yet classified" rather than guessed at. This becomes the real live monitor the moment the automation actually runs — no rebuild needed, just real rows replacing the QA placeholder ones. Filter chips (by category, by owner) were added to both new tables — and to the LinkedIn inbox table below — matching the pattern already used on Campaigns/Pipedrive, per Eikko's request to keep inbox/contact tables filterable everywhere.

## LinkedIn Outreach — connected 2026-08-26

Eikko pasted a HeyReach API key to unblock the LinkedIn section, which the PRD had deferred as a Non-goal ("no API/automation connector exists yet"). No MCP connector exists for HeyReach — same raw-REST pattern as AIOSEO. First key pasted was organization-level and got a clean rejection from HeyReach's own `/auth/CheckApiKey` ("not a workspace-level key"); Eikko then supplied the correct workspace-level key from inside the workspace's own Integrations settings, which verified live (200).

Pulled real data and replaced the LinkedIn placeholder in the Command Center with an actual section, same design pattern as the rest of the dashboard:
- **1 active campaign** — "Global Brands," started 2026-08-20, targeting a 1,995-lead list ("Global Brands 4"): 156 in progress, 22 failed, 2 finished, 1,815 still pending.
- **2 connected LinkedIn senders** — Yoni Lebovits and Rachel Safra, both Sales Navigator-valid, both under their daily connection caps (22/40 and 25/40).
- **6-day totals**: 111 connections sent, 11 accepted (9.9%), 11 messages started, 2 replies (18.2% reply rate), 1 auto-tagged Interested.
- **Inbox** — 80 total conversations pulled, 6 unread, all on Yoni's account. None of the 6 are Interested — five are polite declines (wrong region/marketplace), and one (Claire Boggs, Tremendous) is an inbound vendor pitch, flagged as such rather than counted as real outreach backlog.

No automation touches LinkedIn replies yet — this is a manual-read view, same read-only posture as the rest of Phase 1. Logged in `connector-status.md` and its Notion twin as ✅ Connected, with the org-vs-workspace-key distinction noted for next time.

## n8n retired — 2026-08-26

Eikko's explicit instruction: n8n is no longer the automation platform for Albert Scott — not paused, not blocked-on-credentials, removed from consideration entirely. It never actually ran (the 2026-08-25 test-run failed on missing credentials, and those credentials were never created before this decision).

What this changes:
- This PRD's Plan step 5 ("daily-refresh Routine that re-reads live data and republishes") and the Constraints section's dependency on "the existing Albert Scott n8n workflow and its credentials" are both moot — there is no automation runtime behind this dashboard, and there isn't one planned yet either.
- Success criteria item ("A Claude Activity Log exists... populated from the same Google Sheet the n8n workflow already writes to") can't be met as written — the Sheet is unused since nothing ever wrote to it. The Command Center's Automation Log now tracks **manual review passes by Claude** instead (SmartLead +, as of today, LinkedIn/HeyReach), which is a real substitute for visibility but not the unattended automation the PRD originally scoped.
- `README - n8n Setup.md` and the two workflow JSON files in this folder are marked retired/historical, not deleted — they're an accurate record of what got built (51 nodes, both branches) in case a future automation platform decision wants to reuse the logic.
- Not addressed by this update: what (if anything) replaces n8n. No alternative platform has been chosen. Reply-triage for SmartLead and LinkedIn stays manual until that's decided.
