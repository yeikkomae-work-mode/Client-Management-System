# Cüneyt (SellerVate) — Amazon Seller (Rating, 964 leads): Instantly Draft → PlusVibe

**Date:** 2026-08-26
**Client:** Cüneyt — SellerVate (https://sellervate.de)
**Status:** ✅ Built in PlusVibe — **PAUSED, not launched**

---

## What was moved

The **"Amazon Seller"** campaign as drafted directly in Instantly — campaign id
`981b5d19-ea6b-412d-8c98-c00880e35e0a`, status **DRAFT**, `emails_sent_count: 0`. Confirmed via
the Instantly API before touching anything: this campaign has never sent a single email, and none
of its 964 leads have send history anywhere else in the account either — genuinely untouched
inventory, zero risk of double-contacting anyone.

This is separate from (and does not overlap with) the 107-lead `Amazon Seller UK/USA [MIGRATED]`
campaign built on 2026-08-25 — that one used the product-category variant (file 3, no rating data).
This campaign uses the rating variant (files 1+2, all 964 leads have Rating populated, none have
Product Type).

| | |
|---|---|
| Source | Instantly campaign "Amazon Seller" (draft, `981b5d19-ea6b-412d-8c98-c00880e35e0a`) |
| PlusVibe workspace | Cüneyt's Workspace (`6a8c1c4f92e45be273aa9201`) |
| Campaign name | `Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT]` |
| Campaign ID | `6a8ee087c3903d2a71741b72` |
| Status | **PAUSED** — nothing sends until manually activated |
| Leads | **964** uploaded — 0 duplicate, 0 invalid, 0 missing rating |
| Sequence | 3 emails, Day 0 / 3 / 7, Rating variant |
| Mailboxes | 10 — all of hellostarfix.com |

---

## Why hellostarfix.com

The other paused campaign (`Amazon Seller UK/USA [MIGRATED]`) already claims all 9 starfix.online +
sellervate.net mailboxes. hellostarfix.com's 10 mailboxes had nothing assigned to them, so this
campaign uses those instead — the two campaigns won't compete for the same daily send capacity when
both eventually launch.

---

## Sequence — sourced from the live Instantly draft, not the local markdown draft

Pulled directly from Instantly's API (`GET /api/v2/campaigns/{id}`) rather than reconstructed from
memory, to make sure the copy that actually made it into the client's Instantly account is what
shipped here. It's the same 3-step, dual-variant structure as the earlier build (Variant A =
Rating, Variant B = Product Type per step) — this campaign only needed Variant A, since none of
these 964 leads have Product Type data.

Same two PlusVibe platform fixes applied as the previous migration:

1. **Custom variables take a `custom_` prefix** — `{{Rating}}` → `{{custom_rating}}`.
2. **Only one variable per spintax section** — the Instantly draft nests `{{companyName}}` and
   `{{Rating}}` together inside RANDOM blocks, and the subject line nests a different single
   variable inside each of its 3 RANDOM branches. Both patterns needed restructuring with merge
   fields outside the spintax, wording kept intact. The same validator from the last build
   (`sequences_rating.py`) asserts no variable is ever nested inside a RANDOM block.

`{{accountSignature}}` → `{{sender_signature}}` (PlusVibe's native signature var, already
populated on all 19 inboxes as of the Aug 25 signature fix).

---

## Data quality (964 leads, checked before upload)

| Field | Coverage |
|---|---|
| Rating | 100% (2.4–5.0, avg 4.23) |
| Country | 100% (467 US, 314 UK, 183 spread across 13 other countries) |
| Industry, Employees, Amazon URL, Review Count, Company LinkedIn | 100% |
| Contact Number | 63% (not used by this sequence, email-only) |
| Product Type, Revenue, Comment | 0% (not needed for this variant) |
| Internal duplicates | 0 |

---

## Campaign settings

Same defaults as the previous build: PAUSED, start date 2026-09-07 (14 days after hellostarfix.com
warmup began), Mon–Fri 09:00–17:00 America/New_York, daily limit 30, stop on reply, open tracking
on, unsubscribe link, auto-pause at 4% bounce, round-robin variant selection.

**Timezone judgment call, flagged same as last time:** 467 US + 314 UK + 183 across 13 other
countries (Germany, Italy, Spain, Belgium, Netherlands, Denmark, Ireland, Sweden, France,
Switzerland, Finland, Bulgaria, Canada) — US is the largest single bloc so it drives the schedule,
but this is a genuinely international list. Splitting by region would serve the EU portion better.

---

## Before launching

- [ ] Send a test email and confirm `{{custom_rating}}` renders
- [ ] Wait out warmup — do not activate before ~Sep 7
- [ ] Given the volume (964 leads, 10 mailboxes, 30/day cap = ~300/day capacity), first full pass
      through the list takes ~3-4 days — sanity-check that against whatever pace Cüneyt expects
- [ ] Decide whether the two "Amazon Seller" PlusVibe campaigns (this one + the 107-lead UK/USA one)
      should launch on the same date or staggered
- [ ] Retire the Instantly draft once this is live and confirmed, so nobody accidentally launches
      the original alongside it

---

**Build scripts:** `scripts/plusvibe-migration/sequences_rating.py`, `migrate_rating.py` (API key
read from the environment — never committed)
