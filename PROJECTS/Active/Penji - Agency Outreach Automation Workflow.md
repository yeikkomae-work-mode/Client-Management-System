# Penji — Agency Outreach Automation Workflow (Design Doc)

Proposed automation for the Agency Advisor role. Goal: cut manual work out of the parts of the workflow that are pure data-moving (sourcing → filtering → enrichment → sequence loading → reply routing → logging) so time goes into research quality, messaging, and warm-reply conversations instead.

This mirrors the pattern already running for Chris Drew's `smartlead-pipedrive-automation` — same shape, different tools.

> **Updated 2026-08-18:** the role is confirmed **LinkedIn-only** (see `Penji - Sales Ecosystem & Team Standards.md`) — Lemlist/email is Jayvy's scope, not this pipeline's. Stage 5 below is now Dripify/HeyReach only. A real task for this exact automation is already logged in Eikko's Notion Task Tracker: **"Connect Dripify + Zapier + Claude"** (due 2026-08-18) — "will automate update activity on the leads to the google sheet." Treat that task as the live kickoff of Stage 5/7 below, not just a design exercise.

---

## Current Manual Workflow (confirmed 2026-08-18)

```
[New] Build LinkedIn account (AdsPower) → Source agency → ICP filter (marketing-only, no founders) →
Gojiberry enrich → post to Slack → 👍/👎 → load Dripify/HeyReach (RPS 7-touch script) →
manually copy Dripify activity into Google Sheet → monitor for warm reply →
route to Joan within 1hr / post to #response → log everything in Sheets
```

Every arrow above is a manual step today except the account pool build (AdsPower, semi-templated). Each one is a candidate for automation. **Constraint confirmed 2026-08-17 (Alan):** Gojiberry scraping and Dripify/HeyReach sending should never run simultaneously on the same account — any automated version of this pipeline needs to respect that as a hard sequencing rule, not just run stages in parallel for speed.

---

## Proposed Automated Pipeline

**Stage 0 — Account Pool (AdsPower, semi-automated)**
- Confirmed SOP as of Aug 18: new AdsPower profile → proxy from Sales and PR sheet → WebRTC "Replace" → warm-up browsing on US sites → sign in via Google (bypasses phone verification) → skip LinkedIn setup steps → update photo/banner/work email → 5 initial connection requests only
- Candidate for scripting the proxy-assignment and warm-up-browsing steps specifically; the actual LinkedIn sign-in and initial activity should probably stay manual/semi-manual given how sensitive this step is to detection
- Failure handling (mark for deletion, tag proxy as bad) could auto-update the Sales and PR sheet's "For Deletion" tab instead of manual moves

**Stage 1 — Sourcing (semi-automated)**
- Scheduled scraper/script pulls new listings from directories with public APIs or scrapeable structure (Clutch, Sortlist, GoodFirms) on a rotating weekly schedule
- Dedupes against the master Google Sheet automatically (match on domain)
- Output: raw candidate list appended to a "New — Unfiltered" tab

**Stage 2 — ICP Filter (automated)**
- Script applies the hard filters programmatically: employee count range, service-keyword match on scraped site copy, "no existing Penji subscription" cross-check against a client list
- Anything that passes moves to "ICP Confirmed"; anything borderline gets flagged for manual review rather than auto-rejected

**Stage 3 — Enrichment (automated via API)**
- Once Gojiberry access is confirmed, call its API directly for every ICP-confirmed record — pulls verified email, LinkedIn URL, phone
- Fallback waterfall (Hunter.io → Findymail) triggers automatically only if Gojiberry returns no verified email
- Fully enriched records write back to the Sheet with an "Enriched ✅" flag

**Stage 4 — Slack Verification (automated post, manual reaction)**
- Script posts each enriched agency to the designated Slack channel automatically (agency name, decision-maker, ICP tier, trigger signal if any)
- Your 👍/👎 reaction stays manual — this is the one human quality gate in the pipeline and shouldn't be automated away
- A listener picks up the reaction and updates the Sheet status automatically (no manual copy-paste)

**Stage 5 — Sequence Loading (automated on 👍) — this is the "Connect Dripify + Zapier + Claude" task**
- On 👍, script pushes the contact into the Dripify (or HeyReach) RPS 7-touch campaign via API/Zapier — LinkedIn-only, no Lemlist
- Respect the one-tool-at-a-time rule: this stage should not fire while Stage 3 (Gojiberry enrichment) is actively running on the same account
- This directly automates the currently-manual "copy Dripify activity into Google Sheet" step flagged in the training/onboarding notes

**Stage 6 — Reply Detection & Routing (automated)**
- Webhook listener on Dripify/HeyReach reply events (no Lemlist — LinkedIn-only role)
- Basic sentiment/keyword classification (positive / OOO / unsubscribe / negative) — auto-tags obvious cases, routes anything ambiguous to you for a manual call
- Positive replies auto-post to Slack tagging the sales channel immediately — removes the "route within the hour" as a manual task and makes it near-instant
- Sheet status updates automatically on every reply event

**Stage 7 — CRM/Sheet Logging (automated)**
- Every stage above writes its own timestamped log entry back to the tracking sheet automatically — this is the piece that's most error-prone when done manually and most valuable to automate first
- Weekly report (Friday) can be generated as a script that reads the Sheet and outputs the numbers required for the report format, rather than compiled by hand

---

## What Stays Manual (by design)

- The 👍/👎 ICP judgment call — this is the quality gate, not a bottleneck to remove
- Writing the actual `{{icebreaker}}` line per agency — this is what makes the first touch not-generic; automating it would violate the "never send a generic opening" non-negotiable
- Ambiguous reply classification and the actual conversation with a warm lead
- A/B test hypothesis design (the *running* of the test can be automated, the *thinking* shouldn't be)

---

## Build Order (suggested — lowest effort/highest value first)

1. **Stage 7 (Sheet logging)** — biggest error-reduction for least build effort, doesn't depend on any new account access
2. **Stage 6 (reply routing + Slack alert)** — directly protects the "1 hour" non-negotiable, high leverage
3. **Stage 4 (Slack post + reaction listener)** — removes copy-paste between Sheet and Slack
4. **Stage 5 (sequence loading on 👍)** — needs Lemlist + Dripify API access first
5. **Stage 3 (enrichment)** — needs Gojiberry API access first
6. **Stage 1–2 (sourcing + filtering)** — most complex, most valuable long-term, do last once the pipeline downstream is proven

---

## Blockers

- Gojiberry, Dripify, and HeyReach API/account access — Dripify personal-LinkedIn connection is done (Aug 17), but seat/API access still coming from Alan; Dripify is on a **free trial expiring 2026-08-24**
- Lemlist/Email Bison are **out of scope entirely** — confirmed Aug 17, Jayvy's domain, not this pipeline
- Confirm with Alan/Shekinah whether API access is something Eikko can request directly or needs to go through Penji's internal tooling/ops person
- Slack app/bot permissions needed in the dotpenji workspace for automated posting + reaction listening

---

**Status:** The "Connect Dripify + Zapier + Claude" task (Stage 5/7) is now a live, dated task in Eikko's tracker (due 2026-08-18) — this has moved from design-only to active. Recommend building it before the Dripify trial expires Aug 24.

**Last updated:** 2026-08-18
