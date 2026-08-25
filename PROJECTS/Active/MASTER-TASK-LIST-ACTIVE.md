# Master Task List - Albert Scott Operations
**Last Updated:** August 18, 2026 (GitHub repo audit cross-referenced against tracker — campaign analytics reporting agent confirmed DONE; lead-list/export tooling built out extensively, likely resolves the "paused" master-list item; domain-block standing rule updated for OOO/Wrong Person; Apify integration barely started; LinkedIn targeting flow and blacklist verification both still fully open) | **Owner:** Yoni & Aiko

---

## ACTIVE PROJECTS

### 0. URGENT: SMARTLEAD DELIVERABILITY CRISIS (Aug 10 meeting)
**Status:** In progress — immediate fixes applied, follow-ups outstanding
**Priority:** Critical — affects every active campaign

#### Full Diagnostic (per SmartLead support chat, supersedes meeting-summary numbers):
- **Bounce rate: 7.27%** (7-day: 317 of 3,827 sends bounced = 8.28%), up 5.16pp — more than 3x the 2% safe threshold
- **20 of 71 mailboxes (28% of fleet) in WARMUP_BLOCKED status** — stuck, not sending warmup, reputation can't recover while blocked
- **Tracking was OFF on all 50+ campaigns** (`DONT_EMAIL_OPEN`, `DONT_LINK_CLICK`) — root cause of the "0 opens on 28,840 sends" signal; not a spam/deliverability problem, just invisible data
- 11 of 13 active campaigns plain-text only (85%) — SmartLead recommends mixing in 30-40% HTML
- Daily sends had collapsed to 12/day vs. 1,285/day fleet capacity (0.9% utilization) — likely warmup blocks + bounce auto-throttling
- Totals: 28,840 emails sent, 284 replies (0.98% reply rate), 111 connected mailboxes / 0 disconnected, 100% inbox placement (no spam/throttling detected on delivered mail)
- Root cause chain: tracking disabled → bounces went unseen → bounces accumulated → ISPs throttled/paused warmup → 20 mailboxes stuck blocked → send volume collapsed → reputation never recovers

#### Fixes Applied:
- [x] Tracking enabled on all 13 active campaigns (confirmed via SmartLead support chat, Aug 10)
- [x] Daily send limits cut to 20/mailbox/day (from 12+); goal to return to 30 once reputation recovers
- [x] Time Doctor screencast settings fixed (Aug 11 — confirmed by Eikko)

#### Outstanding — SmartLead support's recommended next steps, awaiting Eikko's go-ahead:
- [ ] Reduce daily send limits further to 10-12/mailbox/day (SmartLead's recommendation, tighter than the 20/day already applied) until bounce rate is under 4%, target <2%
- [ ] Reconnect/unblock the 20 warmup-blocked mailboxes (OAuth reconnect or clear bounce threshold)
- [ ] Audit last 7 days of bounces by type (hard vs. soft) to find bad list/domain sources
- [ ] Mix in 30-40% HTML emails across the 11 plain-text campaigns
- [ ] Confirm "stop on reply" is enabled so engaged leads don't get unnecessary follow-ups
- [ ] Research plain-text vs. HTML mode fully; confirm SmartLead's 28-day reputation window; share findings with Yoni

---

### 1. SMARTLEAD MONITORING & INBOX MANAGEMENT (ONGOING)
**Status:** In progress  
**Documentation:** RESOURCES/Workflows/Smartlead-Pipedrive-Automation-Workflow.md (see "Appendix: Manual/Browser Fallback")

#### Tasks:
- [ ] Hourly monitoring setup during work hours (login to logout)
  - [ ] Monitor Smartlead Master Inbox for new uncategorized non-Rachel messages
  - [ ] Monitor salesmanager@albertscott.com Gmail for Calendly bookings
  - [ ] Extract + tag new Smartlead messages (Interested/Follow Up → Pipedrive + Block)
  - [ ] Extract Calendly contact info → Add to Pipedrive + Block in Smartlead
- [ ] Clarify hourly check implementation:
  - [ ] Manual checks vs. scheduled alerts vs. automation helper script?
  - [ ] Set up tracking checklist or log system

**Reference:** Workflow document covers all procedures

---

### 2. T EXPO CAMPAIGN — ✅ DONE (confirmed by Eikko, Aug 11)
**Status:** Complete — copy polish, settings review, and launch confirmed done
**Timeline:** Launched

#### Refinements (all confirmed complete):
- [x] **Email Copy Polish (ALL 3 EMAILS)** — grammar/tone pass done across all 9 spintax variations
- [x] **Subject Line Fixes** — capitalization strategy applied across all 3 emails
- [x] **First Name Field** — {{first_name}} merge field verified
- [x] **Messaging Improvements** — Atlas Olive Oils example, CTA phrasing, Amazon/Amazon US wording finalized
- [x] **Email Account Validation** — 12 accounts checked (warmup/day cap settings)
- [x] **Campaign Settings Review** — sequence timing, volume cap, 72 leads, subsequence confirmed
- [x] **Launch** — campaign live

**Campaign Details:**
- Subject: T Expo Reconnect campaign
- Leads: 72 imported
- Email accounts: 12
- Sequence: 3 emails, spintax variations
- Target: Reconnection + Q4 mention

---

### 3. MASTER LEAD LIST ORGANIZATION (BACKLOG)
**Status:** Data exported (240K lines, 200+ campaigns)  
**Priority:** Medium-high  
**Complexity:** Moderate

#### Problem:
- 240,000 lines of data but only 117,000 unique contacts (duplicates across campaigns)
- 200 campaign names, but only 148 distinct (naming duplicates)
- Data needs sorting into individual trade-show focused lists

#### Tasks:
- [ ] **Deduplication & Organization**
  - [ ] Pull master export into working sheet
  - [ ] Remove duplicate contacts (cross-reference by email)
  - [ ] Group by trade show source:
    - [ ] Apex (all Apex campaign variations)
    - [ ] Cosmoprof (5+ campaign variations)
    - [ ] [Other trade shows - TBD from data]
  - [ ] Create individual campaign lists for each trade show
  - [ ] Validate final counts match expectations

- [ ] **Cross-Reference with Google Drive**
  - [ ] Access "2025 Lead Blast Lists" folder
  - [ ] Identify which lead files haven't been integrated into master list
  - [ ] Pull missing leads and add to respective trade-show lists
  - [ ] Final dedup pass across all sources

- [ ] **Deliverable**
  - [ ] Create folder structure: /Trade-Shows/[Name]/Leads.csv
  - [ ] Generate summary report: total unique leads per trade show
  - [ ] Mark completion in task tracking

**Note:** This creates single source of truth for all contact data

---

### 4. TOY FAIR Q4 CAMPAIGN (PLANNING → EXECUTION)
**Status:** ✅ LAUNCHED (Aug 11) — campaign 3771090 is ACTIVE in Smartlead with leads loaded and sending Mon-Fri 9am-6pm ET
**Launch Target:** ~~Immediate~~ Done
**Priority:** Complete — monitor performance going forward

#### Aug 10 Meeting Revisions — DONE:
- [x] Replace Mouth Watchers case study with BeYoutiful (correct spelling, no invented/borrowed numbers) — done Aug 11, then superseded by Yoni's own final revision
- [x] Vary "toy and game brands" phrasing — fixed Aug 11
- [x] 9 spintax variations doc compiled and sent to Yoni for review
- [x] **Yoni reviewed and sent back his own final revised copy** ([Google Doc](https://docs.google.com/document/d/10JFZBeSfV6CBJ0o0CMjvIVGlA-AvrhyB6bi3IFpN5UI/edit)) — pulled, converted to spintax, and saved live to Smartlead campaign 3771090 (all 3 sequences updated Aug 11)

#### Launch — DONE (Aug 11):
- [x] Leads loaded into campaign 3771090
- [x] Campaign flipped to ACTIVE and sending
- [x] Sending schedule live: Mon-Fri, 9am-6pm ET

#### Next: post-launch monitoring
- [ ] Track opens/replies/bounces on this campaign now that tracking is confirmed on
- [ ] Watch for early bounce-rate signal given the fleet-wide deliverability issue (Section 0)

#### Lead Consolidation:
- [ ] **Source 1: Smartlead**
  - [ ] Access Master Campaigns Spreadsheet
  - [ ] Filter for campaigns with "toy" keyword (found: "Toy Fair Cards 2026")
  - [ ] Extract all leads from toy-related campaigns
  - [ ] Export to CSV with email, first name, last name, company

- [ ] **Source 2: Google Drive**
  - [ ] Access Toy Fair Google Sheet (1,520 contacts)
  - [ ] Verify fields: First Name, Last Name, Company, Title, Email, Website
  - [ ] Export complete list to CSV

- [ ] **Consolidation & Dedup**
  - [ ] Merge both sources (Smartlead + Toy Fair sheet)
  - [ ] Remove duplicate emails
  - [ ] Final count & validation
  - [ ] Create master "Toy Fair Q4 Campaign - Master List.csv"

#### Campaign Build:
- [ ] **Create Smartlead Campaign**
  - [ ] Campaign name: "Q4 2026 - Toy Brands Outreach"
  - [ ] Upload consolidated lead list (remove duplicates first)
  - [ ] Allocate email accounts (similar to T Expo: 10-12 accounts)

- [ ] **Build 5-Email Sequence**
  - [ ] **Email 1 (Initial):** Q4 timing awareness + reconnect
  - [ ] **Email 2 (Follow-up 1):** Toy industry specific insight (peak season challenges)
  - [ ] **Email 3 (Follow-up 2):** Case study (strong Amazon toy brand example)
  - [ ] **Email 4 (Follow-up 3):** Strategic observation (timing for prep)
  - [ ] **Email 5 (Close loop):** Respectful exit

- [ ] **Messaging Framework**
  - Core positioning: Albert Scott helps toy brands prepare for Q4 and capture peak season
  - Angle: Timing-based (Q4 prep window is now)
  - Tone: Commercial, confident, low-pressure (per ECO guidelines)
  - CTA: Conversation about readiness + opportunity

- [ ] **Polish & Validation**
  - [ ] Run all 5 emails through Claude for grammar/tone
  - [ ] Subject lines: Consistent capitalization strategy
  - [ ] First names: Add {{first_name}} merge field
  - [ ] Case study: Use relevant toy/games category success story
  - [ ] Spintax: 3 variations per email where applicable

- [ ] **Campaign Settings**
  - [ ] Email accounts: Verify warmup & daily volume caps
  - [ ] Send schedule: 20-30 emails/day
  - [ ] Timing: 2-3 days between emails
  - [ ] Stop condition: Reply stops lead from sequence

- [ ] **Launch**
  - [ ] Final review of all emails
  - [ ] Validate lead list imported correctly
  - [ ] Confirm account settings
  - [ ] Launch campaign

**Campaign Resources:**
- Master Campaigns Sheet: https://docs.google.com/spreadsheets/d/1WjxXVym9Ie4YFk5ePIc9OahqyVE-ENpDjzpBFrROuEQ/
- Toy Fair Leads: https://docs.google.com/spreadsheets/d/1b-OoKMmbGiBw4pHswrjDz4kN3-LLno34nDa5oLTduDk/
- Google Drive Folder: 2025 Lead Blast Lists (ID: 148YV2D4AUArgYFEJUZXnzDSaLgpOk_P9)

---

### 5. EMAIL ACCOUNT AUDIT & OPTIMIZATION (BACKLOG)
**Status:** Pending  
**Scope:** All sending email accounts  

#### Tasks:
- [ ] **Check all email accounts used in campaigns**
  - [ ] For each account: Verify warmup emails/day setting
  - [ ] For each account: Verify messages per day cap
  - [ ] Document current settings vs. optimal settings
  - [ ] Update any accounts with sub-optimal settings

- [ ] **Settings Review:**
  - [ ] Warmup emails/day: Should be 15 (safe baseline)
  - [ ] Messages per day: Should be 20-30 (currently many at 15)
  - [ ] Plan adjustment: Gradual increase vs. immediate increase

- [ ] **Deliverable**
  - [ ] Email Account Audit Report with recommended changes

---

### 6. CLAUDE-ASSISTED PROCESS IMPROVEMENTS (ONGOING)
**Status:** In development  
**Notes:** Learning system, error-tracking for future improvement

#### Known Issues:
- [ ] Campaign data pull missed "Sweets and Snacks" campaign (June 1)
  - **Root cause:** Possibly Haiku model limitation or instruction gap
  - **Fix:** Add explicit instruction to cross-reference by date ranges
  - **Future:** Use Sonnet/Opus for complex multi-campaign pulls

- [ ] Master list discrepancy (240K lines vs. 117K unique contacts)
  - **Resolution:** Likely duplicate contacts across multiple campaigns
  - **Action:** Validate during deduplication task
  - **Status:** Paused week of Aug 8 per Eikko, resume next week

---

### 7. CLAUDE SHARED PROJECT ACCESS (Aug 10 meeting)
**Status:** Blocked → researching fix
**Priority:** Medium-high (unblocks SEO project + future joint work)

#### Problem:
- Yoni cannot access the SEO Claude project because its files are stored locally on Eikko's machine

#### Tasks:
- [ ] Research how to create a shared Claude project both Eikko and Yoni can access
- [ ] Propose setup to Yoni (standard workflow: create a "Project" e.g. "Yoni SmartLead," then "Artifacts" within it for specific tasks like weekly reports or campaign launches)
- [ ] Collaborate with Yoni on migrating/rebuilding the SEO project under shared access
- [ ] Define a repeatable process for shared development on future Claude projects

---

### 8. NEW AI AUTOMATION PROJECTS (Aug 11 meeting — scoping stage)
**Status:** Defined, not yet started
**Priority:** Strategic — next wave of automation after deliverability crisis is resolved

#### 8a. Transfer Existing Automation
- [ ] Transfer the existing SmartLead↔Pipedrive Claude automation system to Yoni's own Claude account

#### 8b. Daily Workflow Hub
**Problem:** Yoni's daily follow-up process is manual and multi-app: check Pipedrive for overdue activities → copy lead email → paste into SmartLead to find history → draft reply (often via ChatGPT for grammar) → send email → update Pipedrive.
- [ ] Build single Claude interface to: pull Yoni's outstanding Pipedrive tasks, synthesize full SmartLead + Gmail conversation history, draft/send replies via Claude prompts, update Pipedrive lead status directly

#### 8c. SmartScout Prospecting Pipeline
**Problem:** Current lead source (trade-show business cards) is "spray and pray" — many irrelevant leads. Ideal customer is brands already selling on Amazon. SmartScout has 585,000 Amazon brands with revenue data, but raw data is missing website domains, parent company info, and contact emails; automated tools like Apollo mismatch brand names to wrong domains (e.g. "Shark" → sharkinvestors.com).
- [ ] Phase 1: Data cleaning & enrichment — Claude researches each brand for correct website domain + parent company name/domain (e.g. "Crunch" → "Ferrero")
- [ ] Phase 2: Contact acquisition (TBD) — use Apollo/LinkedIn to find contacts for the enriched list
- [ ] Phase 3: Hyper-personalized outreach — Claude drafts emails using SmartScout data (est. monthly revenue, number of sellers) for relevance

#### 8d. Lead Re-engagement System
- [ ] Build Claude-driven system to track and re-engage past leads who expressed interest, so no opportunities are lost

#### 8e. Meta & LinkedIn Ads
- [ ] Meta Ads Director: Claude manages strategy, budgeting, execution, reporting, ROI optimization
- [ ] LinkedIn Ads Strategist: Claude develops and launches LinkedIn ad campaigns
- [ ] LinkedIn Outreach Agent: content creation (Amazon-related posts for Yoni's approval) + connection request management
- [ ] Research and experiment with Claude for LinkedIn outreach

---

### 9. SMARTLEAD CLAUDE CONNECTOR — BROKEN (Aug 11 meeting w/ Shimi)
**Status:** Blocked — awaiting Shimi's manual fix
**Priority:** Critical — blocks all automated campaign launches on Yoni's own Claude account

#### Problem:
- SmartLead custom connector fails on Yoni's Claude account
- Root cause: "Add Custom Connector" is admin-only on the team plan — Yoni/Eikko can't self-serve, Shimi has to add it manually with a new API key
- Pipedrive connector was successfully connected during the meeting (not affected)

#### Tasks:
- [ ] Eikko: send new SmartLead API key to Shimi
- [ ] Shimi: use the new API key to fix the connector on Yoni's account
- [ ] Eikko: send screenshot of the Pipedrive connector request to Yoni → Yoni forwards to Shimi
- [ ] Yoni: notify Eikko once the connector is confirmed fixed
- [x] Eikko: set up the SmartLead↔Pipedrive automation on Yoni's own Claude account, using `Smartlead-Pipedrive-Automation-Workflow.md` — done Aug 11
- [x] Eikko: executed live setup via Claude Code on the web (SmartLead custom client + Pipedrive MCP connector) — confirmed working Aug 12, documented in `Yoni - Live Automation Setup Runbook.md`
- [x] Verified directly against the live repo (`salesmanager-crypto/smartlead-api-client`) — automation transfer confirmed real and running (scheduled sync prompt with checkpoint file, category IDs, CSV logging, weekly backlog scan), not just documented
- [ ] **⚠️ CONFIRM: was the SmartLead API key that got pasted into chat during setup actually rotated?** Repo inspection CANNOT answer this (no GitHub Advanced Security/secret scanning enabled) — must check the SmartLead dashboard directly. Top open item.
- [ ] Wire a permanent `ProxyAgent` into `client.js` so `NODE_USE_ENV_PROXY=1` isn't a manual flag going forward — confirmed still not done as of Aug 12
- [ ] Fix `leads:block` hardcoded `client_id: null` in `src/cli.js` — confirmed still present as of Aug 12
- [ ] Test the automation on Yoni's account end-to-end

---

### 10. FOUR NEW LEAD CAMPAIGNS (Aug 11 meeting — approved)
**Status:** Fancy Foods copy built (Aug 11) — 3-step/9-variant sequence live in Smartlead (campaign 3792273), awaiting Yoni's review. Build prep done for the other 3 (Aug 14 — mailboxes, settings, tone reference, case studies), but actual creation moved to Yoni's own Claude account rather than run here.
**Priority:** High

#### Campaigns & search terms:
- **Fancy Foods** — search term: "fancy food"
- **Winter Fancy Fair** — search terms: "fancy fair" or "WFF"
- **Sweets & Snacks** — search term: "sweets"
- **Expo West** — search terms: "NPE", "West", or "Natural"

#### Build process (same pattern as Toy Fair):
- [x] Fancy Foods: 3-step, 9-variant spintax email sequence built and saved to Smartlead (campaign 3792273, "Eikko - Fancy Foods Q4"), tracking + HTML enabled from the start. Referenced the old "Fancy Foods q4 strategy" campaign (ID 2791019) for tone/context. Case study: Atlas Olive Oils (qualitative only, no invented figures). Review doc: `Fancy Foods - 9 Email Variants - Yoni Review.md`
- [x] Fancy Foods: lead list cleaning/consolidation complete (Aug 11)
- [ ] **Fancy Foods email sequence ON HOLD** — do not load leads or schedule until Yoni reviews the 9-variant copy and signs off
- [ ] Export leads from all relevant SmartLead campaigns per search term (Winter Fancy Fair, Sweets & Snacks, Expo West)
- [ ] Pull matching leads from the master Drive sheet (status: New, Qualified, or blank)
- [ ] Consolidate into one sheet per campaign, dedupe by email (preserve unique contacts sharing a name)
- [ ] Verify emails (QuickEmailVerification, same as Toy Fair)
- [ ] Create a new master "lead-lists" Drive folder, move the Toy Fair list into it, grant Claude access
- [ ] Build order: Fancy Foods (copy + leads done, awaiting Yoni review) → Winter Fancy Fair → Sweets & Snacks → Expo West

#### Aug 14 — Build prep for Winter Fancy Fair / Sweets & Snacks / Expo West (execution moved to Yoni's Claude account)
- [x] Confirmed all 7 requested mailbox domains already provisioned on Toy Fair Q4 (21 accounts: albertscottexperts.com, albertscottcommerce.com, albertscottoutreach.com, albertscottsolution.com, albertscottservices.com, albertscottfirm.com, albertscottny.com) — same set can be reused for all 4 campaigns
- [x] Pulled Toy Fair Q4 settings as the template (tracking on, HTML on, Mon-Fri 9am-6pm ET, stop-on-reply, 70% follow-up)
- [x] Pulled tone reference from historical campaigns: Winter Fancy Fair (id 2873879), Sweets and Snacks q4 strategy (id 2764360), Expo West intro (id 2971319)
- [x] Drafted case study assignments: Winter Fancy Fair → Atlas Olive Oils, Sweets & Snacks → Human Beanz, Expo West → Nora Seaweed Snacks
- [ ] **Not yet created** — no campaigns exist in SmartLead for these 3 yet. Yoni to build on his own Claude account using the prep above (see EOD log Aug 14 entry for full detail)
- [ ] Fancy Foods (3792273) still needs Toy Fair Q4 settings + 7-domain mailboxes applied — not yet done, also queued for Yoni's account

---

### 11. FINANCIAL MODEL AUTOMATION (Aug 11 meeting — new project)
**Status:** Scoping — first attempt hit a gap
**Priority:** Medium-high (removes a manual post-sales-call task)

#### Problem:
- Amazon sales projection models are currently built manually after each sales call, using a 15-tab Google Sheet template
- First Claude attempt only read one tab; the model's logic requires understanding all 15 tabs, especially the "Business Model" summary tab

#### Tasks:
- [ ] Eikko: refine the Claude prompt to ensure it reads all 15 tabs and understands the model's full purpose/logic before generating projections
- [ ] Test against the shared template sheet

---

### 12. LINKEDIN AUTOMATION STRATEGY (Aug 11 meeting)
**Status:** Researching approach
**Priority:** Medium (ties into Section 8e LinkedIn Outreach Agent)

#### Problem:
- Direct LinkedIn API connection is not feasible — platform policies are too strict for this use case

#### Proposed approach:
- Use a "Cloud Code" agent to simulate user actions (finding contacts, sending connection requests) rather than calling an API directly
- Likely requires a GitHub-hosted script — adds cost

#### Tasks:
- [ ] Eikko: research cost and implementation details for the Cloud Code / GitHub script approach

---

### 13. CLAUDE-SMARTLEAD-PIPEDRIVE INTEGRATION — LIVE & VALIDATED (Aug 13 meeting)
**Status:** Confirmed live and tested by Yoni himself — working as expected
**Priority:** High — unlocks everything below it

#### Validation (done):
- [x] Campaign search by keyword (found 2 "Winter Fancy Fair"-type campaigns using "winter"/"fancy fair"/"WFF")
- [x] Lead export from those campaigns (866 leads) — matched a prior manual pull exactly

#### 13a. Meeting Recap Automation (BlueDot → Pipedrive)
**Problem:** Current "Albert Scott outbound ops morning run" script only pulls from Calendly notifications, missing direct calendar entries.
- [ ] Connect Google Calendar to Claude for a complete daily meeting digest (update the morning script)
- [ ] Build the post-meeting flow: Claude pulls BlueDot summary + recording link → adds as a note on the matching Pipedrive deal

#### 13b. Pipedrive Overdue Activity Triage
- [ ] Build a Claude flow: pull all overdue Pipedrive activities for Yoni's owner ID (26939288) + each lead's full SmartLead conversation history, surfaced together for close/reschedule/reply decisions

#### 13c. SmartLead Campaign Template
- [ ] Build a reusable Claude template for rapid campaign creation (3-email sequence, day intervals, spintax variations) — same pattern already used for Toy Fair/Fancy Foods, just templated
- [ ] First use: build the Winter Fancy Fair campaign with it

#### 13d. Apify + SmartScout Lead Generation Pipeline
**Problem:** SmartScout has 585K Amazon brands with revenue data but no easy way to get targeted contacts (titles like President, Head of Sales) at scale.
- [ ] Eikko: send Yoni Apify links (Amazon seller email scraper, webinar scraper) + research other Apify use cases beyond lead scraping
- [ ] Yoni: ask Shlomo about SmartScout's plan/API access (API requires Business/Enterprise plan); coordinate with Shimi on the Claude connector
- [ ] Interim: export SmartScout brand lists as CSV for manual Claude processing
- [ ] Full pipeline once ready: SmartScout brand export (e.g. Grocery, $200K-$30M revenue) → Claude enriches parent company/domain → Apify scrapes targeted contact emails → Claude drafts custom email bodies → import to SmartLead with custom body as merge field

#### 13e. Pipedrive Lead Analysis Report
- [ ] Define lead parameters, then generate a report on all Pipedrive leads: source, status, reason not closed — to inform a re-engagement strategy for stalled high-value prospects

#### 13f. "Chief of Staff" Claude Agent
- [ ] Build a Claude agent giving Yoni a high-level overview across all projects/tasks

#### 13g. Rollout Timeline
- [ ] Create a timeline covering Claude/SmartLead/Pipedrive/SmartScout/Apify rollout

---

### 14. URGENT: ~54 BLACKLISTED SMARTLEAD MAILBOXES (Aug 14 meeting)
**Status:** Not started
**Priority:** Critical — separate issue from the Aug 10 deliverability crisis (Section 0), compounds it

**Problem:** ~54 SmartLead email accounts are blacklisted due to improper DNS setup by a previous hire. Unusable for outreach as-is.

- [ ] Remove all blacklisted accounts from every active SmartLead campaign
- [ ] Cancel the blacklisted accounts
- [ ] Purchase replacement mailboxes
- [ ] Update Toy Fair Q4X specifically to use only non-blacklisted inboxes
- [ ] Audit SmartLead provider-matching; confirm all (non-blacklisted) mailboxes are actually in use
- [ ] Coordinate cancellation/reprovisioning timeline

#### 14a. SmartLead Campaign Automation (Claude-built)
- [ ] Claude learns tone/style from existing email sequences
- [ ] Create a general email guideline doc for Claude to reference
- [ ] Claude creates campaigns end-to-end: writes copy for Yoni's approval, configures settings (timezone, schedule)
- [ ] Inbox strategy: use all available non-blacklisted inboxes on every campaign to maximize send volume
- [ ] Define SmartLead best-practice settings and apply to new campaigns

#### 14b. Lead-Gen Pipeline — SmartScout Brand → Domain Mapping
- [ ] Build Claude flow to find company domain + parent company for a 100-brand sample (rows 1001-1100 of the 6k-item SmartScout list — mid-tier sample, not top brands)
- [ ] Use SmartScout cols C, D, Z
- [ ] Add 2 Natural Products Expo West lists to the master list; dedupe

#### 14c. Lead-Gen Pipeline — Apify Amazon Seller Scraping
- [ ] Test 4 Apify scrapers against a 100-seller sample (from an 8,374-item list) to find one accepting Seller ID/Seller Name as input, returning emails
- [ ] Report findings to Yoni
- [ ] Future: use Amazon seller business names (SmartScout col L) with Apollo to find emails

#### 14d. Meeting Automation
- [ ] Build a Claude agent to auto-extract tasks/action items from meeting transcripts (reduces manual EOD-log/tracker processing)
- [ ] Send Yoni the meeting transcript summary from this meeting

---

### 15. LEAD-GEN TARGETING REFINED + NEW BLACKLIST ALERT + REPORTING (Aug 15 meeting)
**Status:** In progress — plan defined, needs verification/build before Monday review
**Priority:** High

#### 15a. Lead-Gen Targeting — Brand Contact, Not Seller (supersedes/refines Section 14b)
**Clarification:** Target the brand's own decision-maker, not the Amazon seller of the brand's product.
- [ ] Claude: find each SmartScout brand's + parent company's official LinkedIn profile (rows 1001-1100 sample)
- [ ] Claude: identify the right decision-maker per brand (e-commerce director, VP, etc., based on company size)
- [ ] Produce a target-contact list with LinkedIn URLs
- [ ] Scrape emails from that list via external tool (LinkedIn scraper or Fiverr freelancer) — Apollo subscription not approved, so no direct Apollo email lookup
- [ ] Prepare a detailed written plan for Monday's review with Yoni

#### 15b. NEW: Second Domain-Blacklist Alert (90% of 111 mailboxes) — separate from Section 14's ~54-account DNS issue
**Problem:** SmartLead notification claims 90% of all 111 mailboxes are blacklisted. Conflicts with SmartLead's own inbox health check (NS records show correct). Open SmartLead support ticket exists.
- [ ] Verify independently using external blacklist-checker tools before treating the 90% figure as real — **confirmed still open as of Aug 18 GitHub audit: no diagnosis doc/script/finding exists anywhere in the repo**
- [ ] Report findings to Yoni

#### 15c. SmartLead Campaign Automation — CONFIRMED LIVE
- [x] "Create Campaigns" Claude agent operational — automates campaign setup, generates spintax-ready sequences for review (this is Section 14a, now live). Note: doesn't appear in the `smartlead-api-client` repo's commit history, so it likely runs via the SmartLead MCP connector rather than the custom CLI.

#### 15d. Campaign Analytics Reporting System — ✅ DONE (confirmed via GitHub audit, Aug 18)
- [x] Claude agent for interactive SmartLead analytics dashboard built on branch `claude/campaign-analytics-reporting-ui39uf`: core computation module, CLI, self-contained HTML dashboard (KPI tiles, flagged-campaign table, bounce/open bar charts, targeting-refinement lead tables, inbox health), synthetic fixtures for offline testing, scheduled-run prompt (Aug 14)
- [x] Scope: all campaigns created after July 1, 2026 — implemented
- [x] Cadence: on-demand + weekly — implemented
- [x] Alert threshold: bounce rate above average — implemented, plus a fix (Aug 14) so tracking-disabled campaigns don't get false-flagged for "0 opens"
- [x] Reorganized for presentation (exec summary, anchor nav, print styles) — Aug 17

#### 15e. Side Project (optional, weekend-only, does not affect core work)
- [ ] Research Arc Ads (AI UGC video creator) + Yoni's in-progress "Arc Ads specialist" Claude agent

**Next meeting:** Monday — finalize the lead-generation plan with Yoni

---

### 16. GITHUB REPO AUDIT FINDINGS (Aug 18) — new completed work + gaps not previously tracked
**Source:** Full commit history review of `salesmanager-crypto/smartlead-api-client`, all 10 branches, Aug 13-17 activity.

#### Newly confirmed DONE (not previously in this tracker):
- [x] **Lead-list/export tooling built out extensively** (branch `claude/smartlead-export-leads-csv-30x469`, Aug 13-17): Google Drive integration, Google Sheets client, end-to-end "new campaign sheet" pipeline (SmartLead export by name filter → merge Drive source tab → dedupe into named master tab), and an account-wide "export every lead, dedupe by lead ID not email" script landing within 27 of SmartLead's reported total. **This directly covers Section 10's lead-consolidation step for Winter Fancy Fair/Sweets & Snacks/Expo West — ready to use, not still-to-build. Also means the "Master lead list organization (paused)" item in the Priority Order below is likely resolved — confirm with Yoni.**
- [x] Bug fix: SmartLead's `/campaigns/{id}/status` endpoint requires POST not PATCH (was 404ing) — fixed Aug 14, affects start/pause/stop campaign calls.
- [x] Domain-block standing rule updated — synced into `Smartlead-Pipedrive-Automation-Workflow.md` (see Section 3/5 of that doc): OOO and Wrong Person replies are never domain-blocked, full stop.
- [x] New reference doc: "Email deliverability roles/responsibilities" (Aug 13).

#### Confirmed still PENDING (no repo evidence):
- [ ] Apify integration — only an `APIFY_TOKEN` placeholder added (Aug 17). No scraper script, no seller-sample test run yet.
- [ ] LinkedIn brand-contact targeting flow (Section 15a) — zero repo evidence. Needs to be built before Monday's review.
- [ ] ~54 blacklisted mailbox removal/replacement (Section 14) — can't be confirmed or denied via repo (SmartLead-dashboard action, not a code change). Confirm directly with Yoni.

---

---

## PRIORITY ORDER (Recommended)

0. **CRITICAL (Immediate):**
   - [ ] Verify the Aug 15 alert claiming 90% of 111 mailboxes are blacklisted (conflicts with SmartLead's own health check — needs independent verification before acting on it)
   - [ ] Remove ~54 blacklisted SmartLead mailboxes from all campaigns, cancel, purchase replacements (Aug 14 — separate issue from the 90%/111 alert above)
   - [ ] Update Toy Fair Q4X to use only non-blacklisted inboxes
   - [ ] Resolve remaining SmartLead warm-up blocks (20 mailboxes)
   - [ ] Plain-text vs. HTML research + findings shared with Yoni
   - [x] Fix Time Doctor screencast settings — done Aug 11
   - [ ] Fix broken SmartLead Claude connector on Yoni's account (send API key to Shimi)

1. **DONE:**
   - [x] Toy Fair campaign LAUNCHED (Aug 11) — ACTIVE, leads loaded, sending Mon-Fri 9am-6pm ET
   - [x] Toy Fair copy — Yoni's final revision approved and live
   - [x] Toy Fair lead consolidation — done Aug 7, verified via QuickEmailVerification
   - [x] T Expo campaign — copy polish, settings, launch all confirmed done Aug 11

2. **HIGH (Approved Aug 11):**
   - [ ] Build 4 new lead campaigns: Fancy Foods → Winter Fancy Fair → Sweets & Snacks → Expo West
   - [ ] Create master lead-lists Drive folder, move Toy Fair list in, grant Claude access

2a. **MEDIUM (Next Week):**
   - [ ] Master lead list organization — flagged "paused" here, but GitHub audit (Aug 18) shows Yoni built extensive export/dedupe tooling for this Aug 13-17. Likely resolved or in a different state than "paused" — confirm before resuming.
   - [ ] Email account audit (paused, resume per Eikko)
   - [ ] Claude shared project access — research + propose to Yoni
   - [ ] Financial model automation — refine Claude prompt to read all 15 tabs
   - [ ] LinkedIn automation — research Cloud Code/GitHub script approach + cost
   - [ ] Transfer SmartLead↔Pipedrive automation to Yoni's Claude account

3. **LOW (Future / Strategic):**
   - [ ] SmartScout prospecting pipeline (data cleaning phase first)
   - [ ] Daily Workflow Hub (Pipedrive/SmartLead/Gmail consolidation)
   - [ ] Lead re-engagement system
   - [ ] Meta Ads Director, LinkedIn Ads Strategist, LinkedIn Outreach Agent
   - [ ] Additional trade-show campaigns (based on master list)

---

## RESOURCES & DOCUMENTATION

**Workflows:**
- RESOURCES/Workflows/Smartlead-Pipedrive-Automation-Workflow.md — Full workflow + hourly manual/browser fallback procedures (appendix)
- Albert Scott case studies — Atlas, BeYoutiful, MouthWatchers, Objet D'Art, etc.

**Spreadsheets:**
- Master Campaigns: https://docs.google.com/spreadsheets/d/1WjxXVym9Ie4YFk5ePIc9OahqyVE-ENpDjzpBFrROuEQ/
- Toy Fair Leads: https://docs.google.com/spreadsheets/d/1b-OoKMmbGiBw4pHswrjDz4kN3-LLno34nDa5oLTduDk/
- 2025 Lead Blast Lists Folder: https://drive.google.com/drive/folders/148YV2D4AUArgYFEJUZXnzDSaLgpOk_P9

**Systems:**
- Smartlead: Master Inbox + Campaigns Dashboard
- Pipedrive: Lead/contact management
- Gmail: salesmanager@albertscott.com (Calendly booking monitoring)

---

## NOTES FOR NEXT SESSION

- **Yoni's Preferences:** Clear instructions, ask before executing, live task tracking in Google Sheets
- **Claude's Role:** Build systems, refine copy, organize data, validate before launch
- **Model Choice:** Sonnet/Opus for complex multi-step data pulls (vs. Haiku for simpler tasks)
- **Copy Standards:** Natural English, human-sounding, not AI-generated tone
- **Messaging:** Focus on scaling existing Amazon presence (not just entry-level)

---

**Next Meeting:** TBD  
**Questions/Blockers:** None currently  
**Ready to Execute:** T Expo polish + Toy Fair consolidation
