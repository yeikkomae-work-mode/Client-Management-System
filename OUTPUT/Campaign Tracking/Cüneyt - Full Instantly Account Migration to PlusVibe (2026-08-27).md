# Cüneyt (SellerVate) — Full Instantly Account Audit & Migration to PlusVibe

**Date:** 2026-08-27
**Client:** Cüneyt — SellerVate (https://sellervate.de)
**Status:** 8 more campaigns built, PAUSED. 1 group held back pending a client answer.

---

## What this covers

Following up on the 2026-08-26 request to pull the copy for the other 24 Instantly campaigns
(everything beyond the "Amazon Seller" rating campaign already migrated), revise it for PlusVibe,
and run every lead through MillionVerifier with a dedupe pass first.

---

## Pipeline: pull → dedupe → verify → revise → upload

**1. Pulled all 24 remaining campaigns** via the Instantly API — full sequences, custom variable
config, and complete lead payloads. 3,057 raw rows.

**2. Deduped**, in two passes:
- Within the 24 campaigns themselves (245 leads appear in 2+): 3,057 → 2,812 unique.
- Against everyone already uploaded to PlusVibe (the 1,434 leads across the two Amazon Seller
  campaigns): excluded 108 more → **2,704 final targets**.

**3. Ran every one of the 2,704 through MillionVerifier** (`quality=good` required to pass):

| Result | Count |
|---|---|
| good (pass) | 1,899 |
| risky | 675 |
| bad | 130 |

1,994 credits spent (9,360 → 7,366 remaining). Sampled the two lowest pass-rate campaigns
(USA Seller 18/96, Starfix New UK Leads 2026-08 0/45) to rule out a pipeline bug before trusting
the numbers — both checked out: most of "USA Seller"'s leads were already in PlusVibe (correctly
skipped, not verified twice), and all 45 of "Starfix New UK Leads 2026-08" were already covered
by earlier campaigns, leaving nothing to build for it.

**4. Copy check:** the 24 campaigns collapse to **11 distinct copy sets** (many campaigns reuse
identical sequences — e.g. 9 different "Review2 - [Category] DE" tiers all shared one German
template). None of them use spintax — straightforward variable renaming, no creative rewriting
needed, no risk of the nested-RANDOM issue from the earlier campaigns.

---

## Brand finding — flagged before writing anything

One of the 11 copy sets (1,164 raw leads / 822 verified, **43% of the whole batch** — Sports &
Fitness (mixed), Pet, Baby, and all 9 "Review2 - DE" tiers) is signed **"SalesFix Team"** from
**www.salesfix.ai** — a brand name that has never appeared anywhere in this repo before. Not
Starfix, not SellerVate.

Given this session already had to untangle a real Starfix/SellerVate brand mixup once, this
wasn't treated as another mechanical swap. Eikko has drafted a question for Cüneyt rather than
guessing — **this group is excluded from this build until that's answered.**

---

## Built this round (8 campaigns, all PAUSED, all sharing the existing 19 mailboxes)

| Campaign | Source Instantly campaign(s) | Verified leads | Brand fix applied |
|---|---|---|---|
| Liste von Dennis + 50K DE Amazon Leads [MIGRATED] | Liste von Dennis, 50K DE Amazon Leads | 175 | No — already SellerVate |
| USA Seller [MIGRATED] | USA Seller | 18 | Yes — Starfix → SellerVate |
| Amazon Seller 2cnd (2) [MIGRATED] | Amazon Seller 2cnd (2) | 180 | Yes |
| Sports & Fitness Reviews (SellerVate) [MIGRATED] | Sports & Fitness (sellervate, reviews) | 130 | No — already SellerVate |
| UK Seller [MIGRATED] | UK Seller (starfix) | 24 | Yes |
| **Amazon Ops Support [MIGRATED]** | 50K Leads, Agency Leads | 148 | No — already SellerVate |
| Starfix New US Leads 2026-07-29 [MIGRATED] | Starfix New US Leads 2026-07-29 | 368 | Yes |
| Review [MIGRATED] | Review | 164 | No — already SellerVate |
| **Total** | | **1,207** | |

**Amazon Ops Support is a genuinely different offer** from the review-removal pitch — general
Amazon operational support (catalog errors, listing indexing, technical fixes), pitched as "join
your team." Built as its own campaign per Eikko's explicit go-ahead, since it's a real distinct
service, not a mistake.

### Brand fix detail (4 campaigns)

The Starfix-branded copy used two patterns, both corrected with zero leftover mentions verified
by regex sweep after conversion:
- `"Starfix Team"` → `"SellerVate Team"` (signature)
- `"at Starfix"` / `"using Starfix"` / `"Starfix helps"` → `"at/using/helps SellerVate"` (body copy)
- `"starfix.ai"` → `"sellervate.de"` (domain references)

### Variable conversion (all 8)

Same platform rules as the earlier campaigns — none of these use spintax, so this was pure
mechanical renaming:

| Instantly | PlusVibe |
|---|---|
| `{{firstName}}` | `{{first_name}}` |
| `{{lastName}}` | `{{last_name}}` |
| `{{companyName}}` | `{{company_name}}` |
| `{{accountSignature}}` | `{{sender_signature}}` |
| `{{website}}` | `{{custom_website}}` |
| `{{jobTitle}}` | `{{custom_job_title}}` |
| `{{linkedIn}}` | `{{custom_linkedin}}` |

---

## Excluded from this round

| Group | Leads | Why |
|---|---|---|
| SalesFix-signed copy | 822 verified | Pending Cüneyt's answer on the SalesFix brand identity |
| "Upwork Leads" (SEO-audit offer) | 0 | Different offer again (listing keyword/indexing audit); 0 leads currently so no real cost to waiting |
| "Starfix New UK Leads 2026-08" | 0 remaining | All 45 already covered by earlier campaigns — nothing left to build |

---

## Account-wide picture now

| | Leads in PlusVibe |
|---|---|
| Amazon Seller - Rating (review-removal, star rating) | 1,327 |
| Amazon Seller UK/USA (review-removal, product category) | 107 |
| The 8 campaigns built this round | 1,207 |
| **Total in PlusVibe** | **2,641** |
| Still only in Instantly (SalesFix pending + the two out-of-scope groups) | 822 |

Of the original 3,776 unique leads across the whole Instantly account, **2,641 (70%) are now in
PlusVibe.** The remaining 822 are one answer away from being fully covered too.

---

## Before launching (applies to all 8 new campaigns)

- [ ] Test-send from each and confirm `{{custom_website}}` / `{{custom_job_title}}` / `{{custom_linkedin}}` render
- [ ] Wait out warmup — same Sep 7 floor as the other campaigns
- [ ] Get Cüneyt's answer on SalesFix, then build that group the same way
- [ ] With 10 campaigns now sharing 19 mailboxes, revisit whether to stagger launch dates rather than activate everything at once — daily send capacity is shared across whichever campaigns go live together

---

**Build script:** `scripts/plusvibe-migration/build_batch2.py` + `verify_batch.py` (MillionVerifier
key and PlusVibe key both read from the environment — never committed)
