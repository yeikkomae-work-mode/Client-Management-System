# Master Task List — Cross-Client Rollup

**Built:** 2026-08-25 | **Owner:** Eikko | **Scope:** every active client, one page

This is the file that answers *"what's on my plate?"* across the whole roster. It is a
**rollup, not a source of truth** — every item below is copied from a per-client file and
cites it. Fix things in the source file; re-roll this one.

**Honesty rules this file is held to:**
- Every item traces to a real line in a real file. No item appears here that isn't written
  down somewhere else first.
- **Last touched** = the date the *source file* last recorded movement on that item, not
  today's date and not a guess.
- Where a client's tracking is thin or missing, that's written down as a **coverage gap**
  instead of leaving the section blank or inventing entries.
- `Top Acquisitions` is excluded — that engagement closed 2026-08-13 (not selected).

---

## Coverage — how trustworthy is each client's section below

| Client | Last EOD entry | Days silent (as of 2026-08-25) | Coverage |
|---|---|---|---|
| Penji | 2026-08-24 | 1 | ✅ Current, detailed |
| Chris Drew (Satlas) | 2026-08-22 | 3 | ✅ Current |
| Cüneyt (Starfix) | 2026-08-21 | 4 | ✅ Current |
| Yoni (Albert Scott) | 2026-08-19 | 6 | 🟡 Task list last updated Aug 18; EOD Aug 19 |
| Chris Caffera (Fractio + HPG) | 2026-08-14 | 11 | 🔴 **Gap Aug 15–24 self-flagged in the log** |
| Edward Lehner | 2026-08-12 | 13 | 🔴 One entry ever; offer deadline has since lapsed |
| Krishna | 2026-08-10 | 15 | 🔴 Log stops mid-August; one open blocker, unmoved |
| Chris Soriano | **never** | — | 🔴 **No real entry has ever been written** |

---

## ⚠️ Stale / blocked 3+ days

Rule used: the item is blocked on someone else, or its source file has recorded no movement
on it, for 3+ days as of 2026-08-25. Day counts are from the last-touched date shown.

- [ ] **Krishna — Philippines Silver Chain Retailers copy is finished but blocked on Krishna's sign-off** before leads upload / launch — `OUTPUT/End-of-Day Reports/Krishna - End of Day Log.md` (2026-08-10 entry, first raised 2026-08-07) — last touched **2026-08-10 · 15 days**
- [ ] **Chris Soriano — no tracking exists at all.** His EOD log is 100% unfilled template placeholders (`[DATE]`, `[Task 1]`) — `OUTPUT/End-of-Day Reports/Chris Soriano - End of Day Log.md` — last touched **never**
- [ ] **Chris Caffera — Aug 15–24 backfill.** The log itself flags the window as NOT LOGGED; the Aug 14 call's action items were never marked done or not-done — `OUTPUT/End-of-Day Reports/Chris Caffera - End of Day Log.md` (2026-08-15 → 2026-08-24 gap block) + `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` (🚨 Do First) — last touched **2026-08-24 · 1 day** *(the flag is fresh; the work behind it is 11 days cold)*
- [ ] **Chris Caffera — re-share the cleaned 920-name CPA spreadsheet in Slack #marketing.** Open since the Aug 7 call — `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` (Carried Forward) — last touched **2026-08-13 · 12 days**
- [ ] **Chris Caffera — Chris owes LinkedIn week-3 images/articles.** Chased Aug 13, still not delivered — same file (Chris's items still open from Aug 10) — last touched **2026-08-13 · 12 days**
- [ ] **Yoni — was the SmartLead API key pasted into chat during setup actually rotated?** Flagged as "Top open item," unanswerable from the repo, needs a direct SmartLead dashboard check. A live credential-exposure question — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §9 — last touched **2026-08-18 · 7 days**
- [ ] **Yoni — Aug 15 alert claiming 90% of 111 mailboxes blacklisted is still unverified.** Conflicts with SmartLead's own health check; the Aug 18 repo audit found no diagnosis committed anywhere — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §15 + Priority 0; `OUTPUT/End-of-Day Reports/Yoni - End of Day Log.md` (2026-08-18, "Still PENDING") — last touched **2026-08-18 · 7 days**
- [ ] **Yoni — ~54 blacklisted SmartLead mailboxes not confirmed removed/replaced.** Separate issue from the 90% alert; repo can't confirm because it's a dashboard action — needs a direct check with Yoni — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §14; Yoni EOD 2026-08-18 — last touched **2026-08-18 · 7 days**
- [ ] **Chris Drew — Hillary — Finance Broker and Referral Finance Campaign have sat unlaunched since Aug 10,** "reason/timeline TBD, confirm with Eikko next session"; no resolution in any later entry — `OUTPUT/End-of-Day Reports/Chris Drew - End of Day Log.md` (2026-08-10) — last touched **2026-08-10 · 15 days**
- [ ] **Chris Drew — Capital Financing–Trades sequence still on the old subject-line format** (time-greeting in subject) vs. the corrected v3 doc; flagged for a fix pass Aug 12, not mentioned as fixed since — `OUTPUT/End-of-Day Reports/Chris Drew - End of Day Log.md` (2026-08-12) — last touched **2026-08-12 · 13 days**
- [ ] **Yoni — `PROJECTS/Active/ACTION-PLAN-UNCATEGORIZED-MESSAGES.md` and `PROJECTS/Active/YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md` both still "ON HOLD — Awaiting Rachel's action"** with no update since creation — `PROJECTS/Active/ACTION-PLAN-UNCATEGORIZED-MESSAGES.md`, `PROJECTS/Active/YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md` — last touched **2026-08-05 · 20 days**
- [ ] **Penji — Advisor Job Training Test (quiz) still outstanding.** Open since Aug 17, restated Aug 18 and Aug 24 — `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md` (2026-08-24 Next Steps) — last touched **2026-08-24 · 1 day** *(restated, not progressed, for 8 days)*
- [ ] **Chris Caffera — HPG workstream checkboxes are all unknown.** The file is built from a **2026-06-17** dashboard snapshot; completion state lived in browser `localStorage` and did not sync — `PROJECTS/Active/CHRIS-CAFFERA-HPG-WORKSTREAM.md` (⚠️ Staleness flag) — last touched **2026-06-17 · 69 days**

---

## ⏰ Hard deadlines

Dated commitments only — no "soon", no inferred urgency.

- 🔴 **LAPSED — Edward Lehner: Upwork offer expired 2026-08-19.** Sent Aug 12, pending acceptance, 5 hrs/wk at $5/hr. Nothing in any file records whether he accepted before it expired — `OUTPUT/End-of-Day Reports/Edward Lehner - End of Day Log.md` (2026-08-12); `CLIENT PROFILES/Important info.md` (Edward Lehner block) — last touched **2026-08-12**
- 🔴 **LAPSED/UNCONFIRMED — Penji: Dripify free trial expired 2026-08-24.** "Needs the paid seat/upgrade confirmed with Alan Walker today or outreach stops." No confirmation logged — `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md` (2026-08-24 Notes + Next Steps) — last touched **2026-08-24**
- 🔴 **OVERDUE — Chris Caffera: Apollo credit export before the $59/mo downgrade.** The Aug 14 call set "by Monday" (Aug 17); the Aug 24 task list still carries it as "Time-sensitive / irreversible if credits expire" with ~1,500 credits at stake — `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` (🚨 Do First); `OUTPUT/End-of-Day Reports/Chris Caffera - End of Day Log.md` (2026-08-14) — last touched **2026-08-24**
- 🟡 **2026-09-01 — Penji: 50 US-based LinkedIn accounts target** (39/50 built as of Aug 17). Team-level target, not solely Eikko's, but it gates the outreach scale-up — `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md` (2026-08-17) — last touched **2026-08-17**
- 🟡 **2026-09-28 — Cüneyt: sellervate.net domain renewal due,** confirmed not yet renewed as of the Aug 16 recheck — `OUTPUT/End-of-Day Reports/Cüneyt - End of Day Log (Starfix).md` (2026-08-16) — last touched **2026-08-16**
- ⚪ **~2026-11-09 — Penji: 90-day probation ends** (from the Aug 11 contract date); PTO accrual starts after — `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md` (2026-08-24 Notes) — last touched **2026-08-24**

---

## Yoni (Albert Scott) — last EOD entry 2026-08-19

Full detail lives in `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` (555 lines, 16 workstreams,
last updated 2026-08-18). Only the critical/near-term open items are rolled up here.

**Critical**
- [ ] Verify the Aug 15 alert claiming 90% of 111 mailboxes are blacklisted (conflicts with SmartLead's own health check) — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §Priority 0 — 2026-08-18
- [ ] Remove ~54 blacklisted SmartLead mailboxes from all campaigns, cancel, purchase replacements — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §14 — 2026-08-18
- [ ] Update Toy Fair Q4X to use only non-blacklisted inboxes — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §Priority 0 — 2026-08-18
- [ ] Resolve the 20 remaining SmartLead warmup-blocked mailboxes — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §0 — 2026-08-18
- [ ] Confirm whether the chat-pasted SmartLead API key was rotated — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §9 — 2026-08-18
- [ ] Send the new SmartLead API key to Shimi so he can fix the broken connector on Yoni's Claude account — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §9 — 2026-08-18

**High — from the Aug 19 calls (all 11 logged as Notion Task Tracker rows, status "Not started")**
- [ ] Increase the cloud token limit by $50 — unblocks Amazon seller scraping — `OUTPUT/End-of-Day Reports/Yoni - End of Day Log.md` (2026-08-19) — 2026-08-19
- [ ] Test alternative scraping tools on a 1,000-seller sample (current capture rate ~2–2.3% vs. a 50% target) — same — 2026-08-19
- [ ] Compare HeyReach ($80/mo) / LinkHelper (~$16.50/mo) / Dupify and set up the winner — same — 2026-08-19
- [ ] Email Yoni the scraping-cost summary — same — 2026-08-19
- [ ] Rebuild the SEO/GEO Claude project for albertscott.com from scratch (recommendations-only, no auto-implementation) and request tool access — same — 2026-08-19
- [ ] Enhance the "Overdue Pipedrive Activities" artifact (SmartLead/Gmail context, CC'd leads, Yoni-only filter) — same — 2026-08-19
- [ ] Refine the "Outbound Command Center" dashboard (daily refresh, Blue Dot filter, all campaigns >5% bounce, Lead Categorizations box) — same — 2026-08-19
- [ ] Schedule the SEO strategy follow-up meeting — same — 2026-08-19

**Open from the Aug 18 repo audit**
- [ ] Build the LinkedIn brand-contact targeting flow (§15a) — no repo evidence at all — `OUTPUT/End-of-Day Reports/Yoni - End of Day Log.md` (2026-08-18) — 2026-08-18
- [ ] Apify integration is barely started — only an `APIFY_TOKEN` placeholder committed; no scraper, no seller-sample test, no report — same — 2026-08-18
- [ ] Sync the changed domain-blocking rule into our own docs: Out-of-Office **and** Wrong-Person replies are no longer domain-blocked at all (broader than the currently documented rule) → update `RESOURCES/Workflows/Smartlead-Pipedrive-Automation-Workflow.md` — same — 2026-08-18
- [ ] Reconcile "Master lead list organization — paused" against the extensive export/dedupe tooling Yoni actually built Aug 13–17 — `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §Priority 2a — 2026-08-18
- [ ] Build the 4 new lead campaigns (Fancy Foods → Winter Fancy Fair → Sweets & Snacks → Expo West). Prep is complete and documented; execution was moved to Yoni's own Claude account Aug 14 — confirm it happened — `OUTPUT/End-of-Day Reports/Yoni - End of Day Log.md` (2026-08-14 Additional Work) — 2026-08-19 *(Sweets & Snacks / Winter Fancy Fair / Fancy Foods reported launched or running in the Aug 19 recap; Toy Fair resumed without lead updates)*
- [ ] Resolve the Formex Expo exhibitor-list access blocker — `OUTPUT/End-of-Day Reports/Yoni - End of Day Log.md` (2026-08-19, low priority) — 2026-08-19

**Stalled**
- [ ] Uncategorized-messages resolution — assigned to Rachel Safra, ON HOLD since Aug 5, no timeline — `PROJECTS/Active/ACTION-PLAN-UNCATEGORIZED-MESSAGES.md` — 2026-08-05

---

## Chris Caffera (Fractio + HivePoint Group) — last EOD entry 2026-08-14

> **🔴 Coverage gap.** The EOD log carries an explicit "2026-08-15 → 2026-08-24 — ⚠️ NOT LOGGED"
> block: no entries exist for that window, and campaign metrics stop at Aug 13. Every item below
> is at its **last-known state, not a verified current state** — the Aug 24 task list says so in
> its own header. Do not treat any of it as open *or* closed until Eikko backfills.

**Do first**
- [ ] Backfill the Aug 15–24 gap — `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` (🚨 Do First) — 2026-08-24
- [ ] Export remaining ~1.5k Apollo credits (fractionals + project consultants, excl. MSPs), then confirm the plan moved to $59/mo — time-sensitive, irreversible if credits expire — same — 2026-08-24

**From the Aug 14 call (Eikko's items)**
- [ ] Email Chris the 1,200 + 920 CPA/accountant lists (Apollo + MillionVerifier) — `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` — 2026-08-24
- [ ] Restore SharePoint access; upload the CPA/accountant lists — same — 2026-08-24
- [ ] Draft Reddit posts in Chris's voice and post in the Reddit chat (see the `reddit-playbook` skill) — same — 2026-08-24

**Carried forward from Aug 10**
- [ ] Re-share the cleaned 920-name CPA spreadsheet in Slack #marketing — same — 2026-08-13
- [ ] Send Chris the raw/other Apollo export file — same — 2026-08-24
- [ ] Once the "News Release: CTRO" campaigns finish, turn off `fatin@` and activate `growth@mailfractio.co` as the 5th cold-outbound mailbox (3 of 4 still running as of Aug 13) — same — 2026-08-24
- [ ] Manually research consultants/fractionals/advisors — on hold; overlaps the Aug 14 Apollo export task, reconcile the two — same — 2026-08-24
- [ ] Laptop price quote — 3rd-party Apple reseller, 3-year payment plan — same — 2026-08-24
- [ ] Draft 3 fractional one-pager templates (no pricing, no healthcare), then Eikko's own — same — 2026-08-24
- [ ] Draft LinkedIn post(s) advocating Chris / the fractional offering — Chris reviews before scheduling — same — 2026-08-24

**Fatin's Q3 sequence review (open since Aug 13)**
- [ ] Review Drive folder Parts 0–5, especially Part 5 (sender rotation) and Part 3 (the 56 messages), before go-live — same — 2026-08-24
- [ ] Schedule the sync with Fatin to walk through sender rotation — same — 2026-08-24
- [ ] Resolve `growth@` activation — blocks the full C-ENT round-robin as designed — same — 2026-08-24
- [ ] Flag redlines on specific emails/LinkedIn touches back to Fatin — same — 2026-08-24

**Waiting on Chris (tracking only)**
- [ ] Chris: send LinkedIn week-3 images/articles — chased Aug 13, still not delivered — same — 2026-08-13
- [ ] Chris: call the Lemlist clicks/opens list (447); email Joe re: token add-on billing copy; schedule Eikko's next pay + pre-fund; contact Apollo support re: cancel/renew to $59/mo — same — 2026-08-24

**HivePoint Group workstream**
- [ ] Status pass on the whole HPG file — built from a 2026-06-17 dashboard snapshot, all checkboxes unknown — `PROJECTS/Active/CHRIS-CAFFERA-HPG-WORKSTREAM.md` — 2026-06-17
- [ ] Scope the HivePoint pivot (sell $79–$179/mo HivePoint plans to fractionals) with Chris — no tasks assigned yet — `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-AUG24.md` — 2026-08-24

---

## Chris Drew (Satlas) — last EOD entry 2026-08-22

- [ ] **Decide: cancel or attempt recovery on the 10 Zapmail domains.** As-is they are not sending-safe — 30 mailboxes all `isWarmedUp: false`, domain health 22.65/100, all on CloudNS (matches the original SURBL blacklist issue). Open decision for Chris/Eikko — `OUTPUT/End-of-Day Reports/Chris Drew - End of Day Log.md` (2026-08-22) — 2026-08-22
- [ ] Address 6 PlusVibe mailboxes with bounce rate >5% (worst: tremaynec@satlasmail.com at 20%) — same — 2026-08-22
- [ ] Address 2 mailboxes with 7-day warmup health <90% (tremayne.c@satlaszone.com 83.3%, tremayne.c@satlasplus.com 89.3%) — same — 2026-08-22
- [ ] 30-day reply rate is 0.66% (2,588 sent / 17 replied) against a 2% target — needs a response plan — same — 2026-08-22
- [ ] Launch or formally shelve **Hillary — Finance Broker** and **Referral Finance Campaign** — held back since Aug 10, reason/timeline still TBD — `OUTPUT/End-of-Day Reports/Chris Drew - End of Day Log.md` (2026-08-10) — 2026-08-10
- [ ] Fix the Capital Financing–Trades sequence subject-line format in PlusVibe (still the old time-greeting-in-subject format vs. corrected v3) — same log (2026-08-12) — 2026-08-12
- [ ] Capital Financing – Logistics and Labour Hire sequences still have no content in PlusVibe (Apollo lists only) — same (2026-08-12) — 2026-08-12
- [ ] Scope the "commercial finance brokers" angle Tremayne flagged as inbound interest — scope not yet defined — same (2026-08-12) — 2026-08-12
- [ ] Relay the Ally capacity options to Chris and get a decision: (1) launch Specialist Mortgage/Investment now on the 30 free Zapmail mailboxes, (2) hold Commercial/Asset Finance Brokers until more capacity, (3) pull mailboxes off the 7 active campaigns — **option 3 needs Chris's sign-off, not unilateral** — same (2026-08-13) — 2026-08-13
- [ ] Send the drafted Slack reply to Chris/Ally covering filters, TAM per audience, and ICP alignment — drafted Aug 13, **not sent** (no Slack connector authorized) — same (2026-08-13) — 2026-08-13
- [ ] Re-sync the PlusVibe campaign tracker artifacts and the shared "Satlas Campaign Tracker" Google Sheet — neither auto-refreshes; both are manual until the MCP connector points at the Satlas account — same (2026-08-12) — 2026-08-12

---

## Cüneyt (Starfix) — last EOD entry 2026-08-21 · trial engagement

- [ ] Get Cüneyt's sign-off on **Sequence B** (product-category angle for the UK/USA Seller list) before building it in Instantly — `OUTPUT/End-of-Day Reports/Cüneyt - End of Day Log (Starfix).md` (2026-08-21 Open items) — 2026-08-21
- [ ] Decide whether to fold in the leftover **SellerVeta Database** file (same schema as UK/USA Seller, left out of the Aug 21 cleaning request) — same — 2026-08-21
- [ ] Remove the 2 cross-file duplicate leads (`philip@palladiobeauty.com`, `prudence@beautybyearth.com`) from UK/USA Seller before upload — flagged, not auto-removed — same — 2026-08-21
- [ ] Once approved, build both sequences into Instantly against their cleaned lists — same — 2026-08-21
- [ ] Share the two Aug 20 sequence versions with Cüneyt (realistic vs. full-vision) and get his call on launching now vs. investing in a per-lead negative-review audit step — same (2026-08-20) — 2026-08-20
- [ ] **Rebuild every campaign from scratch** — audit each one's copy, settings, and assigned mailboxes first. Decision locked in Aug 16; all campaigns are paused (0 Active in Instantly) — same (2026-08-16) — 2026-08-16
- [ ] Create 2 replacement mailboxes on hellostarfix.com using the 2 freed seats (no purchase needed — confirmed live in Hostinger); suggested kevin@ and ryan@ — same (2026-08-19) — 2026-08-19
- [ ] Add maximilian@sellervate.net to Instantly — Active in Hostinger, never added, unused capacity — same (2026-08-16) — 2026-08-16
- [ ] Get an answer on whether Cüneyt still needs to review campaign copy before launch — asked Aug 19, no answer in the thread — same (2026-08-19) — 2026-08-19
- [ ] Verify what happened to "UK Seller (starfix)" / "USA Seller" (top performers in the Aug 13 audit) before the rebuild — the "Seller" tag returns 0 campaigns, suggesting a rename, not confirmed — same (2026-08-16) — 2026-08-16
- [ ] Confirm with Cüneyt which is accurate: the Google Sheet marks 2 of the 4 campaigns "Active", but they're still Draft in Instantly — same (2026-08-16) — 2026-08-16
- [ ] Renew sellervate.net (due 2026-09-28) — same (2026-08-16) — 2026-08-16
- [ ] Confirm the 50% upfront week-1 payment landed via Wise, and determine the exact hour count so far — Cüneyt asked to be notified at the 10-hour mark — same (2026-08-14) — 2026-08-14
- [ ] Isolate the emails in "Amazon USA Product Review" (735 leads, emails only in Sheet 1) so it becomes launchable; "UK & USA Amazon Brand Leads" (640) has no emails at all and is not launchable as-is — same (2026-08-19) — 2026-08-19

---

## Penji — last EOD entry 2026-08-24

- [ ] **Confirm the Dripify paid seat with Alan Walker** — free trial expired 2026-08-24; outreach stops without it — `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md` (2026-08-24) — 2026-08-24
- [ ] Ask Shekinah/Johnathan which title is operative for reporting: "LinkedIn Outreach Specialist" (offer letter) or "Agency Advisor" (Notion training + local docs) — same — 2026-08-24
- [ ] Complete the **Advisor Job Training Test** quiz — outstanding since Aug 17 — same — 2026-08-24
- [ ] Reconcile the 7-touch RPS script actually running against the documented 2-touch cap in the Sales Team Standards doc — needs a direct confirmation from Shekinah — same (2026-08-18) — 2026-08-24
- [ ] Confirm whether the Amanda Scott follow-up (meeting link owed to Hudson/Shane) was ever sent — the Aug 19 email promised one and none was included — same — 2026-08-24
- [ ] Get Shekinah's ruling on whether "max 2 touches" means 2 messages total or includes the invite note (trimmed to the safer reading, not confirmed) — same (2026-08-17) — 2026-08-17
- [ ] Split the 321-lead Dripify list into Founder/CEO/Owner vs. Director/VP/Creative-Director segments with different angles — offered, not yet done — same (2026-08-17) — 2026-08-17
- [ ] Verify the garbled names from the Fathom auto-summary ("Heerich/Gojiberry/Glitify", a LinkedIn profile "under Benji") with Alan/Shekinah before acting on them — same (2026-08-17) — 2026-08-17

**⚠️ Contradictions raised 2026-08-24 — surfaced, not overwritten, and still unresolved**
- [ ] **Rate framing:** local files say "$350/month retainer"; the signed document is a full-time *employment* contract (at-will, 90-day probation, PTO accrual, 3-year non-compete) at "Starting Salary: $350". Same number, materially different relationship — same — 2026-08-24
- [ ] **Hours vs. capacity:** the offer letter schedule is 8am–5pm with a 12–1pm break — a full 8-hour day, with §7 requiring being online at shift time. Reconcile against Cüneyt / Yoni / Chris Drew before committing further hours elsewhere — same — 2026-08-24
- [ ] **Non-compete:** §12 bars working "in the same or similar business as Penji" for 3 years post-termination and requires disclosure of related-industry employers. Penji is a design-subscription company but the clause is broad — worth reading closely given the rest of the roster is cold email / lead gen — same — 2026-08-24

---

## Krishna — last EOD entry 2026-08-10 🔴

> **Coverage gap.** The log stops at 2026-08-10 — 15 days silent. The engagement is documented
> as light and irregular (3 hrs/week, `CLIENT PROFILES/Important info.md`), so silence may be
> normal rather than a broken tracker — but the one open blocker below has not moved either way.

- [ ] **Philippines Silver Chain Retailers — copy is finished, blocked on Krishna's sign-off** before uploading leads and launching. First raised Aug 7, still blocked at the Aug 10 entry — `OUTPUT/End-of-Day Reports/Krishna - End of Day Log.md` (2026-08-10) — 2026-08-10
- [ ] Watch the Peru Silver Chain Wholesalers bounce rate (8.3%, above the healthy threshold) — possible list-quality issue; consider verifying the remaining unsent leads — same (2026-08-07) — 2026-08-07
- [ ] Review which variant drove the 2 replies on the US Silver Chain Retailers Sample Run (12.5%, best of the three) before finalizing Philippines/future-region copy — same (2026-08-07) — 2026-08-07

---

## Chris Soriano — no EOD entry has ever been written 🔴

> **Coverage gap — this is the whole section.** `OUTPUT/End-of-Day Reports/Chris Soriano - End of Day Log.md`
> contains nothing but unfilled template placeholders (`[DATE]`, `[Task 1]`, `[PREVIOUS DATE]`).
> No task, date, or metric has ever been recorded. `CLIENT PROFILES/Important info.md` describes
> the engagement as "as-needed", "very sporadic; waits for task assignments" — so an empty log is
> consistent with no work having been assigned, **not** proof that work is being missed.
> Either way, this file cannot answer "what's on his plate," and nothing can be rolled up from it.

- [ ] Decide whether Chris Soriano is an active engagement. If yes, the log needs a first real entry; if no, move him out of the active roster — `OUTPUT/End-of-Day Reports/Chris Soriano - End of Day Log.md` + `CLIENT PROFILES/Important info.md` — no entry on file

---

## Edward Lehner — last EOD entry 2026-08-12 🔴

> **Coverage gap.** One entry ever (the Aug 12 kickoff). The Upwork offer that the engagement
> depends on expired **2026-08-19** and no file records the outcome.

- [ ] **Establish whether the Upwork offer was accepted before it expired on 2026-08-19.** Everything else about this engagement is contingent on it — `OUTPUT/End-of-Day Reports/Edward Lehner - End of Day Log.md` (2026-08-12); `CLIENT PROFILES/Important info.md` — 2026-08-12
- [ ] Set the recurring session schedule — first session Aug 12, recurring cadence still TBD — `CLIENT PROFILES/Important info.md` (Edward Lehner block) — 2026-08-12
- [ ] Fix the Upwork listing category mismatch — the offer is filed under "Graphic Design" but the role is talk-through/focus partner — same — 2026-08-12

---

## Working hours (timing context for the above)

From `CLIENT PROFILES/Important info.md` — note this file's own header says **last updated 2026-08-05**,
and several of its per-client rate blocks still read "(TBD)" even where a rate is confirmed elsewhere.

| Client | Working hours (PHT) | Commitment |
|---|---|---|
| Yoni (Albert Scott) | 9pm–5am, weekdays, 1hr break 11pm–12am | 5 hrs/day |
| Chris Caffera | 2pm–11pm | $7/hr, 20 hrs/week |
| Chris Drew (Satlas) | as-needed (urgent only) | $200 AUD/month flat |
| Krishna | as-needed | 3 hrs/week |
| Chris Soriano | as-needed | project-based |
| Edward Lehner | scheduled Zoom sessions | 5 hrs/week cap |
| Cüneyt (Starfix) | as-needed (WhatsApp) | 20h trial @ $7/hr |
| Penji | 8am–5pm, 12–1pm break *(per the offer letter — conflicts with part-time framing, see Penji section)* | full-time per contract |

---

## Not included

- **Top Acquisitions** — engagement closed 2026-08-13, not selected. Excluded by design. Historical record: `OUTPUT/End-of-Day Reports/Top Acquisitions - End of Day Log.md`.
- **Yoni's full 16-workstream backlog** — only critical and near-term items are rolled up here; `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` is the complete list.
- **Anything not written down in a source file.** If it's only in a chat, it isn't here.
