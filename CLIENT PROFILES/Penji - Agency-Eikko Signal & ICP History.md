# Penji — Agency-Eikko Signal & ICP History

Running record of every ICP and signal configuration run on the Gojiberry "Agency - Eikko" agent (id `29267`, list `45132` "Agency - Eikko leads"). Purpose: every time the ICP/signals get refreshed, whoever does it next can see exactly what's already been tried and its yield, instead of re-testing dead ideas or guessing what's new. Update this file **before** removing anything from the live agent.

**Also mirrored in Notion:** https://app.notion.com/p/3ca811e21c7f8152965be78cf622506e — filed under VA Command Center (Eikko's personal workspace) rather than Penji's own "dotpenji" Signal Tracker (`app.notion.com/p/dotpenji/8-17-26-Signal-Tracker-...`), since the connected Notion integration isn't authorized for the dotpenji workspace. Move/copy it there once that's reconnected, and keep both in sync on future rounds.

---

## Round 4 — live now (Round 2's config restored, 2026-08-28)

**Reason:** Round 3 was reverted a few hours after launch — Shekinah flagged it directly in Slack, with a screenshot of the Gojiberry agent dashboard showing 0 leads found on nearly every new signal (all 7 new keywords, all 3 new competitor pages, and Katelyn Bourgoin; only Dave Gerhardt and the two premium job-title signals showed any activity, and even those were minimal). Her guidance: adjust the signal, check what other reps are doing for ideas, and combine with other triggers rather than guessing blind.

Restored Round 2's exact ICP and all 15 signals (verbatim from the saved pre-Round-3 snapshot, byte-for-byte — same values, same order). Verified via a fresh `get_agent` read after the write.

**Worth noting for next time:** Round 3 was live for only a few hours before this feedback — far short of the ~3 days Round 2 took to show which of *its* swaps worked. Zero leads that fast doesn't necessarily mean the ideas were bad, just unproven. But Shekinah's instruction was explicit and Eikko acknowledged it ("noted po fix ko po"), so reverting now rather than waiting it out. If a Round 5 gets built, do it informed by what other reps' agents are actually running (Kim's config was already checked for Round 3's influencers — worth doing the same for Evi, Kristine, and Shekinah's own agents too) rather than another blind-guess batch of untried phrases.

---

## Round 3 — retired 2026-08-28, same day (reverted after a few hours)

**Reason for the refresh:** per Eikko's request — retire Round 2 in full (record it below), and build a genuinely new ICP + signal set rather than another partial swap. Also corrects a real gap: the ICP had been pulling Founder/CEO/President/Managing Director titles the whole time, despite Shekinah's Aug 17 correction (see `Penji - Agency Advisor Quick Reference.md` #3) explicitly saying to exclude Founders/Co-Founders and target marketing-specific titles instead. That correction was never actually applied to the live Gojiberry config until now — Round 2's lead data confirms it: 14 "Founder", 7 CEO-variant, 3 "President", 2 "Co-Founder" titles came through despite the rule.

**ICP:**
| Field | Value |
|---|---|
| Job Titles | Marketing Director, Head of Marketing, CMO, VP of Marketing, Director of Brand Marketing, Director of Growth Marketing, Director of Digital Marketing, Marketing Manager, Creative Director, Head of Creative |
| Industries | Marketing Services, Public Relations and Communications Services, Business Consulting and Services, Graphic Design |
| Company Sizes | 11-50 employees, 51-200 employees |
| Locations | United States |
| Company Types | Private Company |
| Ignored Companies | Design Pickle, Kimp, Superside |

Changes from Round 2's ICP: dropped Founder/CEO/President/Managing Director/Art Director/Client Success Manager/Director of Client Services entirely, replaced with pure marketing-leadership titles named in Shekinah's original correction but never configured. Industries shifted from Marketing/Advertising/Design Services (broad, and per the real `industry` field on Round 2 leads, mostly matched as "Advertising Services"/"Design Services"/"Marketing & Advertising") to two genuinely untried categories — PR/Communications and Business Consulting — plus Graphic Design. Company size dropped the 2-10 band (where the founder-only shops cluster) in favor of 11-50 + 51-200. Company type dropped "Startup."

**Signals (15):**
| Type | Value | Why |
|---|---|---|
| RECENTLY_CHANGED_JOB (premium) | new job-titles OR-string | Re-tied to the new ICP titles |
| RECENT_ACTIVITY (premium) | new job-titles OR-string | Re-tied to the new ICP titles |
| YOUR_PROFILE | Eikko's own profile | Structural, unchanged |
| INFLUENCER_PAGE_URL | Dave Gerhardt (`davegerhardt`) | Verified real (WebSearch), unused by Eikko before — ex-CMO, fits new Marketing Director/CMO ICP directly |
| INFLUENCER_PAGE_URL | Katelyn Bourgoin (`katebour`) | Verified real, unused before — customer/marketing research audience |
| COMPETITOR_PAGE_URL | Superside (`superside`) | Verified real. Was only in `ignoredCompanies` before, never used as an engagement signal — people following Penji's closest competitor is a strong intent signal |
| COMPETITOR_PAGE_URL | Design Pickle (`designpickle`) | Same rationale as Superside |
| COMPETITOR_PAGE_URL | Kimp (`getkimp`) | Same rationale as Superside |
| SEARCH_KEYWORD | "creative resourcing" | New phrase, untried |
| SEARCH_KEYWORD | "brand refresh" | New phrase, untried |
| SEARCH_KEYWORD | "pitch deck design" | New phrase, untried |
| SEARCH_KEYWORD | "marketing collateral" | New phrase, untried |
| SEARCH_KEYWORD | "campaign creative" | New phrase, untried |
| SEARCH_KEYWORD | "creative operations" | New phrase, untried |
| SEARCH_KEYWORD | "brand consistency" | New phrase, untried |

Applied 2026-08-28, verified persisted via a fresh `get_agent` read after write.

---

## Round 2 — retired 2026-08-28 (ran 2026-08-25 to 2026-08-28)

Partial swap of Round 1 (6 of 15 signals replaced — see Round 1 below for what was swapped out). Sourced **172 leads** in its ~3 days live (up from 85 at the point it was first measured). Final yield at retirement:

| Signal | Type | Leads sourced |
|---|---|---|
| Job-title activity match | RECENT_ACTIVITY (premium) | 34 |
| Job-title change match | RECENTLY_CHANGED_JOB (premium) | 21 |
| "hired a designer" | SEARCH_KEYWORD | 14 |
| Daniel Murray | INFLUENCER_PAGE_URL | 10 |
| Chris Do | INFLUENCER_PAGE_URL | 7 |
| Eikko's own profile | YOUR_PROFILE | 6 |
| "creative as a service" | SEARCH_KEYWORD | 5 |
| "design bottleneck" | SEARCH_KEYWORD | 3 |
| Canva | COMPETITOR_PAGE_URL | 2 |
| "creative team capacity" | SEARCH_KEYWORD | 2 |
| "creative bandwidth" | SEARCH_KEYWORD | 2 |
| Upwork | COMPETITOR_PAGE_URL | 1 |
| 99designs | COMPETITOR_PAGE_URL | 1 |
| "overflow design work" | SEARCH_KEYWORD | **0 — dead** |
| "white label design" | SEARCH_KEYWORD | **0 — dead** |
| *(LOOKALIKE, not a configured signal)* | — | 64 |

**Takeaway:** the two influencer-engagement signals (Chris Do, Daniel Murray) worked well — 17 leads combined, validating that signal type as worth using again with fresh people (see Round 3). Two of the three new keyword phrases from the Round 1→2 swap never produced anything; avoid similarly generic overflow/subscription-style phrasing going forward — the phrases that worked ("hired a designer," "creative as a service," "design bottleneck") all describe something a person would plausibly post in their own words, not product-adjacent jargon.

**ICP at the time:** Job Titles: Creative Director, Founder, CEO, Managing Director, President, Design Lead, Head of Creative, Art Director, Client Success Manager, Director of Client Services. Industries: Marketing, Advertising, Design Services. Company Sizes: 11-50 employees, 2-10. Locations: United States. Company Types: Private Company, Startup. Ignored Companies: Design Pickle, Kimp, Superside. (Unchanged from Round 1 — only signals were swapped, not ICP, on 2026-08-25.)

---

## Round 1 — retired 2026-08-25 (ran 2026-08-21 to 2026-08-25)

Original config from initial agent setup. 6 signals replaced 2026-08-25 for sourcing zero leads (see `Penji - End of Day Log.md`, 2026-08-25 entry, for the original incident notes). Yield at the time of replacement (measured against 85 leads):

| Signal | Type | Leads sourced |
|---|---|---|
| Job-title activity match | RECENT_ACTIVITY (premium) | 21 |
| Job-title change match | RECENTLY_CHANGED_JOB (premium) | 14 |
| "hired a designer" | SEARCH_KEYWORD | 6 |
| Eikko's own profile | YOUR_PROFILE | 5 |
| "creative as a service" | SEARCH_KEYWORD | 4 |
| Canva | COMPETITOR_PAGE_URL | 2 |
| Upwork | COMPETITOR_PAGE_URL | 1 |
| "creative team capacity" | SEARCH_KEYWORD | 1 |
| "design bottleneck" | SEARCH_KEYWORD | 1 |
| "unlimited design" | SEARCH_KEYWORD | **0 — dead, replaced** |
| "freelance designer" | SEARCH_KEYWORD | **0 — dead, replaced** |
| "design subscription" | SEARCH_KEYWORD | **0 — dead, replaced** |
| "in-house design team" | SEARCH_KEYWORD | **0 — dead, replaced** |
| "client renewals" | SEARCH_KEYWORD | **0 — dead, replaced** |
| Fiverr | COMPETITOR_PAGE_URL | **0 — dead, replaced** |

**ICP:** same as Round 2 (see above) — the ICP was never touched in Round 1→2, only in Round 2→3.

---

## All values used to date (do not repeat without a clear reason)

**SEARCH_KEYWORD:** unlimited design, freelance designer, design subscription, in-house design team, client renewals, hired a designer, design bottleneck, creative as a service, creative team capacity, creative bandwidth, white label design, overflow design work, creative resourcing, brand refresh, pitch deck design, marketing collateral, campaign creative, creative operations, brand consistency

**INFLUENCER_PAGE_URL:** Chris Do, Daniel Murray, Dave Gerhardt, Katelyn Bourgoin *(Justin Welsh, Scott Galloway, Jim Stengel are used on Kim's agent — verified real, still available if Eikko's agent needs more influencer signals later)*

**COMPETITOR_PAGE_URL:** Upwork, Fiverr, Canva, 99designs, Superside, Design Pickle, Kimp

**Job titles tried as the primary ICP:** Creative Director, Founder, CEO, Managing Director, President, Design Lead, Head of Creative, Art Director, Client Success Manager, Director of Client Services *(Rounds 1–2, restored as Round 4 — currently live)* → Marketing Director, Head of Marketing, CMO, VP of Marketing, Director of Brand Marketing, Director of Growth Marketing, Director of Digital Marketing, Marketing Manager, Creative Director, Head of Creative *(Round 3 only, reverted same day)*

---

**Last updated:** 2026-08-28
