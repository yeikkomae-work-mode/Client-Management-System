---
description: Set up (or update) a recurring end-of-day sync for a client — Notion command center + client folder + agent kickoff
argument-hint: [client-name]
---

Set up a daily end-of-day automation for client: **$ARGUMENTS**

## 1. Resolve the client

- Match `$ARGUMENTS` against `CLIENT PROFILES/*.md` (fuzzy match on name, including nicknames in parentheses like "Satlas" or "Albert Scott").
- If no confident match, list the close candidates and ask which one.
- Read that profile to confirm: client's Notion command center (page/workspace name or URL, if documented), and which folders under `PROJECTS/`, `OUTPUT/`, and `RESOURCES/` belong to this client.
- If the profile doesn't name a Notion page, search Notion (`notion-search`) for a page/database matching the client name and confirm the match with me before proceeding — don't guess silently.

## 2. Confirm scope with me before scheduling

Ask only what's missing:
- What time should this run each day (default suggestion: 6:00 PM local)?
- Confirm the Notion command center page/database to sync.
- Confirm which agents should run as part of this (default: **project-manager** for the daily rollup, **cfo** for anything money-related on this client; add **file-organizer** if the client's folder tends to accumulate loose files, add **inbox-triage** if this client has a dedicated inbox).

## 3. Create the recurring schedule

Use the `schedule` skill to create a daily cron routine named `eod-sync-<client-slug>`. The routine's prompt should instruct the agent to, in order:

1. Pull current state from the client's Notion command center (pages/tasks/databases) via the Notion MCP tools.
2. Compare against the local client folder(s) identified in step 1 — flag drift (local files/edits not reflected in Notion, or Notion changes not reflected locally). Do not silently overwrite either side; surface conflicts.
3. Reconcile what's safe to reconcile automatically (e.g. append new local file references to the Notion tracker); leave ambiguous conflicts as a flagged list for me to resolve.
4. Run **project-manager** to produce an end-of-day rollup for this client (completed today, open items, blockers).
5. Run **cfo** if there's anything money-related to record for this client (payment received, invoice prep). Note `cfo` never reports an hours figure — no EOD log records one.
6. Run any additional agents confirmed in step 2 (e.g. file-organizer, inbox-triage).
7. Write the EOD summary back to the client's Notion command center as a dated entry (or to `OUTPUT/<client>/EOD Logs/` locally if Notion write access isn't available), and end with a short summary message to me.

## 4. Confirm

After creating the schedule, show me the routine name, the daily run time, and the next scheduled run. Remind me I can list/edit/delete it later with the `schedule` skill.
