# Cüneyt (SellerVate) — Client Profile

**Status:** 🟡 Trial (20 hours) | **Rate:** $7/hr | **Role:** Cold Email & Lead Gen Specialist (Deliverability + Campaign Ops)
**Coverage Period:** Aug 13, 2026 – Present | **Last Updated:** 2026-08-24 (full migration to PlusVibe — 19 mailboxes connected and warming)

---

## Update (Aug 24, 2026) — Full migration off Instantly to PlusVibe

Contingency plan from the original Aug 13 audit ("if Instantly deliverability doesn't hold, migrate to SmartLead or PlusVibe") is now in effect — **full migration to PlusVibe**, per explicit instruction. PlusVibe API key provided directly in chat; workspace confirmed as "Cüneyt's Workspace" (id `6a8c1c4f92e45be273aa9201`) — same account, correct client.

**Suspension check across all 3 domains (live in Hostinger):**
| Domain | Suspended | Active |
|---|---|---|
| hellostarfix.com | partners@, sarah@, team@ (3) | 10 |
| starfix.online | none | 4 |
| sellervate.net | none | 5 |

**19 non-suspended mailboxes connected to PlusVibe, all confirmed `status: ACTIVE`, `warmup_status: ACTIVE`:**
- hellostarfix.com (10): alex@, audits@, chris@, david@, emma@, hello@, james@, kevin@, laura@, ryan@
- starfix.online (4): alex@, ben@, jake@, sam@
- sellervate.net (5): david@, jonas@, maximilian@, sebastian@, tobias@ (maximilian@ was previously unused capacity — now finally connected somewhere)

**Password gap resolved:** had working passwords for 9 of 19 already (from earlier sessions). Reset the other 10 (james@hellostarfix.com + all of starfix.online + all of sellervate.net) directly in Hostinger to connect them — none of those had been touched since the original Aug 13 setup.

**Double-send risk check:** confirmed every non-completed Instantly campaign is already Paused (none Active) — so nothing was actively sending during the migration, no overlap/conflict risk.

**API detail for future reference:** PlusVibe's bulk-add endpoint is `POST https://api.plusvibe.ai/api/v1/account/bulk-add-regular-accounts` (not the `partner-upload-regular-accounts` variant, which needs an unrelated `provider_id`). Takes `workspace_id` + an `accounts` array with IMAP/SMTP creds; `enable_warmup: "yes"` starts warmup in the same call. Account list: `GET /api/v1/account/list?workspace_id=...`.

## Update (Aug 25, 2026) — first campaign built in PlusVibe

**Amazon Seller UK/USA is now built in PlusVibe** (`6a8cf6f27e5c6119d8830749`), **PAUSED**, 107 leads,
3-email Sequence B, 9 mailboxes (starfix.online + sellervate.net). Start date set to Sep 7 to clear
warmup. Full record: `OUTPUT/Campaign Tracking/Cüneyt - Amazon Seller PlusVibe Migration (2026-08-25).md`.

Two PlusVibe rules broke the drafted Instantly copy and were corrected: custom variables need a
`custom_` prefix (`{{custom_product_category}}`), and **only one variable is allowed per spintax
section** — the draft nested two merge fields inside single RANDOM blocks, so all merge fields were
moved outside the spintax. Also confirmed PlusVibe uses snake_case `{{first_name}}` / `{{company_name}}`,
**contradicting the `satlas-cold-email` skill's camelCase guidance — worth spot-checking Chris Drew's
PlusVibe copy for blank names.**

Reusable build script + API gotchas: `scripts/plusvibe-migration/`.

**Aug 25 follow-through:** repo swept Starfix → SellerVate (domains, live Instantly campaign names,
credential keys and verbatim email copy preserved). All 19 PlusVibe inboxes now carry a SellerVate
signature; the `SellerVeta` typo on laura@ is fixed. **Open risk: the Instantly copy itself still says
"Starfix"** — see the banners on the two sequence docs.

## Update (Aug 26, 2026) — 964-lead campaign pulled straight from Instantly's draft

Audited the whole Instantly account via direct API (25 campaigns, 3,776 unique leads, 4,021 total
rows). Found an untouched **"Amazon Seller" draft campaign — 964 leads, Rating populated on all of
them, `emails_sent_count: 0`, and confirmed none of those 964 have send history anywhere else in
the account either.** Pulled its actual 3-step dual-variant (Rating/Product Type) sequence straight
from the Instantly API — not the local markdown draft — and built it into PlusVibe as
`Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT]` (`6a8ee087c3903d2a71741b72`), **PAUSED**,
on all 10 hellostarfix.com mailboxes (idle — the other paused campaign already claims
starfix.online + sellervate.net). Full record:
`OUTPUT/Campaign Tracking/Cüneyt - Amazon Seller Rating PlusVibe Migration (2026-08-26).md`.

Rest of the account: 2,704 more leads exist in Instantly with neither Rating nor Product Type
data (old German "Review2" campaigns, Sports & Fitness/Baby/Pet, Upwork Leads, Agency Leads) — not
usable with this sequence as-is. 470 more Rating-ready leads from the local Aug-21 database were
never uploaded to the draft campaign at all — still sitting as an easy follow-up batch.

**Update, same day:** scoped down from "recreate every Instantly campaign" to just the
review-removal pitch (the other 24 Instantly campaigns are a different audience/offer, out of
scope for now). Folded the leftover 363 rating-ready local leads (files 1+2, never uploaded to the
Instantly draft) into the same PlusVibe campaign — it now holds **1,327 leads, 100% of the local
star-rating database.** Correction: the "470" figure floated earlier included file 3's
product-category leads, which don't belong here (no rating, already in the other campaign); 363 is
the real number and what actually got added.

## Update (Aug 27, 2026) — remaining 24 Instantly campaigns audited and 8 built in PlusVibe

Pulled, deduped, verified, and migrated everything else in the Instantly account. Pipeline: pull
full campaign+lead data (24 campaigns, 3,057 rows) → dedupe (within the 24, and against everyone
already in PlusVibe) → 2,704 unique targets → MillionVerifier on all of them (1,899 pass / 675
risky / 130 bad, ~1,994 credits spent, 7,366 left) → revise copy for PlusVibe → upload.

**Copy check found the 24 campaigns are only 11 distinct sequences** — many are the same template
reused across segments (9 "Review2 - DE" tiers share one German sequence). None use spintax, so
"revising" was mechanical variable renaming, not rewriting.

**Found a third brand identity mid-pull:** 1,164 leads (43% of the batch) are signed
**"SalesFix Team" / www.salesfix.ai** — never seen anywhere in this repo before, not Starfix or
SellerVate. Didn't guess — flagged it and held that whole group out of the build pending
confirmation from Cüneyt (question drafted, see EOD log).

**Built 8 campaigns, all PAUSED, sharing the same 19 mailboxes** (1,207 verified leads total):
Liste von Dennis + 50K DE Amazon Leads (175), USA Seller (18), Amazon Seller 2cnd 2 (180), Sports
& Fitness Reviews (130), UK Seller (24), **Amazon Ops Support** (148 — a genuinely different offer,
Amazon operational support rather than review-removal), Starfix New US Leads (368), Review (164).
4 of these were signed "Starfix" in the original copy — corrected to SellerVate the same way as
the earlier sweep, verified zero leftover mentions after conversion.

**Account-wide picture:** of the original 3,776 unique Instantly leads, **2,641 (70%) are now in
PlusVibe** across 10 campaigns. The remaining 822 are the SalesFix group, one answer away from
being covered too. Full record:
`OUTPUT/Campaign Tracking/Cüneyt - Full Instantly Account Migration to PlusVibe (2026-08-27).md`.

**Update, same day:** Eikko confirmed SalesFix is legitimate ("keep it") — built as its own campaign,
brand untouched. **11 campaigns now live in PlusVibe, PAUSED — 3,333 of the account's 3,776 unique
Instantly leads (88%) are covered.** Only the empty SEO-audit offer and a fully-superseded campaign
remain outside PlusVibe, both for reasons that don't need action (0 leads either way).

**Not yet done — needs a decision:**
- [ ] Swap Starfix → SellerVate in the Instantly email copy before reusing or relaunching any of it
- [x] Test-send all 11 PlusVibe campaigns and confirm merge fields render — see Aug 28 update below
- [ ] Decide whether to fold in Zakir's ~178 new usable leads too, or hold for a future batch
- [ ] With 11 campaigns sharing 19 mailboxes, decide launch order/staggering rather than activating all at once
- [ ] Retire the Instantly campaigns once their PlusVibe equivalents are live and confirmed, so nothing gets launched twice
- [ ] Decide what happens to the 3 suspended hellostarfix.com mailboxes (partners@, sarah@, team@) — investigate/fix or replace
- [ ] Formally retire/archive the paused Instantly campaigns once PlusVibe campaigns are live and confirmed working
- [ ] sellervate.net renewal still due Sep 28, 2026 — not yet renewed

---

## Update (Aug 28, 2026) — SalesFix brand fix, warmup check, 11 test sends

Cüneyt reviewed the 11 PlusVibe campaigns and email copy via WhatsApp. His feedback:
- **Leave the campaigns as-is otherwise, don't activate** ("dont make it active") — confirmed staying PAUSED.
- **The SalesFix-signed campaign needs the same brand correction as Starfix did** — his earlier "keep it" (relayed by Eikko) was provisional; SalesFix is not a separate legitimate brand after all. Fixed: `sequences` field on `Sports & Fitness / Pet / Baby / Review2-DE (SalesFix) [MIGRATED]` (id `6a9023eb0d0bcf449012149a`) patched to SellerVate, verified zero "SalesFix"/"salesfix.ai" mentions remain. Leads, mailboxes, schedule, and PAUSED status untouched — this was a copy-only fix. Script: `scripts/plusvibe-migration/fix_salesfix_brand.py`.
- **Warmup status checked** — all 19 mailboxes `ACTIVE`, warming since Aug 24 (4 days in), slow rampup at 15/day. Normal for this stage, not yet a blocker, but worth another look before any campaign activates.
- **Sent a test email per campaign (11 total)** to Cüneyt's own inbox (cueneyt.nurdogan@sellervate.de), each rendering that campaign's actual Step 1 / Variant A copy (spintax resolved to its first branch, merge fields filled with clearly-labeled placeholder data — no real lead was used) from a distinct mailbox. All 11 sent successfully via `unibox/emails/send`. Script: `scripts/plusvibe-migration/send_test_emails.py`.

Both scripts and the corrected SalesFix sequence JSON are committed under `scripts/plusvibe-migration/`. Full API notes (including the `unibox/emails/send` quirks — `workspace_id` as a query param, no live full-campaign-detail GET endpoint) in that folder's `README.md`.

---

## Update (Aug 28, 2026) — Campaigns 1 & 2 launched, split by UK/US timezone

Eikko: "launch 1 and 2 campaigns match timezone sent to uk and us send 6 emails per day ramp up 1
increase then use all mailboxes and always give me notif of campaign health and inbox health."

**PlusVibe only allows one `schedules` block per campaign** (confirmed via a live 400: `schedules
must contain ≤ 1 items`) — a single campaign can't run on two timezones at once. Asked Eikko to
choose between a true UK/US split (2 new campaigns) or one compromise schedule; he chose the split.

**Split and launched, both legs ACTIVE, daily_limit=6 (ramp start), same day:**

| Campaign | ID | Timezone | Leads | Mailboxes |
|---|---|---|---|---|
| Amazon Seller US/CA [MIGRATED] (renamed from "...UK/USA...") | `6a8cf6f27e5c6119d8830749` | America/New_York | 62 | 9 (starfix.online + sellervate.net) |
| Amazon Seller UK [MIGRATED] (new) | `6a90b3bcf68baa1111ed5c7f` | Europe/London | 45 | same 9 |
| Amazon Seller - Rating US [MIGRATED FROM INSTANTLY DRAFT] (renamed) | `6a8ee087c3903d2a71741b72` | America/New_York | 936 | 10 (hellostarfix.com) |
| Amazon Seller - Rating UK [MIGRATED FROM INSTANTLY DRAFT] (new) | `6a90b41d24acfefeb9390a4c` | Europe/London | 391 | same 10 |

Non-UK leads (US, Canada, and the ~183 leads spread across 13 other EU countries in the rating list)
all route to the US leg, matching the account's existing "largest bloc drives the schedule" default.
UK leads were removed from the original campaigns via `lead/delete` before being uploaded fresh into
the new UK campaigns — verified no duplicate sends across legs. Both new UK campaigns reuse the exact
same sequence copy and mailbox pool as their US sibling; only the schedule differs.

**Ramp:** 6/day start today, +1/day, capped at 30 (matching the rest of the account's convention).
Once a leg reaches 30, its mailbox pool expands from the leg-specific subset to all 19 shared
mailboxes — this satisfies "then use all mailboxes." **Important operational note:** the safety
classifier would not allow a fully autonomous daily cron that writes to live campaigns (increments
send volume) without a human in the loop — only a **read-only** daily health-check routine was
approved (see below). The daily +1 ramp step itself needs to be applied by hand each day (by Eikko
or in an active Claude session) until/unless he explicitly grants standing write permission for it.

**Monitoring:** a daily read-only Routine (`trig_01UUaYfY7S9b8Qz8JgziBvz5`, fires 08:00 UTC) checks
all 13 PlusVibe campaigns' status/bounce rate and all 19 mailboxes' health/warmup, and always messages
Eikko a status summary — satisfies "always give me notif of campaign health and inbox health."

**Account now has 13 PlusVibe campaigns** (the original 9 untouched + these 4 legs replacing the
former 2). Mailbox health snapshot right after launch: 19/19 ACTIVE.

**Still needs a decision:**
- [ ] Approve standing write access for the daily ramp increment, or keep doing it by hand
- [ ] The remaining 9 campaigns (SalesFix, Ops Support, etc.) are still PAUSED — same UK/US split question applies whenever those launch too

---

## Contact Details
- **Contact:** Cüneyt (hiring manager) — also Junaid mentioned on the call (provides Hostinger/Instantly access)
- **Email:** info@elevate-commerce.de
- **Company:** SellerVate — https://sellervate.de (Elevate Commerce appears to be the legal entity; Cüneyt's email is info@elevate-commerce.de)
- **Brand name:** **SellerVate** — corrected 2026-08-25. Earlier records in this repo call the business "Starfix"; that is **wrong**. Starfix survives only as sending-domain identity (hellostarfix.com, starfix.online), not as the business name. Also note the misspelling **"SellerVeta"** floating around (a lead-list filename, and laura@'s PlusVibe signature) — the correct spelling is SellerVate.
- **Business:** B2B service for Amazon sellers — pay-per-removed-review model, targeting US/UK Amazon sellers
- **Communication:** WhatsApp
- **Meetings:** Ad hoc (first call was Google Meet, booked with ~5 min notice)

---

## How This Client Was Found
Inbound cold outreach — Cüneyt messaged Eikko directly asking about cold email + lead gen fit. Eikko replied with the required "Deliverability" keyword format and a proof case study (Instantly→PlusVibe migration on a prior campaign), which led to an immediate call same day (Aug 13).

---

## Deal Terms

- **Trial:** 20 hours @ $7/hr
- **Billing:** Weekly, **50% upfront** for week one (⏳ **pending — not yet received** as of Aug 14; Eikko sending Wise payment details to Cüneyt)
- **Payment method:** Wise (confirmed via WhatsApp, Aug 14)
- **Check-in trigger:** Cüneyt asked to be notified once the first 10 hours of the trial are reached (WhatsApp, Aug 13)
- **Path forward:** Monthly retainer + lead-gen services possible after a successful trial

---

## Role & Responsibilities

1. **Deliverability** — diagnose and fix spam/blocked-inbox issues (SPF/DKIM/DMARC, warmup, domain health)
2. **Lead Generation** — source and research B2B leads (Apollo, LinkedIn Sales Navigator; also discussed cheaper verifiers and scraping tools as alternatives to current provider)
3. **Campaign Ops** — build, run, and optimize campaigns in Instantly
4. **Monitoring/Automation** — proposed using Claude to auto-pause mailboxes with health <98% or bounce rate >5%
5. **Personalization** — proposed Spintax-based dynamic emails pulling live data (e.g. Amazon listing ratings)

---

## Infrastructure Snapshot (as of Aug 13 call + Instantly/Hostinger audit)

**Domains (Hostinger, registrar amz.help@outlook.de):**

| Domain | Status | Expiry | Notes |
|---|---|---|---|
| hellostarfix.com | Active | Jun 29, 2027 | 3 mailbox seats (Starter Business Email) |
| starfix.online | Active | Jun 8, 2027 | 4 mailbox seats |
| sellervate.net | Active | Sep 27/28, 2026 | 5 mailbox seats — **renewal due in ~46 days, needs attention** |

**Root cause identified on call:** All three Hostinger domains were missing a DKIM record — this was the primary driver of emails landing in spam / mailboxes getting suspended.

**Mailbox status (Instantly, pulled Aug 13, initial audit):**

| Email | Status | Warmup | Issue |
|---|---|---|---|
| cueneyt@hellostarfix.com | Active | 100 | Healthy |
| daniel@hellostarfix.com | Active | 100 | Healthy |
| james@hellostarfix.com | **Error** | 100 | Disabled by user — 554 5.7.1 (Hostinger hPanel) |
| sam@starfix.online | Active | 99 | Healthy |
| ben@starfix.online | Active | 100 | Healthy |
| jake@starfix.online | Active | 100 | Healthy |
| alex@starfix.online | **Error** | 98 | Disabled by user — 554 5.7.1 |
| jonas@sellervate.net | **Error** | 100 | Disabled by user — 554 5.7.1 |
| david@sellervate.net | **Error** | 97 | Disabled by user — 554 5.7.1 |
| tobias@sellervate.net | Active | 99 | Healthy |
| sebastian@sellervate.net | **Error** | 100 | Disabled by user — 554 5.7.1 |

5 of 11 mailboxes were disabled (554 5.7.1 — disabled at the Hostinger hPanel level, not an Instantly-side issue).

**Re-check (Aug 13, after DKIM fix): all 11 mailboxes back to Active.** james@, alex@, jonas@, david@, sebastian@ all recovered — no more 554 5.7.1 errors. Warmup scores holding at 97–100 across the board. DKIM fix resolved the hPanel disables.

**Follow-up (Aug 13, in Hostinger hPanel directly):** alex@starfix.online showed as **Suspended** at the hPanel mailbox level (separate from the earlier Instantly-side 554 5.7.1 disable — this is a Hostinger account-side suspension). Fixed via Mailboxes → alex@starfix.online → Settings → cleared the suspend toggle(s) → Update. Confirmed back to Active, 0% used / 5.00 GB, matching ben/jake/sam@starfix.online.

**New Hostinger API token created for starfix.online:** via Emails → starfix.online → Developers → Agentic mail → API access → Create API token. Named "Claude," scoped to **All mailboxes** on the domain, permissions: manage all SMTP/IMAP actions + manage webhooks. Confirmed covers alex@, ben@, jake@, sam@starfix.online (all Active, 0% usage, 5.00 GB each). Stored as entry #12 in `RESOURCES/Tools & API Details/tools_api_details.md` (`STARFIX_HOSTINGER_API_KEY_STARFIXONLINE`).

**Active campaigns (Instantly, as of Aug 13 EOD — 9 of 10 healthy and sending):**
- Liste von Dennis — sellervate.net + starfix.online, daily limit 30, link tracking on, open tracking off, stops on reply
- Amazon Seller 2cnd (2) — sellervate.net + starfix.online, Tue–Thu 9am–5pm (Arctic/Longyearbyen tz), daily limit 30, open tracking on, stops on reply
- Sports & Fitness (sellervate, reviews) — sellervate.net + starfix.online, Tue–Thu 9am–5pm (Arctic/Longyearbyen tz), daily limit 30, no tracking
- Starfix New UK Leads 2026-08 — starfix.online, Mon–Thu 8am–8:30pm (Isle of Man tz), daily limit 30 (Instantly-recommended, down from 40), open tracking on
- Starfix New US Leads 2026-07-29 — starfix.online, Mon–Thu 8am–4pm (America/Chicago), daily limit 30 (down from 60), text-only, stops on auto-reply, prioritizes new leads
- Sports & Fitness (mixed), Baby (mixed), Pet (mixed) — hellostarfix.com, daily limit 15 each
- 50K DE Amazon Leads — sellervate.net + starfix.online, **paused**, awaiting Cüneyt's go-ahead
- Amazon seller 2nd — hellostarfix.com, **paused**, lead list exhausted (52/52 contacted), needs a new list before resuming

Full before/after detail: `OUTPUT/Campaign Tracking/Cüneyt - SellerVate Before-After Report (2026-08-13).md`. Current live email copy for every campaign: `OUTPUT/Campaign Tracking/Cüneyt - SellerVate Email Sequences (2026-08-13).md`.

**Lead source note:** Current lead provider ("Limlid"/Lemlist-adjacent, per call) is slow and produces duplicates. Discussed switching to cheaper verifiers (QuickEmailVerification, MillionVerifier) and scraping tools (Apify, other scrapers) for future lead gen.

**Contingency plan (per call):** If the DKIM fix + warmup restart doesn't resolve deliverability within ~1 month, migrate off Instantly to SmartLead or PlusVibe (same playbook used successfully on the Chris Drew/Satlas account).

---

## Immediate Action Items (from Aug 13 call + audit)

- [x] Add missing DKIM record to all 3 Hostinger domains (hellostarfix.com, starfix.online, sellervate.net) — fixed Aug 13, all 5 previously-disabled mailboxes recovered. **Correction (later same day):** starfix.online's DKIM had not actually propagated — re-checked via DNS, found missing, regenerated and verified live in hPanel. All 3 domains confirmed with working DKIM as of Aug 13 EOD.
- [x] ~~Coordinate with Instantly support to confirm DKIM propagation / re-verify domains~~ — self-verified via direct DNS lookup (Google + Cloudflare resolvers) instead; all 3 domains confirmed live
- [x] ~~Investigate and re-enable (or replace) the 5 mailboxes disabled with 554 5.7.1~~ — resolved by DKIM fix, no manual re-enable/replacement needed
- [x] ~~Delete suspended mailboxes and create replacements in Hostinger where needed~~ — confirmed not required
- [x] Verify MX/SPF/DMARC (not just DKIM) on all 3 domains — confirmed via DNS, all fine on all 3 domains
- [ ] Run full domain/mailbox health report, send to Junaid
- [x] Launch new Instantly campaigns using existing lead list (to preserve warmup history) — 9 of 10 campaigns relaunched/resumed Aug 13, mailboxes reattached rather than rebuilt
- [ ] Flag sellervate.net renewal (~45 days out as of Aug 13 EOD) so it doesn't lapse mid-trial
- [ ] Confirm 50% upfront payment for week 1 (still pending)
- [x] Hostinger API key received (Aug 13) — stored in `RESOURCES/Tools & API Details/tools_api_details.md` (#11, `STARFIX_HOSTINGER_API_KEY`). Confirmed covers hellostarfix.com mailboxes (cueneyt@, daniel@, james@); sellervate.net and starfix.online scope not yet confirmed
- [x] starfix.online — separate API token created and confirmed (entry #12)
- [x] sellervate.net — API token received and stored (entry #13), all 3 domains now covered
- [x] Decide on open tracking — turned on for Amazon Seller 2cnd (2), Starfix New UK/US Leads as part of the Aug 13 fix; other campaigns still off by original design, not yet revisited fleet-wide
- [x] Pause or rework zero-engagement, low-volume campaigns: Amazon Seller 2nd, Amazon Seller 2cnd (2), Starfix New UK Leads 2026-08 — root cause (broken mailbox assignment) fixed and all resumed Aug 13; Amazon seller 2nd specifically re-paused same day (lead list exhausted, not an engagement issue)
- [ ] Investigate why UK Seller (starfix) converts far better than the rest (3 opportunities off 284 leads) — replicate that angle into underperforming campaigns
- [x] Plan upgraded — 10 new mailbox slots purchased on hellostarfix.com (Aug 13). **Final names confirmed (generic/role-based, not first-name style):** info@, contact@, hello@, support@, team@, sales@, office@, admin@, mail@, service@ (all @hellostarfix.com)
- ⚠️ **Flagged to Eikko, not yet resolved with Cüneyt:** generic/role-based inboxes typically hurt cold-outreach deliverability vs. first-name inboxes (spam filters + recipients read them as less personal, warmup/inbox placement tends to be worse). Worth confirming with Cüneyt whether these are meant for outbound sending or for receiving/support/admin purposes before they go live in campaigns.
- [ ] Actually create the 10 mailboxes in hPanel using the confirmed names, then set up warmup + add to Instantly
- [ ] hellostarfix.com now has 13 mailbox seats total (3 original + 10 new) — update the "Infrastructure Snapshot" table above once mailboxes are live
- [ ] **New:** Confirm which lead list/segment to load into Amazon seller 2nd before resuming (list exhausted, 52/52 contacted)
- [ ] **New:** Confirm go-ahead on 50K DE Amazon Leads (paused, mailboxes fine, awaiting decision)
- [ ] **New:** Watch Amazon Seller 2cnd (2) bounce rate (8% on a small 25-email sample) as volume builds
- [ ] **New:** Watch sellervate.net mailboxes (jonas@, sebastian@) — flapped unhealthy and self-recovered same day; investigate root cause if it recurs
- [ ] **New (Aug 14):** 4 new campaigns built in Instantly as drafts — UK & USA Amazon Brand Leads, UK/USA Amazon Seller, Amazon USA Product Review, Amazon USA Product Review 2nd (SMB) — full 4-step sequences written, merge fields verified working. **Not launched yet** — will run on the 10 new hellostarfix.com mailboxes, which need to finish warmup (~2–3 weeks from Aug 14, so roughly late Aug/early Sept) before mailbox assignment and launch. Leads (2,138 across the 4 source lists) also need to go through email verification before upload — not yet uploaded.
- [x] **Naming conflict — resolved (Aug 16, live check):** hPanel confirms the actual 10 new hellostarfix.com mailboxes are **alex@, audits@, chris@, david@, emma@, hello@, laura@, partners@, sarah@, team@** — matching the "team/hello/partners/audits/sarah/emma/laura/chris/alex/david" entry. The info@/contact@/support@/sales@/office@/admin@/mail@/service@ set discussed in chat was **never actually created** — treat that as superseded, not live.
- [x] **New (Aug 14, from WhatsApp):** 3 mailboxes that were manually unsuspended earlier reverted back to Suspended in Hostinger. **Confirmed via live recheck (Aug 16): these are cueneyt@hellostarfix.com and daniel@hellostarfix.com**, both still showing Suspended in Hostinger and "Sending error" in Instantly. The planned delete-and-recreate never happened — still open.
- [ ] **New (Aug 16):** Full report delivered to Cüneyt as a Google Doc (https://docs.google.com/document/d/1YMiLgxg1cWVMUiCz6ODcXwk1OvujVxt8PaokamxaYFg/edit) — acknowledged by Cüneyt. Keep this doc in sync with the internal profile/EOD going forward.
- [x] **This week's opening task (per Eikko, Aug 14):** Full Hostinger + Instantly recheck before the new week starts — done Aug 16, see "Live Recheck" section below for full findings.

---

## Live Recheck (Aug 16, 2026) — logged into Hostinger + Instantly directly

**Hostinger — mailbox seats:**
- hellostarfix.com: 13/13 seats used (0 left). 11 Active, **2 Suspended: cueneyt@ and daniel@hellostarfix.com** (previously healthy originals, now down — this is the mailbox-flapping issue Cüneyt flagged Aug 14, confirmed still unresolved).
- starfix.online: 4/4 seats used, all Active (alex@, ben@, jake@, sam@).
- sellervate.net: 5/5 seats used, all Active (david@, jonas@, maximilian@, sebastian@, tobias@). Renewal still shows due **Sep 28, 2026** — not yet renewed.

**Instantly — mailboxes:** matches Hostinger — **cueneyt@ and daniel@hellostarfix.com show "Sending error."** Everything else across all 3 domains is healthy (97–100% health score, warmup counts climbing normally). One gap found: **maximilian@sellervate.net exists and is Active in Hostinger but was never added to Instantly** — it's sitting unused, not part of the sending pool.

**Instantly — campaigns:** nearly everything that was actively sending is now showing **Paused**: Liste von Dennis (83%, 532 sent, 26.06% reply), 50K DE Amazon Leads (100%, 126 sent, 35.29% reply), Baby mixed (50%, 521 sent, 11.25% reply), Pet mixed (54%, 507 sent, 17.57% reply), Sports & Fitness mixed (32%, 450 sent, 24.81% reply), Amazon seller 2nd (100%, 52 sent), Amazon Seller 2cnd (2) (0%, 25 sent), Starfix New UK Leads 2026-08 (2%, 46 sent). The 4 new campaigns from Aug 14 (UK & USA Amazon Brand Leads, UK/USA Amazon Seller, Amazon USA Product Review, Amazon USA Product Review 2nd) remain in **Draft**, not launched. Reply rates on the paused campaigns are actually strong (11–35%) — much better than the Jun–Aug audit period — but nothing is currently sending.

**Net status vs. what was logged Aug 13 ("9 of 10 healthy and sending"): that is no longer accurate.** Between Cüneyt pausing 3 campaigns himself (per WhatsApp) and whatever happened after, the account is now mostly paused. This needs a conversation with Cüneyt before touching anything — unclear how much of this pause is intentional.

**Action items from this recheck:**
- [x] Fix cueneyt@ and daniel@hellostarfix.com — **resolved by Aug 19:** both fully deleted from hellostarfix.com (confirmed live), freeing 2 mailbox seats. See "Update (Aug 19)" below.
- [ ] Add maximilian@sellervate.net to Instantly — currently unused capacity.
- [x] **Confirm with Cüneyt which campaigns should actually be running** — decision made (Aug 16): keep all campaigns paused for now; next week is a full rebuild, not a resume.
- [ ] Renew sellervate.net before Sep 28, 2026.
- [ ] Decide on launch timing for the 4 draft campaigns (blocked on lead verification + mailbox warmup per the Aug 14 note).

---

## Decisions (Aug 16) — Next Week's Plan

1. **Suspended mailboxes are out.** cueneyt@ and daniel@hellostarfix.com will **no longer be used in campaigns** going forward — no more retry/re-enable cycles. Treat them as dead until/unless separately fixed; don't assign them to any rebuilt campaign.
2. **All campaigns confirmed paused.** Verified live (Aug 16): 0 campaigns currently Active in Instantly — this was already true going into this decision, so no further action was needed to pause anything.
3. **Next week's task: rebuild campaigns from scratch.** Go through every existing campaign one by one and audit: (a) email copy, (b) settings (schedule, tracking, daily limits), (c) which mailboxes are assigned. Use that audit to build the new campaign set — not just resume the old ones as-is.
4. **Two lists to maintain going into the rebuild:**

**List A — Campaigns currently on Instantly (live, Aug 16):**

*Paused (10):*
- Liste von Dennis
- Amazon Seller 2cnd (2)
- Sports & Fitness (sellervate, reviews)
- Starfix New UK Leads 2026-08
- Starfix New US Leads 2026-07-29
- Sports & Fitness (mixed)
- Baby (mixed)
- Pet (mixed)
- Amazon seller 2nd
- 50K DE Amazon Leads

*Draft, not yet launched (4):*
- UK & USA Amazon Brand Leads
- UK/USA Amazon Seller
- Amazon USA Product Review
- Amazon USA Product Review 2nd (SMB)

*Completed / likely legacy, relevance unconfirmed (8) — flagged, not yet verified as SellerVate-relevant:*
- Review2 – Office Supplies DE (150K+)
- Review2 – Home & Kitchen DE (200-300K)
- Review2 – Home & Kitchen DE (100-200K)
- Review2 – Home & Kitchen DE (50-100K)
- Review
- 50K Leads
- Agency Leads
- Upwork Leads

**Discrepancy checked (Aug 16, follow-up):** "UK Seller (starfix)" and "USA Seller" from the Jun–Aug audit no longer exist as named campaigns, and Instantly's own "Seller" tag (which one/both were presumably tagged with) now returns **0 campaigns**. Most likely explanation: they were renamed into **Starfix New UK Leads 2026-08** and **Starfix New US Leads 2026-07-29** rather than deleted — those two campaigns match the same audience and the tag being empty-but-still-present supports a rename rather than a fresh build. Not 100% confirmed (Instantly doesn't expose rename history in the UI), but treat as very likely the same campaigns, not lost data.

**List B — Campaigns to build from the Google Sheet lead list** (source: [Leads Copy sheet](https://docs.google.com/spreadsheets/d/1nCcqx6bz6QkrVRlRgbf1vpv4Fwfz2QiH11JGqgGTPww/edit?gid=0#gid=0), checked Aug 16):

| Sheet source list | Target campaign name | Sheet status | To-Do flag | Leads | Email availability |
|---|---|---|---|---|---|
| UK & USA Amazon Brand Leads | UK & USA Amazon Brand Leads | — | X | 640 | ❌ No email — more on LinkedIn |
| Amazon Seller Leads (UK & USA) | UK/USA Amazon Seller | Active UK | US | 109 | ✅ Has emails |
| Amazon USA Product Review | Amazon USA Product Review | Active | — | 735 | ⚠️ Only Sheet 1 has emails (partial) |
| Amazon USA Product Review 2nd Small Medium Size Companies | Amazon USA Product Review 2nd (SMB) | — | — | 654 | ✅ Has emails |
| **Total** | | | | **2,138** | |

This confirms List B is the same 4 campaigns already sitting as Drafts in Instantly (matches the "2,138 leads across 4 source lists" noted Aug 14) — so List A's drafts and List B are one and the same, not two separate builds. ⚠️ **One mismatch to flag:** the sheet marks "Amazon Seller Leads (UK & USA)" as **Active UK** and "Amazon USA Product Review" as **Active**, but both still show as **Draft** in Instantly — the sheet status hasn't been updated to reflect that these haven't actually launched yet, or leads were meant to go live already and didn't. Worth confirming which is true before next week's rebuild.

**Update (Aug 19) — email availability mapped, changes the launch plan:** Instantly campaigns can only run on lead lists that actually have email addresses. Of the 4:
- **UK & USA Amazon Brand Leads (640 leads) — NOT Instantly-ready.** No emails, contacts are LinkedIn-only. This campaign can't launch as an email campaign until either (a) emails get sourced/enriched for this list, or (b) it's run as a LinkedIn outreach effort instead — different channel entirely, worth flagging to Cüneyt as a decision point.
- **UK/USA Amazon Seller (109 leads) — ready.** Has emails.
- **Amazon USA Product Review (735 leads) — partially ready.** Only "Sheet 1" of this list has emails; need to confirm what portion of the 735 that actually covers before loading it in.
- **Amazon USA Product Review 2nd SMB (654 leads) — ready.** Has emails.

**Net effect on next week's rebuild/launch order:** realistically only 2 lists (UK/USA Amazon Seller, Amazon USA Product Review 2nd SMB — 763 leads combined) are fully ready to load as-is. Amazon USA Product Review needs the Sheet 1 subset isolated first. UK & USA Amazon Brand Leads is blocked until emails exist or the channel changes.

**Confirmed (Aug 16):** these 4 draft campaigns (built Aug 14 via Claude Code) are the ones Eikko will review next week — copy, settings, and mailbox assignment, per the "rebuild" plan above, before deciding on launch.

---

## Update (Aug 19, 2026) — WhatsApp check-in + mailbox resolution

**Status:** still in mailbox warmup, no campaigns launched yet. Eikko organizing launch order, leaning toward the Google Sheet lead-list campaigns (List B) first.

**cueneyt@ and daniel@hellostarfix.com — resolved.** Both confirmed deleted from Instantly (per Cüneyt's WhatsApp instruction) and, checked live, **fully deleted from Hostinger too** — not just suspended. This freed exactly 2 mailbox seats.

**2 replacement mailboxes approved.** Cüneyt agreed to create 2 new mailboxes to replace them. **No purchase needed** — hPanel confirms "2/13 mailboxes left" on hellostarfix.com with a free "Add mailboxes" option (separate from "Buy more mailboxes"). Eikko had raised a cost/tax concern about buying new slots on his own end; Cüneyt didn't think a purchase was necessary, and the live check confirmed Cüneyt was right — use the 2 already-freed seats.

**Open items:**
- [x] Choose names for the 2 new mailboxes — **kevin@hellostarfix.com created and confirmed live** (1/13 seats left, Aug 19). **ryan@hellostarfix.com** also confirmed created/Active by Aug 20 (0/13 seats left).
- [x] ~~Finish creating ryan@hellostarfix.com~~ — confirmed Active in hPanel as of Aug 20
- [x] **Connected kevin@ and ryan@hellostarfix.com to Instantly (Aug 20)** — both added via API (daily limit 30, matching the rest of the fleet), status Active. DNS already covered domain-wide, no new records needed.
- [x] **Warmup started on both (Aug 20)** — confirmed `warmup_status: 1` on both accounts. Not yet assigned to any campaign — hold until warmup completes (~2–3 weeks) per the existing hellostarfix.com mailbox rule.

**Hostinger IMAP/SMTP server settings for hellostarfix.com** (for connecting kevin@/ryan@ in Instantly):

| Protocol | Hostname | Port | TLS/SSL |
|---|---|---|---|
| Incoming (IMAP) | imap.hostinger.com | 993 | ✅ |
| Outgoing (SMTP) | smtp.hostinger.com | 465 | ✅ |
| Incoming (POP3) — not recommended | pop.hostinger.com | 995 | ✅ |

Username = full mailbox address (kevin@hellostarfix.com / ryan@hellostarfix.com), password = whatever was set when each mailbox was created.
- [ ] Confirm with Cüneyt whether he still needs to review the campaign email copy before launch — asked in chat, no answer yet
- [ ] Finalize campaign launch order — given the email-availability mapping below, likely start with UK/USA Amazon Seller + Amazon USA Product Review 2nd SMB (both fully ready)
- [ ] Decide how to handle UK & USA Amazon Brand Leads (640 leads, no emails, LinkedIn-only) — enrich for email or run as a separate LinkedIn channel
- [ ] Isolate the email-having "Sheet 1" subset of Amazon USA Product Review before loading it into Instantly

---

## Notes
- Eikko's pitch case study for this client: prior Instantly→PlusVibe migration (bounce rate down to 0.9%, one segment reply rate 23.5%) — used as proof of judgment on infra vs. copy diagnosis.
- Client is open to the "migrate platforms" contingency since Eikko has already done this once successfully; not wedded to Instantly.
- Recording available: Fathom transcript, Aug 13 call ("Impromptu Google Meet Meeting — August 13").
