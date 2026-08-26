# PRD — Albert Scott SEO Automation Suite

**Date:** 2026-08-26
**Requested by:** Eikko (task list pasted, scope drafted by Claude for review)

> **⚠️ Needs re-scoping before sign-off — n8n retired 2026-08-26.** Everything below (Scope items 1–5, the Constraints section, and Plan steps 2–7) was written assuming "the existing Albert Scott n8n workflow" as the automation backbone. Eikko has since removed n8n as the automation platform for this client entirely — no replacement has been chosen yet. **Do not sign off on this PRD as written**; it needs a fresh pass once a platform decision exists, since right now every scheduled/automated piece of this plan has nowhere to run.

## Problem

Albert Scott's SEO work is currently one-off and manual: the 2026-08-26 SEO Health Check (`SEO Audit - 2026-08-26.md`, same folder) was a point-in-time pull, not a running system. There's no standing process for:

1. Tracking keyword rank movement or getting alerted on traffic drops
2. Recurring technical crawls (broken links, page speed, indexation)
3. A live reporting dashboard pulling from analytics sources
4. Structured, repeatable keyword research (clustering by semantic/intent groups)
5. Schema markup generation at catalog scale, rather than page-by-page

## Feasibility findings (before scoping further)

Checked what's actually connectable from this environment before committing to a plan — this changes the scope meaningfully from the tool names in the original task list:

- **No MCP connector exists for Keyword.com, Screaming Frog, Looker Studio, or DashThis.** Checked the connector registry directly — none of the four are integrable as named. Screaming Frog in particular is a licensed desktop application; it isn't something a cloud session can run crawls from at all without a separate always-on machine.
- **What we already have, that covers most of the same ground:**
  - `albertscott.com` runs **All in One SEO Pro**, which exposes its own REST API (`aioseo/v1`) — already used for the 2026-08-26 audit. It includes a built-in SEO analysis engine (broken/missing meta, thin content, etc.), and **AI schema-generation endpoints** (`/aioseo/v1/ai/schema`, `/aioseo/v1/schema/templates`) that look like a direct fit for item 5 (structured data at scale) with no new tool needed.
  - **Site Kit by Google** is installed and active on the site (confirmed in the audit), which is the standard bridge to Google Search Console and PageSpeed Insights data — once its Search Console connection is authorized (audit found Search Statistics not yet connected in AIOSEO either), that's real rank/traffic/indexation data without a paid third-party tool.
  - The **Albert Scott n8n workflow** (`PROJECTS/Active/Albert Scott - n8n Migration/`) already has the automation backbone (scheduled triggers, an Anthropic API credential for AI classification/clustering work, Google Sheets logging) that items 3 and 4 would slot into rather than needing new infrastructure.
- **OpenRush** and **Helium 10** (Amazon-specific — notable given Albert Scott is an Amazon growth agency) showed up in the connector registry as installable rank-tracking/SEO options, if Eikko wants a real third-party tool rather than the Google-native path above.

## Success criteria

- [ ] Keyword rank tracking runs on a schedule (weekly minimum) for an agreed keyword list, with an alert path for meaningful ranking or traffic drops
- [ ] A recurring technical scan flags broken links, slow pages, and indexation problems without a manual run
- [ ] A live dashboard shows current SEO/traffic metrics, refreshed automatically, viewable without asking Claude for a fresh pull each time
- [ ] Keyword research output is grouped into semantic clusters with intent labels, not a flat list
- [ ] Schema markup is generated for new/uncovered catalog items (products, blog posts) without hand-authoring each one

## Scope

This build covers **Albert Scott only** (`albertscott.com`), building on the existing n8n workflow and AIOSEO's REST API rather than introducing net-new SaaS subscriptions by default. Concretely, pending the open questions below:

1. **Rank tracking + alerts** — via Google Search Console data (once Site Kit's connection is confirmed authorized) pulled into n8n on a schedule, with a threshold-based alert (Slack/email/Sheet flag) on ranking or click drops. *Third-party alternative (Keyword.com or similar) only if Eikko confirms an existing account/API key.*
2. **Technical audits** — scheduled n8n runs against AIOSEO's `seo-analysis` endpoints (already proven reachable), diffed run-over-run to surface new errors, not just a snapshot. Page-speed data via PageSpeed Insights API (free, keyless) rather than Screaming Frog.
3. **Reporting dashboard** — data logged to Google Sheets by n8n (matching the existing run-log pattern in the n8n migration doc), connected to a **Looker Studio** report (Looker Studio itself needs no paid connector — it reads Sheets/BigQuery natively; this is a report-building task, not an integration problem).
4. **Keyword research/clustering** — n8n workflow: pull a keyword export (from GSC or a provided seed list) → Anthropic API (existing credential) clusters by semantic similarity and tags search intent → output to Sheets.
5. **Structured data at scale** — n8n workflow hitting AIOSEO's own `/aioseo/v1/ai/schema` and `/aioseo/v1/schema/templates` endpoints for any post/product missing schema, batch-processed rather than one at a time.

## Non-goals

- Not licensing or standing up Keyword.com, Screaming Frog, or DashThis unless Eikko confirms he wants to pay for/already has one of these specifically — no connector exists for any of them today, so that path means building against their raw APIs from scratch, which is more effort than the Google/AIOSEO-native path above.
- Not migrating or replacing anything already live in the Albert Scott n8n workflow — this extends it with new scheduled sub-workflows, doesn't touch the existing reply-triage/Calendly flows.
- Not applying any of this to other clients in this pass — Albert Scott only.
- Not making any live changes to albertscott.com content/settings as a side effect of building this — same read-first, confirm-before-write posture as the SEO audit.

## Constraints

- Builds on the existing Albert Scott n8n workflow and its credentials (Pipedrive, Smartlead, Anthropic, Google Sheets — per `README - n8n Setup.md`), none of which are wired in yet as of the last check (`list_credentials` still returns zero).
- Uses the `sales` WordPress Administrator app password (already tested, read-only so far) for AIOSEO REST calls — write actions (e.g., applying generated schema) need explicit confirmation before going live, consistent with how the SEO audit was handled.
- Google Search Console / PageSpeed access depends on Site Kit's own connection status on the site, which hasn't been verified beyond confirming the plugin is active.
- No budget assumption — this PRD assumes free/already-available tools (Google APIs, AIOSEO's built-in engine) unless Eikko says otherwise in the open questions below.

## Plan

1. Confirm Site Kit's Google Search Console connection is actually authorized on albertscott.com (read-only check).
2. Wire the 4 outstanding n8n credentials per `README - n8n Setup.md` (blocked on Eikko creating them in the n8n UI — same blocker as the reply-triage workflow).
3. Build the technical-audit sub-workflow first (lowest new-surface-area — reuses AIOSEO endpoints already proven in this session).
4. Build the keyword clustering workflow (reuses the Anthropic credential once wired).
5. Build the rank-tracking + alert workflow once GSC access is confirmed.
6. Set up the Google Sheets run-log → Looker Studio dashboard.
7. Build the schema-generation batch workflow against AIOSEO's AI schema endpoints, with a manual-approval step before anything is applied to live content.

## Open questions

- Does Eikko already hold accounts/API keys for **Keyword.com**, **Screaming Frog**, or **DashThis** specifically — or is the Google/AIOSEO-native substitution above acceptable? This materially changes scope and effort for items 1, 2, and 3.
- What keyword list / seed set should rank tracking and clustering start from — existing Search Console query data, or a list Eikko provides?
- What counts as a "traffic drop" worth alerting on (a % threshold, absolute click/position drop, time window)?
- Who receives alerts, and where (Slack, email, a Sheet someone checks)?
- For schema generation: which catalog (blog posts, a specific product type) is the priority, and should generated schema auto-publish or queue for review first?

---

**Sign-off:** ⬜ Approved to build — Eikko
