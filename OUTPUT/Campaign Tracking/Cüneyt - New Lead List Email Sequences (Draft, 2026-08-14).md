# SellerVate — New Email Sequences for the 4 Lead Lists (Draft)

> [!IMPORTANT]
> **Brand name in the copy below is wrong — corrected 2026-08-25.**
> The email copy on this page signs off as **"Starfix"**. The business is
> **SellerVate** (https://sellervate.de). The copy is left here **verbatim** because
> this page is a record of what was actually built/sent — do not silently edit it.
> **Any of this copy must have "Starfix" swapped to "SellerVate" before it is reused
> or relaunched.** The PlusVibe Amazon Seller campaign built on 2026-08-25 is not
> affected: it names no brand and signs off with `{{sender_signature}}`.


**Date:** 2026-08-14 | **Status:** Draft — not yet built in Instantly, needs Cüneyt's review before launch

These 4 sequences correspond to the 4 lead lists linked in Cüneyt's "Leads Copy" Google Sheet (total 2,138 contacts). Two lists are cold (no pre-identified review, ask for an ASIN); two are warm (a specific review was already flagged during list-building, so copy references it directly via `{{review}}`/`{{rating}}` merge fields).

**Before launch:**
- None of these exist in Instantly yet — need to be built as new campaigns and assigned mailboxes/domains per the existing rotation.
- Verify the `{{review}}` / `{{rating}}` merge field names against the actual column headers in the "Amazon USA Product Review" and "...2nd" sheets before import (confirmed columns: `Rating`, `Review`).
- Confirm all 2,138 contacts get run through email verification first (see Total Contacts sheet) before upload.

---

## SEQUENCE 1 — "UK & USA Amazon Brand Leads"

**Target list:** UK & USA Amazon Brand Leads (640 contacts) | **Segment:** Cold, Amazon brand owners (US/UK)
**Rationale:** These are brand owners, not generic sellers — lead with brand-reputation/rating protection framing since a diluted star rating hits brand equity, not just one listing.

**Step 1 — Day 0**
Subject: a quick look at {{companyName}}'s Amazon reviews
```
Hi {{firstName}},

I took a look through {{companyName}}'s Amazon listings and noticed something worth flagging. Some reviews sitting on brand listings aren't actually about the product at all — they're about shipping, packaging, or seller service. Amazon's guidelines don't allow these to count toward your rating, but most brands never check.

At Starfix, we run a free audit on 1 ASIN and show you exactly which reviews may qualify for removal, no obligation either way.

Want me to check one of your listings?

Best,
Cüneyt / Starfix
```

**Step 2 — Wait 3 days**
Subject: protecting {{companyName}}'s star rating
```
Hi {{firstName}},

Following up on my last note. For brand owners specifically, a handful of off-topic reviews (delivery complaints, competitor sabotage, unrelated rants) can quietly drag a listing's rating down even though the product itself is fine.

We check whether any of those exist on your account and whether they're eligible for removal under Amazon's own guidelines, at no cost.

Send over 1 ASIN and we'll send back exactly what we find. No pressure to act on it.

Worth a look?

Best,
Cüneyt / Starfix
```

**Step 3 — Wait 3 days**
Subject: what a free audit actually shows you
```
Hi {{firstName}},

Wanted to be specific about what this actually is. We're not asking for account access or a subscription, just 1 ASIN from {{companyName}}. We check it against Amazon's Community Guidelines and send back a short report on any reviews that may qualify for removal and why.

You only pay if a review is actually taken down. If nothing qualifies, you've lost nothing by checking.

Happy to run it whenever you're ready.

Best,
Cüneyt / Starfix
```

**Step 4 — Wait 3 days**
Subject: should I close this out?
```
Hi {{firstName}},

Don't want to keep landing in your inbox, so this is my last note on this.

If protecting {{companyName}}'s rating from reviews that shouldn't be there isn't a priority right now, no problem at all. If it is, send me 1 ASIN and I'll get the free audit back to you within a day or two, no strings attached.

Either way, appreciate you reading this far.

Best,
Cüneyt / Starfix
```

---

## SEQUENCE 2 — "UK/USA Amazon Seller"

**Target list:** UK/USA Amazon Seller (109 contacts) | **Segment:** Cold, targeted sellers with industry/product-type data
**Rationale:** Smaller, more targeted list with `{{industry}}`/`{{productType}}` fields available — lead with an operational/category-pattern angle ("sellers like you") rather than list 1's brand-equity angle, so the two don't read as duplicates.

**Step 1 — Day 0**
Subject: noticed something on your {{productType}} listings
```
Hi {{firstName}},

I was looking at how {{companyName}} is doing in the {{industry}} space on Amazon and noticed a pattern that's common with sellers in this category: reviews that read like shipping or service complaints sitting inside the product reviews section.

Amazon's guidelines say those shouldn't count toward your star rating, but pulling them requires going through the right channel the right way.

Send me 1 ASIN and I'll run a free audit, no cost, no obligation.

Best,
Cüneyt / Starfix
```

**Step 2 — Wait 3 days**
Subject: {{industry}} sellers and off-topic reviews
```
Hi {{firstName}},

Following up. We work with a number of {{industry}} sellers and the pattern repeats: a few reviews per listing that are really about delivery time, packaging, or customer service, not the product itself.

Those are removable under Amazon's own Community Guidelines, but most sellers don't realize it or don't have time to chase it through official channels.

I can check 1 ASIN from {{companyName}} for free and show you exactly what we find before you decide anything.

Interested?

Best,
Cüneyt / Starfix
```

**Step 3 — Wait 3 days**
Subject: how the free audit works
```
Hi {{firstName}},

Quick clarification, since offers like this can sound too good to be true: there's no subscription and no upfront fee. Send 1 ASIN, we check it against Amazon's guidelines, and you get a short report on what may qualify for removal.

You only pay if something actually comes down. If nothing qualifies, the audit costs you nothing but a couple of minutes.

Want me to run it on one of {{companyName}}'s listings?

Best,
Cüneyt / Starfix
```

**Step 4 — Wait 3 days**
Subject: last note from me
```
Hi {{firstName}},

I'll keep this short — last email on this from me.

If cleaning up a few off-topic reviews on {{companyName}}'s listings isn't worth two minutes right now, totally understandable. If it is, send me 1 ASIN and I'll have the free audit back to you quickly, no obligation attached.

Either way, wishing you a strong quarter.

Best,
Cüneyt / Starfix
```

---

## SEQUENCE 3 — "Amazon USA Product Review"

**Target list:** Amazon USA Product Review (735 contacts) | **Segment:** Warm/pre-qualified, specific flagged review already identified
**Rationale:** A specific problematic review has already been found for each lead — the pitch is warmer and more concrete than lists 1/2, so it references the actual review instead of asking for an ASIN.

**Step 1 — Day 0**
Subject: a review on your listing worth checking
```
Hi {{firstName}},

While reviewing {{companyName}}'s Amazon listings, we came across a review currently sitting at {{rating}} stars that reads more like a shipping or service complaint than actual product feedback: "{{review}}"

Reviews like this don't comply with Amazon's Community Guidelines, and they're often eligible for removal through official channels.

I'd like to show you exactly why this one may qualify and what removing it could do for your rating, no cost, no obligation.

Want me to send over the details?

Best,
Cüneyt / Starfix
```

**Step 2 — Wait 3 days**
Subject: following up on that review
```
Hi {{firstName}},

Just circling back. The review I flagged, currently sitting at {{rating}} stars, still looks like it belongs to a delivery or service complaint rather than the product itself, which is exactly the kind of review Amazon allows sellers to request removal for.

We work strictly through official Amazon channels, no subscription, no fee upfront. You'd only pay if it's actually taken down.

Happy to walk you through why we think it qualifies. Want the details?

Best,
Cüneyt / Starfix
```

**Step 3 — Wait 3 days**
Subject: why this one may qualify
```
Hi {{firstName}},

To be specific: the review reads "{{review}}", and reviews focused on delivery, service, or unrelated issues rather than the product don't meet Amazon's guidelines for product reviews.

We've had this exact type removed for sellers across supplements, home goods, and beauty — over 5,000 reviews total. Because we've worked inside Amazon's case system for years, we know how to frame the request so it actually gets processed.

No cost to check this one for {{companyName}}. Want us to proceed?

Best,
Cüneyt / Starfix
```

**Step 4 — Wait 3 days**
Subject: should I close this out?
```
Hi {{firstName}},

Last note from me on this.

The {{rating}}-star review I flagged on {{companyName}}'s listing is still sitting there, and it likely qualifies for removal under Amazon's guidelines. Happy to move forward whenever you are, still no cost unless it's actually removed.

If it's not a priority right now, no worries, just let me know and I'll close this out.

Best,
Cüneyt / Starfix
```

---

## SEQUENCE 4 — "Amazon USA Product Review 2nd — Small/Medium Size Companies"

**Target list:** Amazon USA Product Review 2nd — Small/Medium (654 contacts) | **Segment:** Warm/pre-qualified, small-medium sellers, specific flagged review already identified
**Rationale:** Same warm "review already found" mechanic as Sequence 3, but tone softened and framed around approachability/no-retainer reassurance for smaller teams, with distinct subject lines/phrasing so overlapping leads don't see a duplicate.

**Step 1 — Day 0**
Subject: a quick heads-up about one of your reviews
```
Hi {{firstName}},

Hope things are going well at {{companyName}}. While looking through your Amazon listings, we spotted a review sitting at {{rating}} stars that reads more like a shipping or service complaint than feedback on the product: "{{review}}"

Reviews like that technically aren't supposed to count toward your rating under Amazon's own guidelines. We help small and medium sellers get them removed the right way, no subscriptions, no big retainers, just a simple free check.

Want me to walk you through it?

Best,
Cüneyt / Starfix
```

**Step 2 — Wait 3 days**
Subject: just a small follow-up
```
Hi {{firstName}},

Didn't want this to get lost, so a quick nudge. That {{rating}}-star review I mentioned still looks like it's really about delivery or service, not your product, which is exactly the kind of thing Amazon allows you to request removal for.

No pressure either way. If you'd like, I can explain exactly why it may qualify and what it would take, completely free, and you'd only pay us if it's actually removed.

Sound okay?

Best,
Cüneyt / Starfix
```

**Step 3 — Wait 3 days**
Subject: no subscriptions, just results
```
Hi {{firstName}},

Want to be upfront since we work with a lot of smaller teams: this isn't a subscription or a retainer. We flagged one specific review on {{companyName}}'s listing, "{{review}}", and think it has a real shot at removal under Amazon's guidelines.

We've helped sellers your size recover reviews like this across categories from supplements to home goods, and you only pay if it actually comes down.

Happy to send the full breakdown whenever it's convenient.

Best,
Cüneyt / Starfix
```

**Step 4 — Wait 3 days**
Subject: okay to close this one out?
```
Hi {{firstName}},

I'll keep this brief, last message from me on this one.

The review I flagged on {{companyName}}'s listing is still there, and it's a small thing to check but could make a real difference to your rating. If you'd like me to move forward, just say the word, still free to check either way.

If it's not the right time, totally fine, I'll leave it here.

Best,
Cüneyt / Starfix
```
