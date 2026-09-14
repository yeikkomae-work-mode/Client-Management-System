# Central Command — Dashboard v2

Fresh build from the Miro wireframe (https://miro.com/app/board/uXjVHscoGBw=/).
PRD: `PROJECTS/DRAFT PRD - 2026-09-02 - Central Command Dashboard v2.md` (approved 2026-09-02).
Replaces the deprecated `.claude-dashboard/` (kept as reference only).

## Structure

- `index.html` — the whole app: single self-contained page, no build step. Open directly in a browser.
- `data/*.js` — per-source data files (`window.CC_*` globals), refreshed by Claude sessions / sync scripts via connectors. Script-tag globals (not fetch) so the page works from `file://`.

## Design system

**eikko-ds v2.0 "Cobalt"** (`BRAND/eikko-ds/tokens.json`) since 2026-09-08. Light is the default; dark is the opt-in variant (toggle in the user chip, persisted in localStorage as `cc-theme`).
Paper `#FAFAF7` / raised `#FDFDFB`, ink ramp `#151515 → #EDEDE8`, accent Cobalt `#2851E3` (text-safe; `#3D62F5` fills in dark), status tones from the token file.
Type: Schibsted Grotesk 800 (titles), Figtree (body), Martian Mono (numbers, labels; never uppercase). Loaded from Google Fonts.
Radius: 12px surfaces (documented dashboard-only exception, PRD 2026-09-07), pill controls, 4px data-ends.
Chart series: eikko-ds has no categorical hue set, so series use the ordinal ink ramp `--s1…--s4` plus the accent, and every series also carries a legend or label. Status colours are reserved for status.
User chip avatar = portrait mark (`BRAND/eikko-ds/assets/portrait/avatar-32.svg`, inlined). Sidebar badge stays the Flow mark.
Previous dark-first version archived at `_archive/index.v2-dark.html`. QA record: `OUTPUT/Design QA/2026-09-08 - Design QA - Central Command reskin.md`.

All multi-select filters must use the ARIA listbox pattern (see PRD success criteria).

## Build phases (one at a time, demo each)

1. ✅ Shell — sidebar, top bar (PHT greeting, CDO weather via Open-Meteo, news line), routing, clickable cards, theme toggle
2. ✅ Client Profiles (Notion Clients DB, engagement color tiers) + data layer synced 2026-09-02: clients.js, tasks.js, meetings.js, finance.js (entries + debts), campaigns.js (from local scan)
3. ✅ Task/Projects kanban (Notion Task Tracker + ARIA-listbox filters, projects panel, dashboard summary card)
4. ✅ Finance (salary table, salary calendar w/ month nav, weekly+monthly income/bills/saved bars, debt tracker w/ due-soon flags, dashboard MTD card)
5. ✅ Calendar (Google Calendar sync in data/calendar.js — join links/passcodes excluded (public repo) — merged month grid w/ Notion meetings + salary dates, ongoing-work banners, Upcoming panel, dashboard card)
6. ✅ Inbox (Gmail synced to data/inbox.js — subjects only, no bodies (public repo); 4 category cards w/ unread badges + dashboard counts. Noise excluded: job-alert digests, promos, OTPs)
7. ✅ Campaigns (LIVE Smartlead pull for Albert Scott — 19 actives w/ per-campaign progress bars + open/click/reply/bounce; Satlas documented table; Cüneyt summary; Zapmail domain chips; dashboard strip = 4 newest actives)
8. ✅ Extras (Agents roster w/ Notion log links, Resources w/ Tech Radar chips + connector status table, Mood Board = design palette, Tools card w/ live/needs-auth/retired counts)

**All 8 phases complete (2026-09-02).** Remaining wishlist: real news sync for the greeting bar, PlusVibe Sellervate workspace key for Cüneyt per-campaign stats, a projects data source (panel is keyword-heuristic), mood board image source, scheduled data re-sync.

## Data rule

Repo is public — never commit secrets, tokens, or raw email bodies into `data/`.
