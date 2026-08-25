# Yoni Lebovits (Albert Scott) — Client Profile

**Status:** Active | **Rate:** $5/hr | **Hours:** 5h/day (9pm–5am PHT, weekdays) | **Role:** Outreach Specialist / Sales-Marketing Ops Assistant
**Type:** Amazon marketplace growth agency (full-service Amazon account management)
**Last Updated:** 2026-08-13

This file is the reference for any Claude instance working on Albert Scott tasks — it documents the established workflow, tools, and rules as taught by Yoni and Rachel. Follow this as source of truth; if it conflicts with a live instruction from Yoni or Rachel, the live instruction wins, but flag the conflict rather than silently picking one.

---

## Contact Details
- **Email:** (TBD)
- **WhatsApp:** (TBD)
- **Company:** Albert Scott
- **Timezone:** PHT (Philippines)
- **Time tracking:** TimeDoctor (auto-tracked)
- **Break:** 1hr, 11pm–12am PHT

---

## Key People

| Name | Role | Owns |
|---|---|---|
| **Yoni Lebovits** | Principal | CRM (Pipedrive), US campaign operations, final approval on US campaigns, daily check-ins |
| **Rachel Safra** | Head of Brand Partnerships | Europe campaign messaging and approvals, trained Eikko on Smartlead |
| **Maria** | Team member | Collects US trade show leads on-site (business cards) |
| **Phoebe** | Team member (Rachel's side) | Collects Europe trade show leads on-site |
| **John** | Former team member | ~2 weeks, left due to family circumstances; left a Pipedrive/Calendly follow-through gap (~July 2–10) that needed backlog cleanup. His old campaigns (Fancy Foods, IHS) are style references only — Yoni prefers hyperlinked CTAs over his new-thread-per-email approach. |

**Approval rule (non-negotiable):** all campaigns go through Yoni (US) or Rachel (Europe) before launch. No autonomous launching — build to launch-ready and hold for review.

---

## Role & Responsibilities

- Prospect tagging in Smartlead
- CRM updates in Pipedrive
- Calendly booking routing
- Blocklist management
- Campaign monitoring

**Automation pipeline:** Calendly (booking received) → Pipedrive (lead created) → Smartlead (blocklist added).

**Ongoing:** Peru Silver Chain Wholesalers campaign (primary).

---

## Tools

| Tool | Purpose | Notes |
|---|---|---|
| **Smartlead** | Cold email — campaigns, Master Inbox, reply tagging, Global Blocklist | Primary tool, ~111 mailboxes across `albertscott*.com` domains |
| **Pipedrive** | CRM | Interested/Follow-up leads synced manually (see Pipedrive Workflow below); no confirmed native Smartlead integration |
| **QuickEmailVerification** | List verification pre-upload | Manual login (2FA) — cannot be automated, flag back to Eikko |
| **Google Drive** | Lead files, case studies, deck, campaign docs | Root folder ("Yoni Lebovits") ID: `1g3EdQnAMXERl98HJcPhf_OI8LT6oEg11` |
| **Notion** | Task tracking | "Albert Scott — Task Tracker" DB (Calendar/By Category/By Status views) |
| **TimeDoctor** | Time tracking, tied to pay | Invite sent to sales manager email |
| **Covve / ChatGPT card-extraction** | Digitizes trade show business cards | Pre-configured by Yoni, don't modify. Give show name + card images, batch ~9 photos at a time |
| **WhatsApp** | EOD updates channel | Short, chat-ready ✅ bullet format |
| **Wise** | Payment | Weekly, typically Mondays, for prior week |

**APIs connected:** [ ] Smartlead (tagging) · [ ] Pipedrive (CRM) · [ ] TimeDoctor · [ ] Calendly

---

## Reply Tagging Taxonomy (Smartlead Master Inbox)

| Reply type | Tag | Action |
|---|---|---|
| Explicit ask for call / clear interest | **Interested** | Sync to Pipedrive, block domain |
| Asks for info/pricing, no clear interest | **Follow-up** | Reply with info, sync to Pipedrive, set reminder, block domain |
| Explicit "not interested" | **Not Interested** | Block domain |
| "No"/"stop"/"unsubscribe" (list-removal, not objection) | **Do Not Contact** | Tag only, no block unless combined with Interested/Follow-up history |
| Auto-reply / OOO | **Out of Office** | Ignore content, do NOT mark unread |
| Unclear | **Unsure** | Mark unread so it resurfaces |
| Already tagged | — | Don't touch |

**Rule:** whenever a reply is opened and tagged, mark it back as unread — except Out of Office.

**Domain blocking (current rule, expands Rachel's original scope):** ANY lead marked Interested or Follow-up gets its domain blocked once handled via Pipedrive, preventing other campaigns from re-contacting the same company. Master Inbox → open lead → Block → Block entire domain → confirm. Global version: Settings → Global Blocklist (for leads with no Smartlead reply, e.g. Calendly bookings).

---

## Pipedrive Workflow

Applies to every lead tagged Interested/Follow-up, plus two "invisible" sources:
- **Calendly bookings with no reply** — identify via `notifications@calendly.com` forwarded to sales manager inbox, extract booked email from notification body.
- **Direct/forwarded leads** — Yoni CCs/BCCs an intro that didn't come through a Smartlead reply.

**Steps:**
1. Search Pipedrive for the person (email/name/company).
2. If not found: create Person (First/Last Name, Organization — create if needed, Email, Label = `Smartlead`).
3. Create an Activity: Subject = `Interested` or `Follow Up` (matching tag), Notes = summary of latest message or source note, Assigned to Yoni, due date set, save.
4. If person exists: skip creation, go straight to the Activity.
5. **Never create duplicate Activities** — if an open one exists, flag for human review instead of guessing.
6. Block the domain in Smartlead for every lead processed this way.

Separate from Rachel's Europe campaign work — applies to leads/campaigns under Yoni directly.

---

## Lead Sourcing

1. **Fresh show leads** — Maria (US) / Phoebe (Europe) via business cards → spreadsheet via card-scanning app; unreadable cards go through Covve/ChatGPT extraction in batches of ~9.
2. **Older lead lists** — ~10 years accumulated (e.g. ~3,000 emails from past Cosmoprofs), reused periodically as "old lead" campaigns, spaced out to avoid re-hitting the same people.

**Spreadsheet cleanup:** delete empty/unnecessary columns; consolidate secondary/tertiary emails into main column; delete rows with no email; drop/merge inconsistent fields (e.g. middle name). Naming convention: `[Show Name] [Year] cards` (Google Sheet).

**Verification (QuickEmailVerification):** export CSV → upload → validate → filter out invalid emails → delete status columns → download final CSV. Requires human login (2FA) — flag back to Eikko, don't attempt directly.

**Lead status column** (older lists, e.g. T Expo sheet): may carry `New`, `Invalid Email`, `Not Interested`, `Unqualified`, `Working Smartlead`, `Interested`. When building a new campaign from such a list, **only use `New` status leads**.

---

## Campaign Types & Structure

**Two types:** Post-show (can reference recent in-person contact) vs. Old-lead (cannot reference recent attendance).

**No-attendance framing (critical):** for shows nobody from Albert Scott attended, copy must not imply any contact/presence — no "nice seeing your team there." Safe framing: "came up on our radar through [Show]" / "I came across your brand through [Show]." Don't name a colleague unless they actually attended.

**Approved structure — 4 emails (default):**
1. Initial Outreach — intro, positioning, one proof point, low-friction CTA, no calendar link, ~100–150 words.
2. Follow-up 1 — "wanted to follow up" opener, ONE case study (situation → work → result), calendar link.
3. Follow-up 2 — "different note this time" opener, category insight + strategic observation combined, calendar link.
4. Close the Loop — short, no calendar link, no new case study, ends politely.

*(Note: an earlier 5-email version was corrected back to this 4-email structure per explicit instruction — don't use the 5-email version.)*

**Alternate style test (experimental, T Expo only):** 3-email cadence (Day 1/4/8), 50–80 words, plain text, minimal lowercase subject lines, first email link-free ("reputation builder"), links only in emails 2–3 (1–3 max, varied destinations). One-off test for Yoni's review, not yet adopted as standard.

### Case Study Rules
- **Preferred three, in priority order:** Atlas Olive Oils, MouthWatchers, BeYoutiful.
- **Secondary (better category fit):** Roll & Comb (hardware/garden/outdoor), FlipBelt (sports/fitness), Objet D'Art (home/gift, wholesale-to-DTC), Nora (grocery/snacks, international food), Great Western (grocery manufacturer B2B-to-DTC), Human Beanz (vitamins/supplements).
- **Never mix facts between case studies** — keep numbers attached to the correct brand, preserve qualifiers exactly ("on track to," "approximately," "annual run rate" vs. completed revenue).
- **MouthWatchers is oral-care** (toothbrushes/toothpaste) — never a watch/fashion brand.

### Format Rules
- **Spintax:** `{option1|option2|option3}` — exactly 3 variations, phrase/sentence level (not word level), all natural and equivalent in meaning.
- **Merge fields:** `{{first_name}}` standard. `{{company_name}}` — do not use unless explicitly confirmed available; has produced broken/awkward output (legal suffixes rendering oddly).
- **Style:** no em dashes; plain, direct, human tone, not corporate. Include opt-out line: `If this isn't relevant, just reply "no" and I'll stop reaching out.` Signature: `Yoni\n📧 yoni@albertscott.com | 📞 347-388-9725 | 🌐 albertscott.com`

---

## Known Integration Gaps

- **No confirmed native Smartlead → Pipedrive integration** on the core app — Settings → Integrations only lists Hubspot, Clay, Leadmagic, Outboundsync, Listkit. A Pipedrive "Connect" option exists under SmartAgent (separate, API-key based) but likely doesn't support the category-filtered sync + Activity creation this workflow needs.
- **Realistic automation path:** webhook + Zapier/Make, or direct API calls if Smartlead/Pipedrive are available as connected MCP tools (prefer calling directly over custom scripts with stored keys).
- **Blacklist/spam-flag notifications** not yet configured — no alerting if a sending domain gets flagged by a third-party monitor.

---

## Work Hours & Admin

- 5 hours/day, starting 9:00 PM PHT (schedule note: some docs list 9:00 AM start — confirm with Yoni which is current).
- TimeDoctor tracks hours for pay.
- Payment: weekly via Wise, typically Mondays for prior week.
- Daily check-in call with Yoni.
- Inbox doesn't need continuous monitoring — check morning/midday/end of day; rest of time goes to active work.
- If out of clear tasks, say so directly rather than waiting.

---

## Company Positioning (from approved deck — don't invent beyond this)

Albert Scott is a full-service Amazon partner/agency helping established European and global brands launch, manage, and grow their Amazon US business — supporting first-time entrants and existing sellers wanting stronger growth, structure, control. Spans Seller Central and Vendor Central: listings/content, advertising, retail strategy, operations/logistics, ongoing account management. Don't list every capability in one email — select only what supports the specific message.

---

## Standing Preference

**Always ask a clarifying question before executing a task** — applies to every task, not just sensitive ones. Don't assume; confirm scope, especially when Yoni's and Rachel's instructions could conflict (surface the conflict, don't silently pick a side).

---

## References

- `OUTPUT/Campaign Tracking/Yoni-Projects-Active.md`
- `OUTPUT/Campaign Tracking/Q4-Toy-Campaign-Call-Notes-Yoni.md`
- `OUTPUT/Campaign Tracking/Toy Fair - 9 Email Variants - Yoni Review.md`
- `OUTPUT/Campaign Tracking/Fancy Foods - 9 Email Variants - Yoni Review.md`
- `PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md`
