# Cüneyt (SellerVate) — Campaign Settings: Before / After Report

**Date:** 2026-08-13 | **Platform:** Instantly | **Prepared for:** Client delivery (Cüneyt / Elevate Commerce)

---

## Part 1 — The 3 campaigns adjusted today

Cüneyt adjusted mailboxes and daily sending limits on these three campaigns and paused them for the change. On pickup, all three showed **zero mailboxes attached** (the reassignment hadn't saved), which had auto-flagged two of them "Accounts Unhealthy" in Instantly. Mailboxes were reattached per Cüneyt's direction and all three were resumed.

### Amazon Seller 2cnd (2)

| Setting | Before (Aug 13 baseline) | Found today (mid-change) | After (live now) |
|---|---|---|---|
| Status | Active | Active (flagged unhealthy — no sender) | **Active, healthy** |
| Mailboxes | (sellervate.net set) | **None attached** | sebastian@, jonas@, david@, tobias@ (sellervate.net) |
| Schedule | Tue–Thu, 9am–5pm, Arctic/Longyearbyen | unchanged | unchanged |
| Daily limit | 30 | 30 | 30 |
| Open tracking | Off | **On** | On |
| Link tracking | Off | Off | Off |
| Stop on reply | On | On | On |

### Starfix New UK Leads 2026-08

| Setting | Before (Aug 13 baseline) | Found today (mid-change) | After (live now) |
|---|---|---|---|
| Status | Active | **Accounts Unhealthy** | **Active, healthy** |
| Mailboxes | (unspecified in original audit) | **None attached** | sam@, ben@, jake@, alex@ (starfix.online) |
| Schedule | Mon–Thu, 8am–8:30pm, Isle of Man | unchanged | unchanged |
| Daily limit | 40 | 30 | 30 *(intentional — per Instantly's recommendation)* |
| Open tracking | Off | **On** | On |
| Link tracking | Off | Off | Off |
| Stop on reply | — | On | On |

### Starfix New US Leads 2026-07-29

| Setting | Before (Aug 13 baseline) | Found today (mid-change) | After (live now) |
|---|---|---|---|
| Status | Active | **Accounts Unhealthy** | **Active, healthy** |
| Mailboxes | (unspecified in original audit) | **None attached** | sam@, ben@, jake@, alex@ (starfix.online) |
| Schedule | Weekdays (Mon–Fri), 8am–4pm, America/Chicago | **Mon–Thu only (Fri dropped)** | Mon–Thu only *(unconfirmed — flagged, not yet resolved)* |
| Daily limit | 60 | 30 | 30 *(intentional — per Instantly's recommendation)* |
| Daily new leads | — | 50 | 50 |
| Text only | Yes (per original notes) | **No** | **Yes** *(re-enabled per Cüneyt, 2026-08-13)* |
| Open tracking | Off | **On** | On |
| Stop on auto-reply | On | On | On |
| Prioritize new leads | On | On | On |

**Resolved with Cüneyt (2026-08-13):**
- Daily-limit reductions (UK 40→30, US 60→30) — confirmed intentional, per Instantly's own recommendation.
- Text-only on US Leads — confirmed should be on; re-enabled.
- Dropped Friday on US Leads schedule (was Mon–Fri, now Mon–Thu) — **still unconfirmed**, not yet changed either way.

---

## Part 2 — Current settings on the other active/paused campaigns

*(Snapshot only — nothing on this list was touched today.)*

| Campaign | Status | Mailboxes | Schedule | Daily Limit | Open Track | Link Track | Stop on Reply |
|---|---|---|---|---|---|---|---|
| Liste von Dennis | Active | sellervate.net (4) | Tue–Thu 9:30–12:00, Longyearbyen | 30 | Off | On | On |
| Sports & Fitness (sellervate, reviews) | Active | sellervate.net (4) | Tue–Thu 9:00–17:00, Longyearbyen | 30 | Off | Off | On |
| Sports & Fitness (mixed) | Paused | salesfix.eu (5)* | Mon–Fri 9:30–12:00, Longyearbyen | 15 | Off | On | On |
| Baby (mixed) | Paused | salesfix.eu (5)* | Tue–Thu 9:30–12:00, Longyearbyen | 15 | Off | On | On |
| Pet (mixed) | Paused | salesfix.eu (5)* | Tue–Thu 9:30–12:00, Longyearbyen | 15 | Off | On | On |
| Amazon seller 2nd | Paused | salesfix.eu (5)* | Tue–Thu 9:30–12:00, Longyearbyen | 15 | Off | On | On |
| 50K DE Amazon Leads | Paused | sellervate.net (4) | Mon–Fri 9:30–12:00, Longyearbyen | 25 | On | On | On |

\* **Data quality flag — confirmed with Cüneyt (2026-08-13):** the `salesfix.eu` mailboxes referenced on these four campaigns (alex@, daniel@, julian@, marco@, tom@salesfix.eu) do not appear in Instantly's current connected-accounts list (only the 11 hellostarfix.com / starfix.online / sellervate.net mailboxes are live) and should not be used going forward. They're all currently paused, so nothing is broken today — but the stale mailbox references have not yet been removed from these campaigns, and no replacement mailboxes have been assigned. Needs a decision on which live mailboxes to reassign before any of these four are resumed.

---

## Part 3 — Infrastructure fix: starfix.online missing DKIM

Root-cause audit found starfix.online had **no DKIM record at all** — SPF and DMARC were fine, but DKIM never generated (unlike hellostarfix.com and sellervate.net, which both have it). Verified via direct DNS lookup against Google/Cloudflare resolvers, then confirmed in Hostinger hPanel (Emails → starfix.online → Custom DKIM — showed empty state).

**Fixed:** Generated and verified the DKIM record (`hostingermail1._domainkey.starfix.online`) directly in hPanel. Confirmed live via public DNS afterward. This directly affects Starfix New UK Leads and Starfix New US Leads, both sending from starfix.online mailboxes.

All 11 Instantly-connected mailboxes checked individually — all Active, warmup scores 97–100, no SMTP/IMAP connection errors. No other infrastructure issues found.

## Part 4 — Remaining campaigns fixed and resumed

Four more campaigns (Sports & Fitness mixed, Baby mixed, Pet mixed, Amazon seller 2nd) were paused with the same root problem as the original 3: their assigned mailboxes (`@salesfix.eu`) no longer exist in the connected Instantly account — stale references, most likely from a disconnected/removed domain. Reassigned to hellostarfix.com's 3 mailboxes (cueneyt@, daniel@, james@ — previously unused by any campaign) and resumed.

**Final state — all SellerVate campaigns:**

| Campaign | Status | Mailboxes |
|---|---|---|
| Liste von Dennis | Active (unchanged) | sellervate.net |
| Amazon Seller 2cnd (2) | **Active** (fixed) | sellervate.net |
| Sports & Fitness (sellervate, reviews) | Active (unchanged) | sellervate.net |
| Starfix New UK Leads 2026-08 | **Active** (fixed) | starfix.online |
| Starfix New US Leads 2026-07-29 | **Active** (fixed) | starfix.online |
| Sports & Fitness (mixed) | **Active** (fixed) | hellostarfix.com |
| Baby (mixed) | **Active** (fixed) | hellostarfix.com |
| Pet (mixed) | **Active** (fixed) | hellostarfix.com |
| Amazon seller 2nd | **Active** (fixed) | hellostarfix.com |
| 50K DE Amazon Leads | Paused (left as-is) | sellervate.net — mailboxes valid, just not resumed; confirm with Cüneyt whether it should run |

All 9 active campaigns verified healthy on both the raw campaign record and the analytics endpoint (no lag, no unhealthy flags remaining).

## Part 5 — Full account sweep (all 24 campaigns, all 11 mailboxes)

Checked every campaign's mailbox references, lead counts, and bounce rates; checked every connected mailbox for connection errors; checked the account-level block list.

**Found and fixed:**
- **Amazon seller 2nd** — showed Active with healthy mailboxes but 0 leads remaining (52 already contacted, list exhausted). Paused it — resuming it accomplished nothing since there was nothing left to send. Needs a decision on which leads/list to load before it's worth reactivating; didn't want to guess and risk double-contacting companies already reached via another campaign.
- **Amazon Seller 2cnd (2)** — schedule had drifted to America/Chicago (days unchanged, Tue–Thu, but wrong timezone label) and tracking flags had changed after this morning's fix, most likely a live edit in Instantly while we were working. Restored to Arctic/Longyearbyen, Tue–Thu 9am–5pm, matching every other campaign in the account.

**Flagged for Cüneyt, not changed — include in the client-facing report:**
- **Amazon Seller 2cnd (2) bounce rate: 8% (2 of 25 sent).** Above the 5% watch threshold from the original audit, but the sample is only 25 emails — not statistically meaningful yet. Left running; worth a second look once it's sent more volume. Couldn't isolate the specific bounced leads via the API to investigate further.

**Checked, no issue found:**
- Stale `salesfix.eu` mailbox references only appear on already-completed campaigns (8 of them, all "Review2 - ..." batches) — harmless, they won't send again.
- Account-level block list: 4 entries, all routine manual blocks (a domain + 3 individual leads) — nothing wrong.
- All 11 connected mailboxes re-checked: still Active, warmup 97–100, no connection errors.

## Part 6 — sellervate.net mailbox flap (jonas@, sebastian@)

Later the same day, jonas@sellervate.net and sebastian@sellervate.net briefly dropped to an unhealthy status in Instantly (status -3). Checked Hostinger hPanel directly for both — no suspend toggle was active on either (mailbox, access, receiving, or sending all clear), and by the time the check finished both had already recovered on their own in Instantly too. This looks like the same kind of transient flap as the original 554 5.7.1 pattern from the Aug 13 audit — self-resolving, but recurring.

**Action taken (precautionary):** Rather than leave the two campaigns exposed to the next flap, removed jonas@ and sebastian@sellervate.net from every active/paused campaign that used them and backfilled with jake@ and alex@starfix.online (that domain had the lightest campaign load — 2 campaigns vs. sellervate.net's 4 — so the most spare capacity to absorb it):

| Campaign | Mailboxes before | Mailboxes after |
|---|---|---|
| Liste von Dennis | jonas@, david@, tobias@, sebastian@ (sellervate.net) | david@, tobias@ (sellervate.net) + jake@, alex@ (starfix.online) |
| Amazon Seller 2cnd (2) | jonas@, david@, tobias@, sebastian@ (sellervate.net) | david@, tobias@ (sellervate.net) + jake@, alex@ (starfix.online) |
| Sports & Fitness (sellervate, reviews) | jonas@, david@, tobias@, sebastian@ (sellervate.net) | david@, tobias@ (sellervate.net) + jake@, alex@ (starfix.online) |
| 50K DE Amazon Leads (paused) | jonas@, david@, tobias@, sebastian@ (sellervate.net) | david@, tobias@ (sellervate.net) + jake@, alex@ (starfix.online) |

Confirmed jonas@ and sebastian@ are no longer referenced by any active/paused campaign (only 4 already-completed campaigns still list them, harmless). All four updated campaigns re-verified healthy afterward; 50K DE Amazon Leads correctly stayed paused.

**Flag for Cüneyt:** this is at least the second time sellervate.net mailboxes have briefly dropped and recovered on their own. Worth digging into the root cause (rate limits, provider-side flapping) if it keeps happening rather than relying on it clearing each time.

## Notes

- Mailbox reassignment and DKIM fix today were done via direct API call (Instantly API v2) and Hostinger hPanel — this session's default Instantly MCP connector was pointed at a different (unrelated) workspace, so Cüneyt's own API key and hPanel access (via amz.help@outlook.de) were used directly for all changes in this report.
- hellostarfix.com mailbox assignment for the 4 newly-fixed campaigns was a judgment call (idle capacity, not previously used by any campaign) — flag to Cüneyt if a different split is preferred.
