# Penji — Agency Outreach Automation Workflow (Design Doc)

Proposed automation for the Agency Advisor role. Goal: cut manual work out of the parts of the workflow that are pure data-moving (sourcing → filtering → enrichment → sequence loading → reply routing → logging) so time goes into research quality, messaging, and warm-reply conversations instead.

This mirrors the pattern already running for Chris Drew's `smartlead-pipedrive-automation` — same shape, different tools.

---

## Current Manual Workflow (from training doc)

```
Source agency → ICP filter → find decision-maker → Gojiberry enrich →
post to Slack → 👍/👎 → load Lemlist + Dripify → monitor for warm reply →
route to Joan → log everything in Sheets/CRM
```

Every arrow above is a manual step today. Each one is a candidate for automation.

---

## Proposed Automated Pipeline

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

**Stage 5 — Sequence Loading (automated on 👍)**
- On 👍, script pushes the contact into the correct Lemlist campaign (selected by angle — capacity/margin/freelancer/white-label — based on the signal tag from Stage 1–3) via the Lemlist API
- Same trigger pushes the LinkedIn contact into the matching Dripify campaign
- Both loads happen within minutes of the reaction, not manually batched later

**Stage 6 — Reply Detection & Routing (automated)**
- Webhook listener on Lemlist + Dripify reply events
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

- Lemlist, Email Bison, and Gojiberry account/API access — not yet obtained (see `Penji - Agency Advisor Quick Reference.md`, Open Items)
- Confirm with Johnathan/Shekinah whether API access is something Eikko can request directly or needs to go through Penji's internal tooling/ops person
- Slack app/bot permissions needed in the dotpenji workspace for automated posting + reaction listening

---

**Status:** Design only — no code built yet. Recommend starting with Stage 7 once basic Sheet/Slack access is confirmed, independent of the blocked tool logins.

**Last updated:** 2026-08-13
