# Claude Code Subagents — Client-Management-System

**10-agent team**, split front-office (client-facing) / back-office (internal ops), adapted from Eikko's research into this actual system. Built 2026-08-13, replacing the earlier 5-agent functional version (kept in `_archived-5-agent-version/` for reference, not deleted).

## Front-office (client-facing)

| Agent | Scope |
|---|---|
| `inbox-triage` | Scans/categorizes email across all connected accounts, drafts replies for approval |
| `copywriter` | Cold email sequences, LinkedIn posts, campaign copy — per-client voice/rules |
| `lead-prospector` | Apollo-based list building, campaign create/launch/pause/delete |
| `reply-handler` | Categorizes inbound campaign replies (Smartlead/PlusVibe Master Inbox), syncs qualified leads to Pipedrive, handles blocklisting |
| `market-scout` | Competitor/industry trend research per client niche |

## Back-office (internal ops)

| Agent | Scope |
|---|---|
| `project-manager` | Daily task rollup across clients, morning briefing, EOD wrap-up, quick task capture |
| `cfo` | **Money.** Monthly close (P&L), cash-flow + 60-day runway, debt payoff modelling, tool/subscription cost register, per-client profitability, invoice prep. Notion `Finance Tracker and Bills` is its source of truth. Read-only Notion tools by design — every write is confirmed with Eikko first. **Replaced `billing-auditor` 2026-08-25**, carrying forward its rate card and its full 2026-08-13 known-gaps audit verbatim. |
| `onboarding-guide` | New client setup — folders, profile doc, welcome/questionnaire draft |
| `file-organizer` | Keeps this whole system clean — dedup, archive stale docs, fix naming, fix broken references |
| `meeting-summarizer` | Transcript → minutes + action items, pushed to task files |

## Shared context (not agents — reference files the agents read)

- `_shared/connector-status.md` — **the single source of truth** for which tools are actually connected vs. broken vs. need authorizing vs. don't exist. Update this ONE file when a connector changes status; every agent reads it instead of carrying its own stale copy.

## How to use

Claude Code auto-picks a subagent from its `description` when a task matches, or call one directly:

```
Use the lead-prospector agent to build Krishna's next Apollo list.
Use the cfo agent for this month's income review.
```

## The three chaos-prevention rules baked into these agents

1. **Human-in-the-loop:** `inbox-triage`, `copywriter`, `reply-handler`, and `onboarding-guide` all draft only — nothing sends, publishes, or launches without Eikko's explicit yes/edit/skip. This is written into each of their files, not left to chance.
2. **Folder separation:** each agent is scoped to touch only the client files relevant to the task at hand unless it's explicitly a cross-client rollup (like `project-manager`'s daily briefing).
3. **Central control room:** ✅ built — [🎛️ VA Command Center](https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b) in Notion (workspace: "eikko mae ybanez's Space"). Has a Front-Office log, Back-Office log, a Clients database (status/tools/next action per client), and a Connector Status page mirroring `_shared/connector-status.md`. Agents should write their output there once they're actually running live — right now the sections are seeded but empty since none of the 10 are on a live schedule yet. Note: this is a *different* Notion workspace from the Satlas team one that owns the "Cold Email" hub discussed earlier — that one still needs separate access.

## Known connector gaps (see `_shared/connector-status.md` for full detail)

PlusVibe (Chris Drew) is pointed at the wrong account. Satlas/Fractio/Albert Scott Gmail accounts, HubSpot, Slack, and Fireflies aren't connected yet. Instantly, Porkbun, Zapmail, InboxKit, MillionVerifier, Lemlist, and LinkedIn have no Claude connector at all and stay manual/browser-assisted regardless of agent setup.
