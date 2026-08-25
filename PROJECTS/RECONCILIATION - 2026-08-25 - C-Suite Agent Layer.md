# Reconciliation — C-Suite Agent Layer

**Date:** 2026-08-25 · **Covers:** `cto` (built), `chief-of-staff`, `cfo`, `cmo`
**Why this exists:** four C-suite PRDs were drafted the same day in parallel sessions that couldn't see each other. Two are already built on branches. This is the single reconciled view.

---

## ⚠️ Two findings that change the plan

### 1. Two of these are already built — on branches you haven't merged

Five PRs are open on `yeikkomae-work-mode/Client-Management-System`:

| PR | What | State |
|---|---|---|
| #1 | Tremayne sign-off fix | Open, draft |
| #2 | Penji AdsPower integration | Open, draft |
| #3 | Amazon Seller Instantly→PlusVibe migration | Open, draft |
| **#4** | **master-list fix + `chief-of-staff` orchestrator** | **Open, draft — 3 commits, 26 files** |
| **#5** | **CMO agent layer** | **Open, draft** |

So the CoS PRD's "blocked on the master-list fix" is stale — PR #4 does both. And `cto` was built by me today **directly on `main`, uncommitted**.

**The collision:** PR #4, PR #5, and my CTO build all edit the same four index files — `CLAUDE.md`, `README.md`, `.claude/agents/README.md`, `.claude/commands/agent-manager.md`. Each writes its own agent-roster line. Merging them in any order produces conflicts or a roster that's wrong in three different ways. **Fix: one roster reconciliation pass after the last merge, not four independent edits.** See build order below.

### 2. You have zero scheduled tasks. Both "live" automations are fiction.

Checked the scheduler directly. The only registered tasks are five one-shot PR check-ins created today. Specifically:

- **`daily-eod-sync` does not exist.** `ARCHIVE - Inactive Automations/README.md` says it's "the only one actually running." It isn't. Nothing has been syncing your EOD logs.
- **`project-builder-check` does not exist.** `PROJECTS/README - Builder Pipeline.md` says it runs every 3 hours. It doesn't. `Pending/`, `In-Progress/`, `Done/`, and `Failed/` are all empty because **the pipeline has never run once.**

**Consequences you need to act on:**

1. **Do not drop a PRD in `PROJECTS/Pending/` expecting it to get built.** Nothing is watching that folder. Every PRD in this batch says "move it to Pending once approved" — that instruction is dead.
2. Two status docs actively lie. `ARCHIVE - Inactive Automations/README.md` and `README - Builder Pipeline.md` both need correcting.
3. This is precisely the failure mode the `cto` agent was built to catch, and it was true on the day it was built. Its own baseline has been corrected.

---

## The reconciled hierarchy

CFO and CMO independently arrived at the same structure — CoS as front door, specialists beneath. CTO was built without that positioning and needs the same line. Reconciled:

```
chief-of-staff              ← front door: session routing, context carry, root CLAUDE.md routing block
│
├── cmo                     ← marketing engagements
│   ├── seo-agent
│   ├── brand-agent
│   └── outbound-agent
├── cfo                     ← money: income, expenses, cash flow, debt   (absorbs billing-auditor)
├── cto                     ← tech: tool verdicts, what to build, stack decay, skills   ✅ BUILT
│
└── the 10 operators        ← inbox-triage · copywriter · lead-prospector · reply-handler ·
                              market-scout · project-manager · onboarding-guide ·
                              file-organizer · meeting-summarizer   (billing-auditor retired by CFO)
```

**Roster math when all four land:** 10 operators − `billing-auditor` (retired) + `chief-of-staff` + `cmo` + 3 CMO specialists + `cfo` + `cto` = **16 agents.**

That is a lot of routing surface. The CMO PRD already flags that five enabled plugins add ~50 skill descriptions per session and will blunt routing for daily client ops. Sixteen agents on top of that is a real risk to the thing you actually do all day. **Flagged, not resolved — see Decision 4.**

---

## Conflicts and resolutions

### C1 — Tool register duplication (CFO ↔ CTO) 🔴

CFO creates a Notion **Tools & Subscriptions** data source plus `OUTPUT/Monthly Reports/Tools & Subscriptions Register.md`. CTO already has `RESOURCES/Tech Radar.md` with a cost column. Two registers of what you pay for will drift inside a month.

**Resolution — split by question asked, one owner per field:**

| Question | Owner | Lives in |
|---|---|---|
| What does it cost, who pays, when does it renew, is it lapsing | **CFO** | Notion Tools & Subscriptions + monthly register |
| Should this exist at all — adopt / trial / hold / kill | **CTO** | `RESOURCES/Tech Radar.md` |

The radar's cost column becomes a **pointer**, not a second source: it states *client-paid* or *you-pay* and links to the register for the number. CFO's register carries a `Radar verdict` column that reads from the radar. Neither agent writes the other's field.

**Already applied:** CFO's confirmed finding — *every client tool is client-paid; your entire business expense base is ₱7,600/mo (Claude ₱7,000 + iCloud ₱600)* — has been written into the Tech Radar so the two agree from day one.

### C2 — Who may write `connector-status.md` 🔴

`cto.md` forbids the CTO from editing it: it's a human-verified single source of truth, the CTO flags drift and you verify. But the CFO PRD says *"This rule is now recorded in `_shared/connector-status.md` so every agent reads it"* — i.e. CFO writes to it. Both can't be right.

**Resolution:** the file has two kinds of content. **Connector status rows are human-verified — no agent writes them.** **Standing rules recorded at the bottom** (like "all client tools are client-paid") may be written by an agent, in a clearly separated `## Standing rules` section, with a date and the agent that added it. CFO's line goes there. CTO still writes nothing.

### C3 — Session-open drift check (CoS ↔ CTO) 🟡

CoS opens every session with a context/routing protocol. CTO opens its own sessions with a 3-line stack-decay check. If CoS becomes always-on via root `CLAUDE.md`, both fire and one is noise.

**Resolution:** different objects. **CoS owns session continuity** — what were we doing, which client, what's unresolved. **CTO owns stack decay** — what's silently broken. CTO's check fires only inside a `cto` session, never globally. CoS's routing table gets one line: *"stack looks stale / is X still running → `cto`"*.

### C4 — Root `CLAUDE.md` ownership 🟢 (already agreed)

CMO and CFO both correctly ceded the routing block to CoS. CTO takes the same rule: **roster line only, no routing block.** Already true of what I built.

### C5 — Model cost 🟡

CTO ships on `opus`. The CoS PRD's open question #2 leans opus for routing/contradiction work. If CoS, CFO, and CTO all run opus, spend rises against a **₱7,000/mo Claude line that is 92% of your business expense base**.

**Recommendation:** opus for `cto` (judgment is its only output) and `chief-of-staff` (routing errors cascade). `cfo` on sonnet — arithmetic and report assembly against live Notion data, where correctness comes from reading the right rows, not from reasoning depth. Revisit if CFO produces a wrong close.

### C6 — `billing-auditor` deletion 🟡

CFO deletes `.claude/agents/billing-auditor.md` and edits three index files. Combined with PR #4 and #5 doing their own roster edits, that's four uncoordinated writers. **Resolution:** deletion happens in the CFO build; the roster is reconciled once, at the end, by the pass described below.

---

## Build order

Revised for what's actually on branches, and for the fact that nothing is watching `Pending/`.

| # | Step | Why here |
|---|---|---|
| 0 | **Commit the `cto` build on `main`** | It's uncommitted. Do this before merging anything or it gets clobbered. |
| 1 | **Review + merge PR #4** (master-list + chief-of-staff) | Biggest file count (26). Landing it first makes every later conflict smaller. Also unblocks nothing else — CMO and CFO are standalone by design. |
| 2 | **Review + merge PR #5** (CMO layer) | Already built. Expect roster conflicts with #4 — resolve toward the reconciled roster above. |
| 3 | **Build CFO** from `PROMPT - 2026-08-25 - CFO Agent Build`, with C1/C2 amendments applied | Not yet built. The Notion Expenses migration inside it is the one irreversible step in this whole batch — keep its confirmation gate. |
| 4 | **One roster reconciliation pass** | Single edit to `CLAUDE.md`, `README.md`, `.claude/agents/README.md`, `agent-manager.md` reflecting the final 16-agent roster with `billing-auditor` removed. Replaces four independent edits. |
| 5 | **Fix the two lying status docs** | `ARCHIVE - Inactive Automations/README.md` (daily-eod-sync is dead) and `README - Builder Pipeline.md` (pipeline never ran). |
| 6 | **Decide the automation question** | Either re-create `daily-eod-sync` + `project-builder-check` as real scheduled tasks, or delete the docs that promise them. Right now you have the worst version: documentation of automations that don't exist. |

---

## Decisions needed from you

1. **C2 — connector-status write authority.** Standing-rules section writable by agents, status rows human-only? Or nothing writable by any agent, and CFO's rule lives in its own file?
2. **C5 — models.** Opus for CoS + CTO, sonnet for CFO — or all three opus and accept the spend?
3. **Step 6 — the dead automations.** Rebuild them as real scheduled tasks, or delete the docs? A third option: rebuild `daily-eod-sync` only, and kill the builder pipeline outright since you're building interactively anyway.
4. **16 agents.** Do you actually want `seo-agent`, `brand-agent`, and `outbound-agent` as three separate agents under CMO, or would CMO with three modes route better? More agents means more description surface competing on every routing decision, in a folder where your daily work is client ops, not marketing builds.
5. **CoS authority** — still open from its own PRD: literal full-auto within a session, or the carve-out table (auto for reads and internal writes, stop-and-confirm for client-facing and destructive). That PRD recommends the carve-out and flags that full-auto overrides your own standing rule. It's still unanswered.

---

*Nothing in this document has been built. The `cto` agent is the only thing from this batch on disk, and it is uncommitted on `main`.*
