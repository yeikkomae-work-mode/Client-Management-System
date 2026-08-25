# Cüneyt (SellerVate) — Amazon Seller Campaign: Instantly → PlusVibe

**Date:** 2026-08-25
**Client:** Cüneyt — **SellerVate** (https://sellervate.de)
**Brand note:** the business is **SellerVate**, not "Starfix" as older records in this repo say (corrected 2026-08-25). Starfix is sending-domain identity only. The campaign copy names no brand — it signs off with `{{sender_signature}}` — so nothing built here was affected.
**Status:** ✅ Built in PlusVibe — **PAUSED, not launched**

---

## What was moved

The drafted **UK/USA Amazon Seller** campaign — Sequence B (product-category angle) from
`Cüneyt - Starfix Revised Sequences (Cleaned Database, 2026-08-21).md`, run against the cleaned
`3_UK_USA_Amazon_Seller_CLEANED.csv` list.

This was the one Amazon list whose drafted copy was never built anywhere — it had no rating data,
so it got its own product-category sequence rather than the star-rating one used for the other two lists.

| | |
|---|---|
| PlusVibe workspace | Cüneyt's Workspace (`6a8c1c4f92e45be273aa9201`) |
| Campaign name | `Amazon Seller UK/USA [MIGRATED]` |
| Campaign ID | `6a8cf6f27e5c6119d8830749` |
| Status | **PAUSED** — nothing sends until manually activated |
| Leads | **107** uploaded (0 invalid, 0 duplicate) |
| Sequence | 3 emails, Day 0 / 3 / 7 |
| Mailboxes | 9 — all 4 starfix.online + all 5 sellervate.net |

**Lead count:** the cleaned file holds 109. The 2 cross-file duplicates
(`philip@palladiobeauty.com`, `prudence@beautybyearth.com`) were dropped on upload since they already
sit in the MAIN List — leaving 107. This clears the open item from the 2026-08-21 log.

---

## Copy changes forced by the platform

The drafted copy was written for Instantly. Two PlusVibe rules required changes — the copy would
have shipped broken otherwise.

**1. Custom variables take a `custom_` prefix.**
`{{product_category}}` → `{{custom_product_category}}`. Confirmed against the live API: the value
uploads into the lead record as `custom_product_category`. Mapped from the `Product Type` column,
100% populated across all 107 leads.

**2. Only ONE variable is allowed per spintax section.**
This is the important one. The drafted copy nested **two** merge fields inside single RANDOM blocks —
e.g. `{{RANDOM | I took a look at {{company_name}}'s {{product_category}} listings... }}`. PlusVibe
rejects more than one variable inside a spintax block, so every merge field was moved **outside** the
RANDOM blocks, keeping the varied wording intact:

> `I took a look at {{company_name}}'s {{custom_product_category}} listings on Amazon. {{RANDOM | A few of the reviews read more like delivery or seller complaints... | Some of the reviews seem off-topic... | Several reviews look like they shouldn't count...}}`

Meaning and the 3-variation-per-sentence structure are unchanged. A validator in the build script
asserts no variable is ever nested inside a RANDOM block.

**3. `{{first_name}}` / `{{company_name}}` stayed as-is.**
Worth flagging: the `satlas-cold-email` skill states PlusVibe uses camelCase (`{{firstName}}`,
`{{companyName}}`). That appears to be **wrong** — PlusVibe's own help docs and the live API both use
snake_case, and the API stores `first_name` / `company_name`. Used snake_case here.
**Chris Drew's PlusVibe campaigns should be spot-checked for this**, since copy built on the skill's
guidance may be rendering blank names.

---

## Campaign settings

| Setting | Value | Why |
|---|---|---|
| Status | PAUSED | Mailboxes only started warming Aug 24 |
| Start date | 2026-09-07 | 14 days after warmup began |
| Schedule | Mon–Fri, 09:00–17:00 | |
| Timezone | America/New_York | 63 US / 45 UK / 1 CA — 9am ET is still in-hours for UK |
| Daily limit | 30 | Account-wide convention post-DKIM fix |
| Stop on reply | Yes | Matches existing account convention |
| Open tracking | **On** | Audit rec #1 — the fleet-wide open-tracking blind spot |
| Unsubscribe link | Yes | |
| Auto-pause on bounce | Yes, at 4% | |
| Variant selection | Round robin | |

Two of these are judgement calls worth a second look: **open tracking** (turned on per the Aug 13
audit recommendation, but it does add a pixel on freshly-warmed domains — one toggle to reverse), and
the **single America/New_York timezone** for a mixed UK/US list (splitting into two campaigns would
serve both blocs better).

---

## Before launching

- [ ] Send a test email from PlusVibe and confirm `{{custom_product_category}}` renders (this is the
      variable most likely to break — verify before anything else)
- [ ] **Set `{{sender_signature}}` on the sending inboxes — checked 2026-08-25, 18 of 19 are EMPTY.**
      As it stands every email would end with no sign-off at all. The one populated signature
      (laura@hellostarfix.com) reads `Best,\n\nLaura\nSellerVeta` — **"SellerVeta" is a misspelling
      of SellerVate** and needs fixing before it goes out. Signatures do not carry over from Instantly.
      Needs Cüneyt's actual sign-off block (name, title, contact) — his call, not ours to invent.
- [ ] Confirm the step delays read as Day 0 / 3 / 7 in the UI (`wait_time` is set as days *after*
      each step; step 3 carries a filler value of 1 because the API rejects 0)
- [ ] Wait out warmup — do not activate before ~Sep 7
- [ ] Retire/archive the equivalent paused Instantly campaigns once this is live and confirmed

---

## Still on Instantly

The other two cleaned lists are **not** migrated — they use Sequence A (star rating), which is a
separate build:

| List | Leads | Sequence |
|---|---|---|
| Amazon USA Product Review 2nd SMB | 613 | A — star rating |
| Amazon Leads MAIN List | 714 | A — star rating |

The build script (`scripts/plusvibe-migration/`) is parameterised and can do both the same way.

---

**Build script:** `scripts/plusvibe-migration/` (reads the API key from the environment — never committed)
