# Cüneyt (Starfix) — Client Profile

**Status:** 🟡 Trial (20 hours) | **Rate:** $7/hr | **Role:** Cold Email & Lead Gen Specialist (Deliverability + Campaign Ops)
**Coverage Period:** Aug 13, 2026 – Present | **Last Updated:** 2026-08-13

---

## Contact Details
- **Contact:** Cüneyt (hiring manager) — also Junaid mentioned on the call (provides Hostinger/Instantly access)
- **Email:** info@elevate-commerce.de
- **Company:** Elevate Commerce (brand: Starfix)
- **Business:** B2B service for Amazon sellers — pay-per-removed-review model, targeting US/UK Amazon sellers
- **Communication:** WhatsApp
- **Meetings:** Ad hoc (first call was Google Meet, booked with ~5 min notice)

---

## How This Client Was Found
Inbound cold outreach — Cüneyt messaged Eikko directly asking about cold email + lead gen fit. Eikko replied with the required "Deliverability" keyword format and a proof case study (Instantly→PlusVibe migration on a prior campaign), which led to an immediate call same day (Aug 13).

---

## Deal Terms

- **Trial:** 20 hours @ $7/hr
- **Billing:** Weekly, **50% upfront** for week one (⏳ **pending — not yet received** as of Aug 13)
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

**Active campaigns (Instantly):**
- Liste von Dennis — daily limit 30, link tracking on, open tracking off, stops on reply
- Amazon Seller 2cnd (2) — Tue–Thu 9am–5pm (Arctic/Longyearbyen tz), daily limit 30, no open tracking, stops on reply
- Sports & Fitness (sellervate, reviews) — Tue–Thu 9am–5pm (Arctic/Longyearbyen tz), daily limit 30, no tracking
- Starfix New UK Leads 2026-08 — Mon–Thu 8am–8:30pm (Isle of Man tz), daily limit 40, no tracking
- Starfix New US Leads 2026-07-29 — weekdays 8am–4pm (America/Chicago), daily limit 60, text-only, stops on auto-reply, prioritizes new leads

**Lead source note:** Current lead provider ("Limlid"/Lemlist-adjacent, per call) is slow and produces duplicates. Discussed switching to cheaper verifiers (QuickEmailVerification, MillionVerifier) and scraping tools (Apify, other scrapers) for future lead gen.

**Contingency plan (per call):** If the DKIM fix + warmup restart doesn't resolve deliverability within ~1 month, migrate off Instantly to SmartLead or PlusVibe (same playbook used successfully on the Chris Drew/Satlas account).

---

## Immediate Action Items (from Aug 13 call + audit)

- [x] Add missing DKIM record to all 3 Hostinger domains (hellostarfix.com, starfix.online, sellervate.net) — fixed Aug 13, all 5 previously-disabled mailboxes recovered
- [ ] Coordinate with Instantly support to confirm DKIM propagation / re-verify domains (recovery looks self-resolved but worth a formal confirmation)
- [x] ~~Investigate and re-enable (or replace) the 5 mailboxes disabled with 554 5.7.1~~ — resolved by DKIM fix, no manual re-enable/replacement needed
- [ ] Delete suspended mailboxes and create replacements in Hostinger where needed — likely no longer needed, confirm not required
- [ ] Verify MX/SPF/DMARC (not just DKIM) on all 3 domains
- [ ] Run full domain/mailbox health report, send to Junaid
- [ ] Launch new Instantly campaigns using existing lead list (to preserve warmup history rather than starting fresh)
- [ ] Flag sellervate.net renewal (~46 days out as of Aug 13) so it doesn't lapse mid-trial
- [ ] Confirm 50% upfront payment for week 1 (still pending)
- [x] Hostinger API key received (Aug 13) — stored in `RESOURCES/Tools & API Details/tools_api_details.md` (#11, `STARFIX_HOSTINGER_API_KEY`). Confirmed covers hellostarfix.com mailboxes (cueneyt@, daniel@, james@); sellervate.net and starfix.online scope not yet confirmed
- [x] starfix.online — separate API token created and confirmed (entry #12)
- [x] sellervate.net — API token received and stored (entry #13), all 3 domains now covered
- [ ] Decide on open tracking (currently off/broken fleet-wide across all 11 campaigns — no funnel visibility past reply rate); see full performance audit in `OUTPUT/Campaign Tracking/Cüneyt - Starfix Campaign Tracking.md`
- [ ] Pause or rework zero-engagement, low-volume campaigns: Amazon Seller 2nd, Amazon Seller 2cnd (2), Starfix New UK Leads 2026-08
- [ ] Investigate why UK Seller (starfix) converts far better than the rest (3 opportunities off 284 leads) — replicate that angle into underperforming campaigns

---

## Notes
- Eikko's pitch case study for this client: prior Instantly→PlusVibe migration (bounce rate down to 0.9%, one segment reply rate 23.5%) — used as proof of judgment on infra vs. copy diagnosis.
- Client is open to the "migrate platforms" contingency since Eikko has already done this once successfully; not wedded to Instantly.
- Recording available: Fathom transcript, Aug 13 call ("Impromptu Google Meet Meeting — August 13").
