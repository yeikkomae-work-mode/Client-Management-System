# Cüneyt (Starfix) — Personalized Email Sequence Draft

**Purpose:** Draft copy for Cüneyt's Aug 20 request — personalize each cold email with the prospect's actual Amazon product data, so it's clear Starfix already checked their listing.
**Format:** Same convention as the existing Instantly campaigns and the earlier suggested sequence — merge fields + sentence-level `{{RANDOM | opt1 | opt2 | opt3}}` spintax. 3 emails (Day 0 / 3 / 7).
**Status:** Draft for Cüneyt's review — not yet built in Instantly.

---

## New variables needed (in addition to existing {{first_name}} / {{company_name}})

| Variable | What it holds | Example |
|---|---|---|
| `{{product_name}}` | The specific Amazon product/listing being referenced | "Wireless Charging Pad" |
| `{{star_rating}}` | Current average star rating | "3.8" |
| `{{negative_review_count}}` | Number of 1–3 star reviews found | "6" |

⚠️ **Feasibility note for Cüneyt:** Instantly can insert these into emails the same way it does `{{first_name}}`/`{{company_name}}` — but only if the values already exist as columns in the lead list CSV before upload. Instantly doesn't check Amazon listings live. This means someone (manual research, a scraper, or an enrichment tool) needs to pull product name + star rating + negative review count for each lead **before** the list goes into Instantly.

**Checked against the actual lead sheet Cüneyt is using (Amazon USA Product Review 2nd - Small Medium Size Companies), Aug 20:**

| Data needed | Status in the sheet |
|---|---|
| Star rating | ✅ Already there — column "Rating" (e.g. 4.4) |
| Amazon URL | ✅ Already there — column "Amazon URL" |
| Product name | ⚠️ **Not a real column.** Only the Amazon URL exists, and the "product name" would have to be scraped from the URL slug (e.g. `Alkaline-Ionised-Spring-Purified-Electrolytes`) — messy, not client-ready text without cleanup |
| Negative review count | ❌ **Not in the sheet at all.** The "Review" column is the *total* review count (e.g. 2,915), not a count of 1–3 star / non-compliant reviews. Getting that number means actually auditing the listing — the same manual work behind Starfix's core service — it can't be pulled from a public field |

**Net effect:** star rating personalization is ready to go today. Product name needs a cleanup step (or manual naming) before it's usable. Negative review count can't be automated from this sheet — it would need to either (a) be dropped from the copy, (b) replaced with softer language ("reviews that may not comply" instead of a specific number), or (c) actually be pre-audited per lead, which is significant manual/tool work per campaign, not a one-time setup.

---

## Email 1 — Day 0

**Subject:**
`{{RANDOM | found something on {{product_name}}, {{first_name}} | quick note on your {{product_name}} listing | {{star_rating}} stars on {{product_name}} — worth a look}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I took a look at {{company_name}}'s {{product_name}} listing — it's currently sitting at {{star_rating}} stars, and we found {{negative_review_count}} reviews that read more like delivery or seller complaints than actual product feedback. | While checking {{company_name}}'s Amazon store, I looked closer at {{product_name}} ({{star_rating}} stars) and spotted {{negative_review_count}} reviews that seem off-topic — more about shipping or service than the product itself. | I went through {{company_name}}'s {{product_name}} listing (currently {{star_rating}} stars) and found {{negative_review_count}} reviews that look like they shouldn't count against the product rating.}}

{{RANDOM | Amazon's Community Guidelines don't actually allow reviews like that to stay on a listing, even though most sellers never challenge them. | Under Amazon's own guidelines, reviews like that usually don't qualify to remain on the product page — most sellers just don't know they're removable. | Those kinds of reviews technically violate Amazon's Community Guidelines, but very few sellers ever flag them.}}

{{RANDOM | We already ran a free check on {{product_name}} — happy to send over exactly which reviews look removable, no cost either way. | We've already looked at {{product_name}} specifically — want me to send what we found? No cost, no obligation. | Since we already checked {{product_name}}, I can send the breakdown of what's realistically removable whenever you'd like.}}

{{RANDOM | Want me to send it over? | Worth a look? | Interested in seeing the breakdown?}}

{{sender_signature}}
```

---

## Email 2 — Day 3

**Subject:**
`{{RANDOM | following up on {{product_name}} | quick nudge, {{first_name}} | still worth checking {{product_name}}}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | Circling back on {{product_name}} — at {{star_rating}} stars with {{negative_review_count}} reviews that look non-compliant, there's likely real upside in getting a few of those removed. | Just following up on the {{product_name}} listing. {{negative_review_count}} of the reviews we flagged look like they're pulling that {{star_rating}} rating down for reasons that have nothing to do with the product. | Wanted to bump this back up — {{negative_review_count}} reviews on {{product_name}} look removable, which could move that {{star_rating}} rating in the right direction.}}

{{RANDOM | We only get paid if a review actually comes down, so there's no risk in checking. | This is fully success-based — you pay only for reviews that are actually removed. | No subscription, no flat fee. You only pay for what we successfully remove.}}

{{RANDOM | We've handled thousands of these cases as an Amazon SPN partner, so we know which ones are worth pursuing. | We do this daily as an Amazon SPN partner — we know Amazon's process well enough to push past the first auto-reply. | Between similar cases, we've removed well over 5,000 reviews across categories like this one.}}

{{RANDOM | Want the full breakdown on {{product_name}}? | Should I send over what we found? | Happy to share the specifics whenever works.}}

{{sender_signature}}
```

---

## Email 3 — Day 7 (break-up)

**Subject:**
`{{RANDOM | should I close this out? | last note on {{product_name}} | one more try, {{first_name}}}}`

**Body:**
```
Hi {{first_name}},

{{RANDOM | I'll leave it here for now — didn't want the {{product_name}} findings to just sit unanswered. | This is my last note on {{product_name}}, don't want to keep nudging if it's not a priority right now. | Not trying to be a pest, so this'll be my last message on this one.}}

{{RANDOM | If the {{negative_review_count}} reviews on {{product_name}} ever become worth a look, the breakdown is ready whenever you want it. | If this becomes relevant later, happy to send what we found on {{product_name}} anytime. | The offer's open whenever it's useful — just reply and I'll send the {{product_name}} breakdown.}}

{{RANDOM | If it's not the right time, no worries at all — just let me know and I'll close this out. | All good either way, just say the word and I'll stop following up. | Totally fine if it's not a priority, just a quick reply and I'll drop it.}}

{{sender_signature}}
```

---

---

## Realistic version — using only what's actually in the lead sheet today

The templates above assume all 3 variables are available. Since only `{{star_rating}}` is real data right now, here's Email 1 rewritten to match what can actually ship without extra data-prep work — drops the hard negative-review number in favor of honest, still-personalized language:

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

This keeps the "we already looked at your specific listing" feel Cüneyt wants, uses real data (star rating), and doesn't overpromise a specific bad-review count that isn't actually known yet.

---

## Final composed sequence — ready to build in Instantly

Full 3-email sequence using only what's actually in the lead sheet (`{{first_name}}`, `{{company_name}}`, `{{star_rating}}`). No product name, no negative review count — those aren't real fields yet, so nothing below promises a number that can't be backed up.

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

## What to show Cüneyt

Two things to walk him through:

1. **The full-personalization version above** — shows what it'd look like with product name, star rating, and negative review count all filled in. This is the vision he described.
2. **The realistic version** — checked against his actual lead sheet (Amazon USA Product Review 2nd SMB), and only star rating is real, ready-to-use data today. Product name isn't a clean column (just a raw Amazon URL), and negative review count doesn't exist anywhere — pulling it means manually auditing each listing, which is Starfix's actual paid service, not a free data point. The realistic version above ships today using just the star rating and softer language, without promising a specific bad-review count that isn't actually known.

Worth asking him directly: does he want to (a) launch with the realistic version now, or (b) wait and build out a proper per-lead audit step (more setup time, but delivers the full pitch he described)?
