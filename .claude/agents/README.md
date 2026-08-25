# Claude Code Subagents — Client-Management-System

**9 operators, a 3-agent C-suite, and one front door.** The operators split front-office
(client-facing) / back-office (internal ops), adapted from Eikko's research into this actual
system. Built 2026-08-13, replacing the earlier 5-agent functional version (kept in
`_archived-5-agent-version/` for reference, not deleted). The `chief-of-staff`
was added 2026-08-25 as Eikko's second-in-command and the front door to all of them.

## Orchestrator (sits above the front/back-office split — not one of the nine)

| Agent | Scope |
|---|---|
| `chief-of-staff` | **Eikko's second-in-command.** Runs day-to-day business administration and internal operations *directly* — keeping trackers honest, the record straight, and the system's own docs true — and routes client-facing work to the right specialist, sequences it, sanity-checks what comes back, and checkpoints session memory. **Holds the single source of truth for routing** — the request-shape → agent → files table, the authority rules, the connector rule, and the session-memory protocol all live in `chief-of-staff.md` and are not duplicated elsewhere. Invoke with `/chief-of-staff`. |

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
| `billing-auditor` | Time tracking vs. rates, monthly income/expense review, invoice prep |
| `onboarding-guide` | New client setup — folders, profile doc, welcome/questionnaire draft |
| `file-organizer` | Keeps this whole system clean — dedup, archive stale docs, fix naming, fix broken references |
| `meeting-summarizer` | Transcript → minutes + action items, pushed to task files |

## Marketing — the CMO layer (added 2026-08-25)

`cmo` is the marketing-domain orchestrator. It runs intake, picks tracks, holds the phase gates, owns the client's living Marketing Brief, and delegates — to its three track specialists and to the existing 10. It is **not** a global router: billing, inbox, meetings, task rollups, and file hygiene belong to `chief-of-staff`, and `cmo` hands those straight back.

```
cmo  (marketing engagements only)
├── outbound-agent   → cold outbound, end to end
├── seo-agent        → SEO audits and checks
└── brand-agent      → positioning, identity, website, content
        │
        └── all three delegate into the existing 10:
            market-scout (research) · copywriter (all copy)
            lead-prospector (lists) · reply-handler (inbound)
```

| Agent | Scope |
|---|---|
| `cmo` | Marketing orchestrator — intake, track selection, phase gates, owns `CLIENT PROFILES/<Client> - Marketing Brief.md` |
| `outbound-agent` | Cold outbound end to end: research → ICP → lead export → verification → copy → campaign build → domain/mailbox capacity → deliverability monitoring. Builds to DRAFT and holds |
| `seo-agent` | SEO audits via the `claude-seo` plugin — zero-key mode by default, client-neutral, narrowest command that answers the ask |
| `brand-agent` | Positioning, verbal and visual identity, brand guidelines, website, content engine, inbound campaigns. Hands outbound to `outbound-agent` |

**Delegation over duplication.** The track agents call `copywriter` rather than restating its per-client copy rules — those rules came out of real client feedback and live in exactly one file. A second copy would drift, and the drifted copy is the one that reaches a client's inbox.

**Model note:** `cmo` runs on `opus` (orchestration and gate judgement); the other 13 run on `sonnet`. One line in its frontmatter if that should change.

## Shared context (not agents — reference files the agents read)

- `_shared/connector-status.md` — **the single source of truth** for which tools are actually connected vs. broken vs. need authorizing vs. don't exist. Update this ONE file when a connector changes status; every agent, the Chief of Staff included, reads it at runtime instead of carrying its own stale copy.
- `_shared/cmo-intake.md` — the merged marketing intake form, read by `cmo` at the start of every engagement. Replaces the three separate intake forms the SEO / brand / outbound source prompts each carried. Track-scoped, so a cold-email client never sits through a brand interview. Its Step 0 requires reading the client's existing docs before asking anything.

## How to use

Sessions in this folder default to Chief of Staff mode (see the root `CLAUDE.md`) — describe the goal and
it either runs it (internal admin/ops) or routes it (everything else). Or run `/chief-of-staff` for the
cross-client picture, or `/coo <goal>` for a routing plan on one goal.

Claude Code also auto-picks a specialist from its `description` when a task clearly matches, and
you can always call one directly:

```
Use the lead-prospector agent to build Krishna's next Apollo list.
Use the billing-auditor agent for this month's income review.
Use the cmo agent to start a new outbound engagement for <client>.
```

Note on structure: delegation happens from the main thread — a subagent can't spawn another
subagent — so the Chief of Staff is the mode the main thread runs in, not a dispatcher you hand
off to and wait on.

## The three chaos-prevention rules baked into these agents

(The Chief of Staff enforces all three across whatever it routes, and carries the authority table that decides what stays inside its own standing authority and what stops for Eikko's yes.)

1. **Human-in-the-loop:** `inbox-triage`, `copywriter`, `reply-handler`, and `onboarding-guide` all draft only — nothing sends, publishes, or launches without Eikko's explicit yes/edit/skip. This is written into each of their files, not left to chance.
2. **Folder separation:** each agent is scoped to touch only the client files relevant to the task at hand unless it's explicitly a cross-client rollup (like `project-manager`'s daily briefing).
3. **Central control room:** ✅ built — [🎛️ VA Command Center](https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b) in Notion (workspace: "eikko mae ybanez's Space"). Has a Front-Office log, Back-Office log, a Clients database (status/tools/next action per client), and a Connector Status page mirroring `_shared/connector-status.md`. Agents should write their output there once they're actually running live — right now the sections are seeded but empty since none of the 10 are on a live schedule yet. Note: this is a *different* Notion workspace from the Satlas team one that owns the "Cold Email" hub discussed earlier — that one still needs separate access.

## Known connector gaps (see `_shared/connector-status.md` for full detail)

PlusVibe (Chris Drew) is pointed at the wrong account. Satlas/Fractio/Albert Scott Gmail accounts, HubSpot, Slack, and Fireflies aren't connected yet. Instantly, Porkbun, Zapmail, InboxKit, MillionVerifier, Lemlist, and LinkedIn have no Claude connector at all and stay manual/browser-assisted regardless of agent setup.
