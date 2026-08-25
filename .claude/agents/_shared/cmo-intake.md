# CMO Intake — One Form, Three Tracks

**Read by `cmo` at the start of every marketing engagement.** This replaces the three separate intake forms that used to live in the SEO, Brand & Marketing, and Outbound Outreach source prompts — those overlapped heavily on client/offer/URL and made a cold-email client sit through a full brand interview. One form now, scoped by track.

**Companion file:** `_shared/connector-status.md` — check it before promising any tool. Never ask the client or Eikko to paste an API key into this form; keys live in `.env` and are referenced by variable name only.

---

## Step 0 — Check before asking

**Re-asking a documented fact is the specific failure this system exists to prevent.** Before you ask a single question, read:

1. `CLIENT PROFILES/<Client> - Profile*.md` — offer, voice rules, approval rules, key people, rate, tooling
2. `CLIENT PROFILES/<Client> - Marketing Brief.md` — if it exists, this engagement is already partly briefed; you're topping it up, not starting over
3. `OUTPUT/Campaign Tracking/` — live campaigns, lead volumes, past performance, what's already been tried
4. `OUTPUT/End-of-Day Reports/<Client> - End of Day Log.md` — recent state, open issues
5. `PROJECTS/Active/` — any live task list for this client

Then present what you already know back to Eikko as a filled-in draft and ask only for the gaps. Format it as:

> **Already documented** (correct me if stale): offer, URL, voice rules, current infra…
> **Need from you:** target niche for this campaign, lead volume, CTA.

If a documented fact looks stale (a profile says "trial day one" and it's two months later), flag the staleness rather than either trusting it or silently re-asking.

---

## Step 1 — Track selection (ask this first, always)

**Which tracks does this engagement actually need?**

- ⬜ **Outbound** — cold email/DM campaigns, lead lists, sending infrastructure
- ⬜ **SEO** — audits, technical/on-page, schema, content briefs, GEO/AI-search
- ⬜ **Brand** — positioning, verbal/visual identity, guidelines, website, content engine

More than one can apply. **Most of Eikko's engagements are outbound-only** — Satlas, Krishna, Penji, Starfix, Chris Caffera all run cold email with no brand or SEO scope. Do not run brand or SEO questions at a client who only wants campaigns; skip straight past those sections.

Only ask the Universal block plus the sections for the ticked tracks. If Eikko ticks all three, say plainly that this is a full engagement and confirm before running the long form.

---

## Step 2 — Universal (every engagement, every track)

Asked once here so no track re-asks it.

| Field | Notes |
|---|---|
| Client name + website URL | Check `CLIENT PROFILES/` first — most are already documented |
| What the business sells, and to whom | The offer. One or two sentences, in the client's own framing |
| Industry / business type | SaaS, local business, e-commerce, publisher, lead-gen, B2B service, other |
| Existing proof | Case studies, testimonials, named clients, concrete results — the raw material for both copy and positioning |
| Primary objective | Awareness / leads / sales / credibility. One primary, not four |
| Geographic & language scope | Markets being sold into |
| Competitors | Named by the client, or `market-scout` finds them — say which |
| Timeline | Launch date or deadline to work backward from, if any |
| Budget & resource constraints | E.g. no paid ad budget, one person executing, fixed monthly retainer |
| Approval rule | Who signs off, and on what. Some clients have hard ones — Yoni's "all campaigns through Yoni or Rachel before launch" is non-negotiable and lives in his profile |

---

## Step 3 — Outbound track

Only if Outbound is ticked. Everything here is per-campaign, not per-client — a second campaign for the same client re-runs this section and nothing above it.

| Field | Notes |
|---|---|
| Target niche for **this** campaign | The market being prospected into, **not** the client's own niche. E.g. "US Series A–C SaaS, VP Sales / Head of RevOps" |
| Campaign goal / desired CTA | E.g. "book a 15-min call." Drives every step's ask |
| Target lead volume for this run | E.g. 1,000 exported → ~700 verified after `ok`-only filtering |
| Sending infrastructure available | Domains and mailboxes already live, warmed, and connected — or "none yet." Cross-check against Zapmail / InboxKit / Porkbun rather than taking a number on trust |
| Sending platform for this client | PlusVibe, Smartlead, Instantly, or Apollo-native. Per-client and easy to get wrong — see `_shared/connector-status.md` for which account each connector is actually authenticated to |
| Apollo account | Which key applies (`APOLLO_API_KEY` or `APOLLO_API_KEY_ACCOUNT2`). Name the variable, never the value |
| Catch-all inclusion | Default is `ok`-only. Only ask if volume is tight — catch-alls add reach and bounce risk |

---

## Step 4 — SEO track

Only if SEO is ticked. Per-task, not per-client — each audit re-runs this.

| Field | Notes |
|---|---|
| Ask | Full audit / single page / schema / technical / GEO / local / e-commerce / content brief / hreflang / backlinks / sitemap. Be specific — this picks the command |
| Repeat client? | If yes, offer a drift baseline so future audits show what changed |
| Client's own Google credentials | Default is zero-key mode. Only if the client supplies GSC/GA4 access does that change |
| Paid extension available | DataForSEO, Ahrefs, Firecrawl, SE Ranking, Profound, Bing Webmaster, Unlighthouse. Default is none |
| Output | Client-facing (Markdown + PDF) or internal (Markdown only) |

If the industry wasn't given in Step 2 and the ask is industry-specific (local, e-commerce), ask once — don't guess.

---

## Step 5 — Brand track

Only if Brand is ticked. This is the long one; don't run it unless the engagement genuinely includes brand work.

| Field | Notes |
|---|---|
| Brand goal | Launch from zero / reposition / refresh |
| Existing assets to keep | Name, logo, colors, domain, social handles — anything that's fixed |
| Naming needed? | If yes, Phase 2 includes name candidates |
| 3–5 adjectives | How the brand should feel |
| Brands admired / to avoid resembling | Both directions are useful |
| Website in scope? | Whether Phase 5 runs at all, and on what stack |
| Content platforms | Which the client will actually run — don't plan a calendar for a platform nobody will post to |

---

## Step 6 — Write it down

The moment intake is answered, `cmo` creates `CLIENT PROFILES/<Client> - Marketing Brief.md` from `TEMPLATES/Client Marketing Brief Template.md` and fills in everything gathered. **Nothing downstream depends on chat history.** If a brief already exists, update it in place and date the change in its decisions log.

Do not edit `CLIENT PROFILES/<Client> - Profile*.md` from intake. The profile is the client relationship; the brief is the marketing engagement. If intake surfaces something that contradicts the profile, flag the contradiction to Eikko and let him decide which is right — never silently overwrite a profile.
