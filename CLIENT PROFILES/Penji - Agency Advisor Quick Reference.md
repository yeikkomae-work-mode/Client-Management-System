# Penji — Agency Advisor Quick Reference

One-page reference for the role. Full detail lives in the "Agency Advisor Eikko" Notion (Job Training modules), `Penji - Profile.md`, and `Penji - Sales Ecosystem & Team Standards.md`. Task/meeting history is tracked live in Eikko's personal Notion (Task Tracker + Meeting Tracker databases, VA Command Center workspace).

---

## The Role

**Title:** **LinkedIn Outreach Specialist** (offer-letter title) / Agency Advisor — Outbound Outreach Specialist, Agency Listing track (Notion training title). Which one is operative for reporting is an open question for Shekinah.
**Pay:** **$350/month base salary — full-time employment**, not a retainer *(corrected 2026-08-24 from the signed offer letter + employment contract; the earlier "retainer" wording came from the Notion Clients database and understated the commitment)*
**Schedule:** 8am–5pm, 1hr break 12–1pm. 90-day probation ends ~2026-11-09; PTO accrues after that.
**Full terms:** see Work Arrangement in `Penji - Profile.md`

**Objective:** Build and maintain the most complete database of digital marketing agencies globally, enrich every record with verified contact data, and run **LinkedIn** outreach until every qualifying agency has been contacted, replied, or exhausted. Agencies are Penji's highest-LTV segment.

> **Confirmed 2026-08-17:** Company-wide policy is "ALL outbound must ONLY focus on LinkedIn outreach" — email automation belongs solely to Jayvy ("JV"). Treat LinkedIn as the sole outbound channel for this role unless Shekinah says otherwise.

**Monthly KPIs:**
- 25+ meetings scheduled
- 10% response success rate
- 5+ total accounts closed

**Reporting week runs Friday → Thursday** (Friday = day 1, Thursday = day 7) — confirmed via personal task tracker, not the calendar week.

---

## Daily Workflow

1. **Grow the database** — pull new agencies from Clutch, Agency Spotter, UpCity, Design Rush, GoodFirms, G2, Sortlist, The Manifest, Bark.com + LinkedIn/Google Maps/social searches. Never stops — database grows every week.
2. **ICP filter** — 5–200 employees, active client roster, offers social/paid/content/SEO/branding/web dev, no existing Penji subscription. Disqualify: pure design agencies, freelance collectives, competitor-locked accounts. LinkedIn outreach specifically is scoped to **Agency** and **Mid-Market Signal Trigger** segments.
3. **Identify the decision-maker** — **Corrected 2026-08-17 by Shekinah (Slack):** exclude Founders and Co-Founders entirely, and exclude anyone not related to marketing. Target marketing/creative titles specifically — Creative Director (and variants: Executive/Associate/Senior/Design Director), Marketing Director, Head of Marketing, CMO, Director of Brand/Growth/Ecommerce/Digital Marketing, etc. This supersedes the old "founder/owner → MD → creative director" hierarchy for Gojiberry-sourced marketing lists. Never an info@ address.
4. **Enrich via Gojiberry/GoJaberry** (Hunter.io → Findymail as backups) before anything enters outreach. No prospect enters a sequence without verified contact data — hard rule.
5. **Post to Slack for verification** — 👍 = load into outreach within 24hrs. 👎 = add reason comment, drop.
6. **Launch outreach via Dripify (LinkedIn)** — see the RPS script section below for what's actually confirmed running. No new outreach starts before all follow-ups are caught up.
7. **One tool at a time per account (confirmed 2026-08-17, Alan):** never run Gojiberry scraping and Dripify/HeyReach outreach simultaneously on the same account — pick one active tool at a time to reduce restriction risk.
8. **Watch for trigger signals** — job postings for designers, negative competitor reviews, funding news, new campaign launches. Any of these jump an agency to the front of the queue.
9. **Route warm replies to Joan within the hour.** No exceptions. Oliver closes. Also post positive responses in the `#response` Slack channel.
10. **Log everything in real time** — CRM/tracking sheet (the "Agency Master List" in Google Sheets), status, next action, conversation history in the prospect's exact words. Not logged = didn't happen. Note: transferring who's been messaged in Dripify into the Sheet is still a **manual** step as of Aug 18 — see Open Items for the automation task in progress.
10a. **Response routing (confirmed 2026-08-25 by Kristine, Slack — no prior SOP existed for this):** after forwarding a response in Slack, it also has to be logged in the shared **"LinkedIn responses"** sheet (`docs.google.com/spreadsheets/d/1euKlI0MZLw1ptXLXXggzQ9QmEo_FlXil34R9aMMBaOM` — checked weekly by John). Two tabs, easy to get backwards (Eikko had it flipped until corrected):
    - **Agency Response** tab → cold leads, declines, unsubscribes, anything not warm
    - **Agency LEAD** tab → hot/warm leads only
    Reporting on this sheet happens **every Thursday**.
11. **15-day rule:** any prospect untouched for 15 days rolls into automated re-engagement — not manual follow-up.
12. **Morning discipline:** work warm leads before cold contacts, every morning, without exception.

**Weekly report (Friday→Thursday cycle):** new agencies added by source, total passing ICP filter, total enriched, total entered into Dripify, LinkedIn acceptance rate, positive replies, meetings booked, best-performing source, running database total.

---

## LinkedIn Outreach

- LinkedIn is Penji's primary lead source — books more meetings than email despite email running 100k/month. Team: 6 people on LinkedIn outreach, 2 on email (Jayvy solo on email automation).
- Start on **personal LinkedIn** (~490 connections) via Dripify — goal **25 messages/day**. Alan Walker manages Dripify seat access and sent the team invite.
- Live LinkedIn stack: **Dripify, GoJaberry (Gojiberry), HeyReach** (corrected 2026-08-18 — earlier notes had this as "HeyRidge," a Fathom auto-transcript mishearing of "HeyReach"/"Heerich"). Evaluating LinkedIn Helper against Dripify (Eikko has prior hands-on experience with it from a past role — Sales Navigator filters + campaigns + auto-withdraw after 30 days).
- Messaging style for LinkedIn: casual, attention-grabbing hook (e.g. "rock paper scissors"), **3 sentences max** per message.
- 50 US-based LinkedIn accounts in progress for scaling (39/50 built as of Aug 17), via proxies not VPNs, by Sept 1. Eikko will add a new US-based account to this pool — **confirmed 2026-08-18: Eikko himself chose the name "Benji" for this persona** (his own words in the Aug 17 onboarding call — not an externally-assigned name, earlier "unconfirmed" flag is resolved). Build it using the AdsPower process below.
- Lead verification currently **Clearout**; Eikko recommended **Million Verifier** over Quick Email Verification based on past-client experience — sent to Alan to forward to Jayvy.
- Scraping tool in active use: **Apify** (confirmed Aug 17, Eikko has prior experience with it too).
- Team-wide LinkedIn scale target: ~5,000 → 10,000+ messages/month, expected 50+ meetings/month (team total, not an individual target).
- **Other team members on outreach:** Alan Walker (own "Alan Walker" persona, handles a larger enterprise-tier account, also owns Dripify seat/access management), Cristy (LinkedIn profile added to HeyReach Aug 17 — role uses 2+ LinkedIn profiles), Ninette (newer team member, also raised LinkedIn Helper as an option), Lyn & Iko / Kristine (named in the Aug 18 AdsPower training — building the account pool).

### Official "Rock Paper Scissors" script (from Shekinah / loaded into the Gojiberry campaign, Aug 17)

Confirmed **live and running** — this is the exact 7-touch sequence loaded into the "Setup Gojiberry Campaign" task (marked Done, Aug 17), scoped to **marketing-related contacts only**:

1. **Connection note:** Hey NAME, If I beat you at Rock Paper Scissors, would you give Penji 10 minutes?
2. **~1hr after accepted:** Hey NAME, Still waiting on your move, Rock, Paper or Scissors? What's your move?
3. Okay I'll go first, I'm throwing Paper. Out of curiosity, are you currently satisfied with your creative setup, or is there room to improve for COMPANY?
4. If I could guarantee all your design and video projects are delivered in under 24 hours, would you be open to a quick chat?
5. Lately, I've been talking to a lot of professionals, and one common challenge they mention is struggling with design consistency, managing revisions and late submission. Is that something you've dealt with as well?
6. Do you feel like you're overpaying for mediocre design? Any interest in meeting me to chat about Penji?
7. Curious if you have any design projects that could use an extra push?

⚠️ **Still worth a direct confirmation with Shekinah:** the written Sales Team Standards doc caps LinkedIn outreach at **2 touches per prospect**, but the completed Gojiberry campaign setup task explicitly loaded all 7 RPS beats. As of Aug 18 the 7-touch version is what's actually configured and running for the Gojiberry-sourced list, so treat that as the operative sequence for now — but it's not yet reconciled against the documented 2-touch cap. Doesn't block continuing to run it; just flag it if Shekinah reviews touch counts.

### AdsPower — new LinkedIn account creation process (confirmed 2026-08-18, team training)

This is the current SOP for building "Benji" and any other new US-based persona accounts:

1. **Setup:** create a new AdsPower profile → copy a proxy from the Sales and PR sheet's Proxy tab → paste the proxy into AdsPower → set WebRTC to "Replace."
2. **Warm-up:** browse US-based sites (CNN, ESPN, Amazon, etc.) for several minutes; play a YouTube video in the background. This is to build a human-like browsing pattern before touching LinkedIn.
3. **Sign-in:** sign into Gmail using the assigned "Try Penji" email → on LinkedIn, use **"Sign in with Google"** specifically — this bypasses the phone-number verification step that's the most common failure point.
4. **Profile setup:** after sign-in, the LinkedIn location prompt appears — skip all other setup steps (connections, etc.). Update profile photo, banner, and verify the work email.
5. **Initial activity:** send only **5 connection requests** on a brand-new account. Target 2–3 acceptances per week before scaling further.
6. **If it fails** (persistent captchas or phone-number prompts): mark the account for deletion in the Sales and PR sheet immediately, tag the associated proxy as "not working," and start over with a new proxy + email. Don't reuse a flagged proxy.
7. **Sheet management:** move restricted accounts to the "For Deletion" tab, successful ones to "Active Accounts." Persona names (5 male, 5 female) go in a dedicated tab for Shekinah to create the matching "Try Penji" emails.
8. Accounts start on the free 2-profile AdsPower plan; scale to the paid 10-profile plan once the process is proven — this requires providing AdsPower login credentials for setup.

**Persona accounts owned by Eikko** (registry: "Sales & PR Team Linkedin Accounts" sheet — credentials in `Penji - Profile.md`):

| Persona | Account | Status |
|---|---|---|
| Amanda Scott | `amanda@trypenji.co` | Active — Female tab row 11; password reset + internal warm-up email sent Aug 19 |
| "Benji" | (to be built) | Planned — build via the SOP above |
| Tina Lombardo | tina.lombardo098@gmail.com | Blocked since Aug 13 (login issue) |

---

## Non-Negotiables

- Never enter outreach without a verified decision-maker contact
- Never send a generic opening — every first touch references the agency by name and a specific angle
- Never skip Gojiberry/GoJaberry enrichment
- Never let more than 24 hours pass between enrichment and outreach trigger
- Never contact a pure design agency, existing Penji customer, or competitor employee
- Never let a warm reply sit longer than 1 hour before routing to Joan
- Never leave a 👎 without a reason comment
- Never exceed the confirmed touch sequence per prospect (currently the 7-beat RPS script for Gojiberry leads — see flag above)
- Never start new outreach before follow-ups are caught up
- Never do manual outreach outside an approved tool
- Never let a prospect sit past 15 days without rolling them into automated re-engagement
- Never work cold contacts before warm leads in the morning
- **(Aug 18)** Never run Gojiberry scraping and Dripify/HeyReach sending on the same account at the same time
- **(Aug 18)** Never push a new AdsPower account past 5 initial connection requests before it's proven safe

---

## Tools

| Tool | Use |
|---|---|
| Gojiberry / GoJaberry | Lead scraping & enrichment |
| Apify | Scraping (confirmed active, Aug 17) |
| Dripify | LinkedIn automation — seat provided by Alan Walker |
| HeyReach | LinkedIn outreach (corrected name, Aug 18 — was "HeyRidge") |
| AdsPower | Proxy-based browser profiles for new LinkedIn account creation |
| LinkedIn Helper | Not yet adopted — evaluating against Dripify |
| Clearout | Lead verification (current) — Million Verifier recommended as cheaper alternative |
| Google Sheets | Master agency database & tracking ("Agency Master List"); response logging ("LinkedIn responses" — Agency Response / Agency LEAD tabs, see Daily Workflow #10a) |
| Slack | Verification + warm reply routing (`#response` channel) |
| Lemlist / Email Bison / Instantly / Linless | Jayvy's email-automation scope, **not part of this role** |

---

## Open Items

- [ ] Complete "Advisor Job Training Test" (10-question scenario quiz — submit via Google Sheet, own words, no AI)
- [ ] Confirm with Shekinah how the 7-touch RPS script reconciles with the documented 2-touch cap (not blocking — sequence is live either way)
- [x] Pay confirmed — $350/month base salary, full-time (Aug 24, offer letter). Note: "retainer" framing corrected.
- [x] Hours and start date confirmed — 8am–5pm (1hr break), started Mon Aug 11, 2026 (Aug 24, offer letter + contract)
- [ ] Confirm which title is operative for reporting: LinkedIn Outreach Specialist vs. Agency Advisor
- [ ] Ask whether the contract's "wage plus commission" structure carries a commission component for this role — the offer letter names none
- [ ] Confirm whether the 8am–5pm shift is PHT or ET (the interview form recorded a night-shift preference)
- [x] Connect personal LinkedIn to Dripify — Done Aug 17
- [x] Add Cristy's LinkedIn to HeyReach — Done Aug 17
- [x] Setup Gojiberry Campaign (RPS sequence, marketing-only filter) — Done Aug 17
- [x] Meeting with Shekinah — process/tooling clarification — Done Aug 17
- [ ] 🔴 **Dripify paid seat still not active as of 2026-08-25** (trial expired Aug 24). Card/billing not set up on the account per Eikko — Hayden was to tell Shekinah. Doing outreach manually on personal LinkedIn in the meantime.
- [ ] Send Hudson Miller & Shane Williams the meeting link promised in the Aug 19 "Yearly Team Outing" email from the Amanda Scott account — never sent
- [ ] **Connect Dripify + Zapier + Claude** (due 2026-08-18) — automate lead-activity updates from Dripify into the Google Sheet; matches Stage 5/7 of the automation workflow doc
- [ ] Setup AdsPower (proxy tool) — in progress
- [ ] Build the "Benji" persona LinkedIn account using the AdsPower SOP above
- [ ] Evaluate LinkedIn Helper against Dripify
- [ ] Daily 8AM meeting with Penji team — recurring, ongoing
- [x] Response-routing SOP clarified (Agency Response vs Agency LEAD tabs) — Aug 25, Kristine

---

**Last updated:** 2026-08-25
