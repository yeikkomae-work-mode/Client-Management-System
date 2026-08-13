# Cüneyt (Starfix) — Campaign Tracking

**Client:** Cüneyt (Elevate Commerce / Starfix)
**Platform:** Instantly
**Status:** 🟡 Trial — audit complete, optimization pending

---

## Performance Audit — Jun 1 to Aug 13, 2026

| Campaign | Emails Sent | Leads Contacted | Replies (Unique) | Bounces | Completed Leads | Opportunities | Opp. Value |
|---|---|---|---|---|---|---|---|
| Liste von Dennis | 400 | 389 | 4 | 8 | 140 | 2 | 2 |
| USA Seller | 366 | 366 | 0 | 7 | 90 | 0 | 0 |
| Sports & Fitness (sellervate) | 314 | 300 | 5 | 6 | 45 | 1 | 1 |
| UK Seller (starfix) | 284 | 284 | 3 | 1 | 88 | 3 | 3 |
| Starfix New US Leads 2026-07-29 | 78 | 78 | 0 | 2 | 0 | 0 | 0 |
| Baby (mixed) | 70 | 70 | 0 | 2 | 101 | 0 | 0 |
| Pet (mixed) | 57 | 57 | 2 | 0 | 107 | 0 | 0 |
| Amazon seller 2nd | 52 | 52 | 0 | 0 | 0 | 0 | 0 |
| Starfix New UK Leads 2026-08 | 36 | 30 | 0 | 1 | 0 | 0 | 0 |
| Sports & Fitness (mixed) | 23 | 23 | 0 | 1 | 102 | 1 | 1 |
| Amazon Seller 2cnd (2) | 19 | 13 | 0 | 2 | 0 | 0 | 0 |

**Totals:** 1,699 emails sent, 1,662 leads contacted, 14 unique replies, 30 bounces, 673 completed leads, 7 opportunities, value 7.

---

## Key Findings

**Deliverability:** Bounce rates mostly under ~3% per campaign. Two outliers — Liste von Dennis (8/400, ~2%) and USA Seller (7/366, ~2%) — worth watching but not yet at the ~5% concern threshold.

**Engagement blind spot:** No campaign shows any recorded opens across the board — open tracking is disabled or non-functional on every campaign, so open-rate data isn't usable right now. (Matches the earlier campaign config audit — several campaigns were set up with open tracking off by design; worth deciding deliberately rather than by default, since it's currently blocking any funnel visibility above reply rate.)

**Reply rates:** Low overall — best performer is Liste von Dennis and Sports & Fitness (sellervate) at 4–5 unique replies. Several campaigns (USA Seller, Starfix New US Leads, Baby, Amazon Seller 2nd/2cnd, Starfix New UK Leads) have zero replies despite meaningful send volume.

**Conversion gap:** Baby (mixed) and Pet (mixed) have high completed-lead counts (101, 107) but zero and low opportunities respectively — messaging/offer may not be converting even where the sequence completes. UK Seller (starfix) is the standout: only 284 leads contacted but 3 opportunities, the best conversion rate of any campaign in the set.

**Dead/underperforming campaigns:** Amazon seller 2nd, Amazon Seller 2cnd (2), and Starfix New UK Leads 2026-08 have very low volume and zero engagement — either too new to judge or candidates to pause/rework.

---

## Recommendations (from audit)

1. Enable open tracking (plan-permitting) to get real funnel visibility beyond reply rate.
2. Add more subject line / body variants for A/B testing, especially on zero-reply campaigns.
3. Refresh copy on campaigns with high completions but no opportunities (Baby, Pet, Sports & Fitness mixed) — the offer/CTA likely needs work, not just volume.
4. Clean lead lists to keep bounce rates from creeping toward the ~5% risk zone, particularly Liste von Dennis and USA Seller.
5. Investigate why UK Seller (starfix) is converting so much better than the rest — likely worth replicating that angle/copy into the underperforming campaigns.
6. Reassess or pause the lowest-volume, zero-engagement campaigns (Amazon Seller 2nd/2cnd, Starfix New UK Leads 2026-08) rather than letting them run passively.

---

**Last Updated:** 2026-08-13
