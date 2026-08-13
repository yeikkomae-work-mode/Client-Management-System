# CAMPAIGN METRICS — Lemlist (Chris Caffera / Fractio)
**Report date:** 2026-08-13
**Source:** `campaigns-export.csv` (Lemlist campaign-level export, uploaded by Eikko)
**Requested by:** Chris — needed to build a ~100-lead call list for next week's phone campaign (per Aug 12 impromptu call)

---

## CAMPAIGN DETAILS

| Field | Value |
|-------|-------|
| **Client** | Chris Caffera / Fractio |
| **Tool** | Lemlist |
| **Campaigns in this export** | 4 ("News Release: CTRO" series) |
| **Current phase** | 1 ended, 3 running |

---

## KEY METRICS — PER CAMPAIGN

| Campaign | Sent | Not Bounced | Opens | Open % | Clicks | Click % | Replies | Reply % | Bounces | Bounce % | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CTRO - Fractio Deals | 264 | 245 | 112 | 45.7% | 9 | 3.7% | 1 | 0.4% | 19 | 7.2% | Ended |
| CTRO - Fractio LinkedIn Page Followers | 489 | 458 | 154 | 33.6% | 58 | 12.7% | 0 | 0.0% | 31 | 6.3% | Running |
| CTRO - Fractio Podcast Attendees | 129 | 116 | 38 | 32.8% | 22 | 19.0% | 0 | 0.0% | 13 | 10.1% | Running |
| CTRO - Fractio Content Offer Consumed | 378 | 359 | 143 | 39.8% | 28 | 7.8% | 3 | 0.8% | 19 | 5.0% | Running |
| **Combined total** | **1,260** | **1,178** | **447** | **37.9%** | **117** | **9.9%** | **4** | **0.3%** | **82** | **6.5%** | — |

*No target benchmarks were provided for these campaigns — marking "on track / behind" as not available. Let me know if Chris has a target open/reply rate and I'll re-run this against it.*

---

## PERFORMANCE ANALYSIS

**What's working:**
- **Podcast Attendees** has by far the best click-to-open rate (57.9% — 22 of 38 openers clicked), suggesting this audience is the most warmed-up/engaged segment despite the smallest volume.
- **LinkedIn Page Followers** has strong click volume (58 clicks, 12.7% click rate) — this list is engaging with content even though replies are at zero.
- Combined open rate (37.9%) is healthy for cold/warm B2B outreach.

**What's not:**
- **Replies are almost nonexistent** — only 4 replies across 1,260 sends (0.3%). Two of the four running campaigns have zero replies despite meaningful open/click activity — opens and clicks aren't converting to conversation.
- **Podcast Attendees bounce rate is 10.1%** — notably higher than the other three campaigns (5–7%) and above typical cold-email hygiene thresholds (~2–3%). Worth checking list quality/verification on this segment specifically before sending more from it.
- **CTRO - Fractio Deals** is marked "ended" with only 1 reply from 245 delivered — lowest-performing campaign in the set relative to its size.

**Hypothesis for changes:**
- High opens/clicks with near-zero replies suggests the CTA or follow-up cadence isn't prompting a response — worth reviewing whether there's a clear next step in the email copy, or whether these leads need a different channel (e.g., the phone campaign Chris wants) rather than more email.
- The Podcast Attendees bounce rate warrants a quick check on how that list was sourced/verified.

---

## ~100-LEAD CALL LIST — DONE (Aug 13)

Built from the 4 lead-level Lemlist exports Eikko uploaded. Filtered to leads with `lastState` in (opened, clicked, replied) **AND** a phone or mobile number on file, sorted by engagement priority (replied → clicked → opened).

| Stage | Count |
|---|---|
| Total engaged leads across all 4 campaigns (opened/clicked/replied) | 251 |
| ...of which have a phone/mobile number on file | **106** |
| Replied (highest priority) | 2 |
| Clicked | 8 |
| Opened | 96 |

**Note on scope:** phone number coverage, not engagement volume, is the binding constraint — 251 leads engaged, but only 106 have any phone number in the CRM data. The call list is effectively "all callable engaged leads," not a top-100 cut of a larger pool. Podcast Attendees and LinkedIn Page Followers have almost no phone data (0 and 4 respectively) — worth flagging to Chris/Fatin if phone capture should be added to those forms going forward.

**Deliverable:** `Chris Caffera - Phone Call List (Top 106 Engaged Leads) - Aug 13.csv` — columns: campaign, engagement type, name, email, phone, job title, company. Sorted so Chris can start at the top (the 2 repliers) and work down.

---

## NEXT STEPS

- [ ] Get lead-level engagement export from Lemlist (or Lemlist login access) to build the actual ~100-lead call list — **Owner: Eikko — Due: before next week's phone campaign**
- [ ] Flag Podcast Attendees' 10.1% bounce rate to Chris/Fatin — check list source/verification
- [ ] Ask Chris whether there's a target open/reply rate benchmark for these campaigns
- [ ] Consider: near-zero reply rate across 1,260 sends may mean these leads are better suited to the phone follow-up than continued email
