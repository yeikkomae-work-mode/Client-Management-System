# Tools & Subscriptions Register

**Owner:** `cfo` agent · **Created:** 2026-08-25 · **Last updated:** 2026-08-25

The cost side of every tool this operation touches: what it costs, who pays, when it renews, and what happens if it lapses.

**Boundary:** this file answers *cost, who pays, renewal, lapse risk*. Whether a tool **should exist at all** is `cto`'s call in `RESOURCES/Tech Radar.md`. The `Radar verdict` column below **reads from** that file — `cfo` does not set it, and the radar's cost column is a pointer back here rather than a second number. Neither agent writes the other's field.

**Standing rule:** *all client tools are client-paid unless explicitly documented otherwise.* They run on the client's account and bill to the client; they are not part of Eikko's expense base.

---

## Eikko's own expense base

| Tool | Cost | Who pays | Renewal | Radar verdict | Lapse risk |
|---|---|---|---|---|---|
| Claude (Claude Code + connectors) | **₱7,000/mo** | Eikko | Monthly | ✅ ADOPT | **Critical.** The entire agent system stops. ~92% of Eikko's business expense base — a model choice on any agent is a real financial decision. |
| Notion | Not documented — **gap** | Eikko | Not documented | ✅ ADOPT | High. VA Command Center, finance data, Tech Radar twin all live here. |
| Fathom | Not documented — **gap** | Eikko | Not documented | ✅ ADOPT | Medium. Meeting transcripts stop; displaced Fireflies, so there's no fallback configured. |
| Gmail ×5 (1 native + 4 custom OAuth) | ₱0 | — | — | ✅ ADOPT | Low. |

**Total documented internal spend: ₱7,000/mo.** Three internal tools have no cost on file — that's a real gap, not a zero. Do not report a total as complete until they're filled.

## Client-paid — billed to the client, not to Eikko

| Tool | Client | Cost | Who pays | Radar verdict | Notes |
|---|---|---|---|---|---|
| Apollo | Satlas, Krishna | Not documented | Client | ✅ ADOPT | Chris Caffera has no documented key *or* payer — gap flagged by `cto`. |
| Smartlead | Yoni (Albert Scott) | Not documented | Client | ✅ ADOPT | Yoni's account only. |
| PlusVibe | Satlas | Not documented | Client | ✅ ADOPT | ⚠️ MCP connector points at Yoni's account — never use it for Satlas. |
| Instantly | Cüneyt (Starfix) | Not documented | Client | ✅ ADOPT | Separate account from Satlas's dead one. |
| Pipedrive | Yoni | Not documented | Client | ✅ ADOPT | — |
| Porkbun | Satlas | Not documented | Client | ✅ ADOPT | 25 domains verified 2026-08-22. Domain renewals are the lapse risk here. |
| Zapmail | Satlas | Not documented | Client | ✅ ADOPT | Health 22.65/100, 0/30 warmed — an operational problem, not a cost one. |
| InboxKit | Satlas | Not documented | Client | ✅ ADOPT | 15 domains / 30 mailboxes. |
| Hostinger | Cüneyt (Starfix) | Not documented | Client | ✅ ADOPT | 3 domain-scoped tokens. |
| MillionVerifier | Shared / per-run | Not documented | Client | ✅ ADOPT (manual) | Manual 2FA by design. Credit-based. |

## Zero-cost or inactive

| Tool | Cost | Radar verdict | Notes |
|---|---|---|---|
| Higgsfield | ₱0 (free plan, **0 credits**) | ⏸️ HOLD | Every `generate_*` call fails. No spend, no capability. Costs nothing to keep; costs a wasted run to forget. |
| HubSpot · Slack | ₱0 | ⏸️ HOLD | Connectors exist, unauthorized. |
| Fireflies | ₱0 | ❌ KILL | Displaced by Fathom. Confirm no subscription is still billing. |
| Instantly (Satlas) | ₱0 | ❌ KILL | Migrated off, key dead. **Confirm the subscription was actually cancelled** — a migrated-off tool that still bills is the classic leak. |
| Lemlist | Unknown | ❓ UNCLEAR | Browser-only. Still in use for Caffera? If yes it has a cost nobody has recorded. |
| Asana / ClickUp / Trello | ₱0 | ❌ KILL | Not in use. |
| Design/frontend skills bundle | ₱0 | 🧪 TRIAL (review 2026-09-30) | Claude Code-native. |

---

## Open cost gaps — the honest list

These are unresolved. They are listed rather than estimated.

1. **Notion, Fathom** — internal tools, no cost on file. Until filled, the ₱7,000/mo internal total is a floor, not a total.
2. **Every client tool** — no cost documented for any of them. The standing rule says the client pays, so this doesn't hit Eikko's P&L, but "client-paid" is currently an assumption per tool rather than a verified fact per tool.
3. **Instantly (Satlas)** and **Fireflies** — both killed. Neither has a confirmed cancellation. A tool that was migrated off but never cancelled bills silently and indefinitely. **Check these first.**
4. **Lemlist** — status unknown, cost unknown, possibly still active for Chris Caffera.

## Renewals to watch

| What | Date | Source |
|---|---|---|
| `sellervate.net` domain renewal (Cüneyt/Starfix) | **2026-09-28** | Confirmed not yet renewed as of the 2026-08-16 recheck — `OUTPUT/End-of-Day Reports/Cüneyt - End of Day Log (Starfix).md` |

No other renewal dates are documented anywhere in this system. That is itself the finding.
