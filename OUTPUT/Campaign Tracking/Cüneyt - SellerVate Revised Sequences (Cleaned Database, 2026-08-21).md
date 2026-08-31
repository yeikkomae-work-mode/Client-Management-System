# Cüneyt (SellerVate) — Sequences Revised Against Cleaned Database

**Trigger:** "clean it, organize it, then revise email sequence based from the cleaned database."
**Source data:** `Cüneyt - Cleaned Lead Lists (2026-08-21)/` — 1,436 unique clean leads across 3 files (see README in that folder for cleaning details).
**Format:** Same convention as existing campaigns — merge fields + sentence-level `{{RANDOM | opt1 | opt2 | opt3}}` spintax. 3 emails (Day 0 / 3 / 7).
**Status:** Draft for review — not yet built in Instantly.

---

## Which sequence goes with which list

| List | Rating data? | Sequence to use |
|---|---|---|
| 1 — Amazon USA Product Review 2nd SMB (613 leads) | ✅ Yes | **Sequence A — Star Rating** (below) |
| 2 — Amazon Leads MAIN List (714 leads) | ✅ Yes | **Sequence A — Star Rating** (below) |
| 3 — UK_USA Amazon Seller (109 leads) | ❌ No — has `Product Type` instead | **Sequence B — Product Category** (below) |

Verified against the actual cleaned CSVs: Rating is 100% populated in Files 1 & 2 (no missing values after cleaning), so `{{star_rating}}` can be mapped straight from that column. File 3 has zero Rating data — it only has `Product Type` (e.g. "Health Products," "Pet Animals Accessories," "Wellness and Fitness Products") and `Revenue`, so it needs its own angle rather than being forced into the rating-based copy.

---

## Sequence A — Star Rating (Files 1 & 2)

This is the same "realistic version" composed on 2026-08-20, now confirmed against the cleaned data (no changes needed — Rating is fully populated in both lists). Map `{{star_rating}}` to the `Rating` column on upload.

### Email 1 — Day 0

**Subject:**
`{{RANDOM | found something on {{company_name}}'s Amazon listing | quick note on your {{star_rating}}-star listing | worth a look, {{first_name}}}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I took a look at {{company_name}}'s Amazon listing — currently sitting at {{star_rating}} stars — and noticed a few reviews that read more like delivery or seller complaints than actual product feedback. | While checking {{company_name}}'s Amazon store ({{star_rating}} stars), I spotted some reviews that seem off-topic — more about shipping or service than the product itself. | I went through {{company_name}}'s listing (currently {{star_rating}} stars) and found reviews that look like they shouldn't count against the rating.}}

{{RANDOM | Amazon's Community Guidelines don't actually allow reviews like that to stay on a listing, even though most sellers never challenge them. | Under Amazon's own guidelines, reviews like that usually don't qualify to remain on the product page — most sellers just don't know they're removable. | Those kinds of reviews technically violate Amazon's Community Guidelines, but very few sellers ever flag them.}}

{{RANDOM | We can run a free, closer check and send back exactly which reviews look removable — no cost either way. | Happy to run a no-cost audit on your listing and show you what's realistically removable. | We can check the listing free of charge and send you a breakdown, no obligation.}}

{{RANDOM | Want me to send it over? | Worth a look? | Interested in seeing the breakdown?}}

{{sender_signature}}
```

### Email 2 — Day 3

**Subject:**
`{{RANDOM | following up, {{first_name}} | quick nudge on the {{star_rating}}-star listing | still worth checking}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | Circling back on this — most sellers are surprised how many of their reviews actually qualify for removal once we look closely, and {{company_name}}'s {{star_rating}}-star listing looked worth a proper check. | Just following up. It's common for brands sitting around {{star_rating}} stars to have a few reviews that never should have been approved in the first place. | Wanted to bump this back up — worth a closer look at what's pulling {{company_name}}'s rating down from where it could be.}}

{{RANDOM | We only get paid if a review actually comes down, so there's no risk in checking. | This is fully success-based — you pay only for reviews that are actually removed. | No subscription, no flat fee. You only pay for what we successfully remove.}}

{{RANDOM | We've worked through thousands of these cases as an Amazon SPN partner, so we know which ones are worth pursuing and which aren't. | We do this daily as an Amazon SPN partner — we know Amazon's internal process well enough to push past the first auto-reply. | Between similar cases, we've removed well over 5,000 reviews across categories like this one.}}

{{RANDOM | Still happy to run the free check whenever works. | Want me to send over what we'd find? | Send the word whenever's convenient and I'll get you the breakdown.}}

{{sender_signature}}
```

### Email 3 — Day 7 (break-up)

**Subject:**
`{{RANDOM | should I close this out? | last note on this, {{first_name}} | one more try before I stop}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I'll leave it here for now — didn't want this to just sit unanswered in your inbox. | This is my last note on this, don't want to keep nudging if it's not a priority right now. | Not trying to be a pest, so this'll be my last message on it.}}

{{RANDOM | If {{company_name}}'s reviews ever become worth a look, the free check still stands — just reply and I'll run it. | If this becomes relevant later, happy to pick this back up anytime. | The offer's open whenever it's useful, just reply and we'll take it from there.}}

{{RANDOM | If it's not the right time, no worries at all, just let me know and I'll close this out. | All good either way, just say the word and I'll stop following up. | Totally fine if it's not a priority, just a quick reply and I'll drop it.}}

{{sender_signature}}
```

---

## Sequence B — Product Category (File 3 only)

File 3 has no rating data, so this version drops the star-rating hook and personalizes on `{{product_category}}` (map from the `Product Type` column, e.g. "Health Products") instead — still ties back to SellerVate's core review-removal pitch without claiming a rating figure that isn't in the data.

### Email 1 — Day 0

**Subject:**
`{{RANDOM | question about your {{product_category}} listings on Amazon | quick note, {{first_name}} | found something worth flagging on your Amazon store}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I took a look at {{company_name}}'s {{product_category}} listings on Amazon and noticed a few reviews that read more like delivery or seller complaints than actual product feedback. | While checking out {{company_name}}'s Amazon store in the {{product_category}} space, I spotted some reviews that seem off-topic — more about shipping or service than the product itself. | I went through {{company_name}}'s {{product_category}} listings and found reviews that look like they shouldn't count against the product rating.}}

{{RANDOM | Amazon's Community Guidelines don't actually allow reviews like that to stay on a listing, even though most sellers never challenge them. | Under Amazon's own guidelines, reviews like that usually don't qualify to remain on the product page — most sellers just don't know they're removable. | Those kinds of reviews technically violate Amazon's Community Guidelines, but very few sellers ever flag them.}}

{{RANDOM | We can run a free, closer check and send back exactly which reviews look removable — no cost either way. | Happy to run a no-cost audit on your listing and show you what's realistically removable. | We can check the listing free of charge and send you a breakdown, no obligation.}}

{{RANDOM | Want me to send it over? | Worth a look? | Interested in seeing the breakdown?}}

{{sender_signature}}
```

### Email 2 — Day 3

**Subject:**
`{{RANDOM | following up, {{first_name}} | quick nudge on your {{product_category}} listings | still worth checking}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | Circling back on this — most sellers in the {{product_category}} space are surprised how many of their reviews actually qualify for removal once we look closely. | Just following up. It's common for {{product_category}} brands to have a few reviews that never should have been approved in the first place. | Wanted to bump this back up — worth a closer look at what might be pulling {{company_name}}'s ratings down.}}

{{RANDOM | We only get paid if a review actually comes down, so there's no risk in checking. | This is fully success-based — you pay only for reviews that are actually removed. | No subscription, no flat fee. You only pay for what we successfully remove.}}

{{RANDOM | We've worked through thousands of these cases as an Amazon SPN partner, so we know which ones are worth pursuing and which aren't. | We do this daily as an Amazon SPN partner — we know Amazon's internal process well enough to push past the first auto-reply. | Between similar cases, we've removed well over 5,000 reviews across categories like {{product_category}}.}}

{{RANDOM | Still happy to run the free check whenever works. | Want me to send over what we'd find? | Send the word whenever's convenient and I'll get you the breakdown.}}

{{sender_signature}}
```

### Email 3 — Day 7 (break-up)

**Subject:**
`{{RANDOM | should I close this out? | last note on this, {{first_name}} | one more try before I stop}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I'll leave it here for now — didn't want this to just sit unanswered in your inbox. | This is my last note on this, don't want to keep nudging if it's not a priority right now. | Not trying to be a pest, so this'll be my last message on it.}}

{{RANDOM | If {{company_name}}'s reviews ever become worth a look, the free check still stands — just reply and I'll run it. | If this becomes relevant later, happy to pick this back up anytime. | The offer's open whenever it's useful, just reply and we'll take it from there.}}

{{RANDOM | If it's not the right time, no worries at all, just let me know and I'll close this out. | All good either way, just say the word and I'll stop following up. | Totally fine if it's not a priority, just a quick reply and I'll drop it.}}

{{sender_signature}}
```

---

## Upload notes

- Files 1 & 2: map `{{star_rating}}` → `Rating` column. Both are 100% populated post-cleaning, so no leads need to be excluded for missing data.
- File 3: map `{{product_category}}` → `Product Type` column. All 109 rows have this populated.
- Before uploading, pull the 2 cross-file duplicate emails (`philip@palladiobeauty.com`, `prudence@beautybyearth.com`) out of File 3 — they're already in File 2 (MAIN List). See `cross_file_duplicate_emails.csv`.
- Product name and negative-review-count personalization are still not available in any of the 3 lists (same finding as the 2026-08-20 draft) — would need manual per-lead audit work to add.
