# CMO Agent System — Build Notes & Open Threads

**Built:** 2026-08-25 | **Branch:** `claude/cmo-agent-system-build-i8ejv4` | **Status:** Built, pending Eikko's review

Records what was built, what's owed elsewhere, and the assumptions made where the source spec wasn't reachable. Delete or fold into a PRD once everything below is closed.

---

## 🔴 Owed: chief-of-staff routing line

**One line is owed to `chief-of-staff`'s routing table:**

> marketing / SEO / brand / outbound engagement → `cmo`

It could not be added at build time because **`.claude/agents/chief-of-staff.md` does not exist yet**. The build prompt's fallback was to record it in `PROJECTS/DRAFT PRD - 2026-08-25 - Chief of Staff Orchestrator.md` — **that file doesn't exist either** (see below). It's recorded here instead, per Eikko's call on 2026-08-25.

**Action:** whoever builds `chief-of-staff`, add that row to its routing table and close this thread.

---

## 🔴 Both PRDs unreachable at build time

Neither PRD the build prompt named as binding could be found:

| Expected | Searched |
|---|---|
| `PROJECTS/PRD - CMO Agent System (DRAFT).md` | Repo (both branches), full git history, Notion — not found |
| `PROJECTS/DRAFT PRD - 2026-08-25 - Chief of Staff Orchestrator.md` | Same — not found |

The Notion connector was live and returned all three source prompts on request, so this wasn't a connector failure. Most likely both PRDs are uncommitted local files on Eikko's machine.

**Eikko's call (2026-08-25):** build from the prompt alone and reconcile against the PRD afterward.

**Action:** when the PRD surfaces, diff it against the six built files. The prompt carried the PRD's headline decisions inline (hybrid delegation, track selection, phase gates, the tool-status corrections), so drift should be small — but it hasn't been checked, and "PRD wins on conflict" hasn't been applied.

---

## What was built

| File | Purpose |
|---|---|
| `.claude/agents/_shared/cmo-intake.md` | Merged intake form — track-scoped, de-duplicated from three source forms |
| `.claude/agents/cmo.md` | Marketing orchestrator (`opus`) |
| `.claude/agents/outbound-agent.md` | Outbound track, all 8 phases |
| `.claude/agents/seo-agent.md` | SEO track, zero-key, client-neutral |
| `.claude/agents/brand-agent.md` | Brand track, all 8 phases, tool-gated |
| `TEMPLATES/Client Marketing Brief Template.md` | Persisted output → `CLIENT PROFILES/<Client> - Marketing Brief.md` |

Registered in `.claude/agents/README.md` (10 → 14) and root `CLAUDE.md` (roster line only — no routing block; that's `chief-of-staff`'s).

---

## 🟡 Environment discrepancies — verify on Eikko's machine

These were checked from a cloud container holding a fresh clone. **Eikko's local install may differ** — none of these were treated as blockers, but each is a claim an agent file now makes that couldn't be confirmed here.

| Claim in the build prompt | What this container showed |
|---|---|
| `claude-seo` plugin v2.2.4 installed | Not present. `seo-agent.md` is written assuming it is |
| `ui-ux-pro-max` installed | Not present. `brand-agent.md` Phase 3 and the Phase 5 QA gate both depend on it |
| `remotion` installed | Not present. `brand-agent.md` Phase 6 references it |
| `impeccable` with `/impeccable audit\|polish\|document` | Only the `impeccable-anti-slop-catalog` reference skill is available — not the slash commands the Phase 5 QA gate calls for |
| `taste-skill`, `emil-design-eng` + siblings in `.claude/skills/` | Available at account level, but **there is no `.claude/skills/` directory in this repo** |
| Higgsfield `plan_type: free`, 0 credits | Not independently verified — `brand-agent.md` requires a runtime credit check before any generation phase regardless, so this is safe either way |

**Action:** confirm the four missing tools are installed locally, or soften the affected lines in `seo-agent.md` and `brand-agent.md`.

---

## 🟡 `PROJECTS/Pending/` doesn't exist

Referenced by both root `CLAUDE.md` and `PROJECTS/README - Builder Pipeline.md` as the drop folder for approved PRDs, but the directory isn't in the repo. Not touched by this build — flagging because the builder pipeline can't work without it.

---

## Open threads

| # | Thread | Owner | Raised | Blocking |
|---|---|---|---|---|
| 1 | Add the routing line to `chief-of-staff`'s table | Whoever builds `chief-of-staff` | 2026-08-25 | `cmo` being reachable through the global router |
| 2 | Diff the built files against the real CMO PRD | Eikko | 2026-08-25 | Sign-off on the build |
| 3 | Confirm `claude-seo`, `ui-ux-pro-max`, `remotion`, `impeccable` commands are installed locally | Eikko | 2026-08-25 | `seo-agent` and `brand-agent` running as written |
| 4 | Create `PROJECTS/Pending/` or drop the references to it | Eikko | 2026-08-25 | Builder pipeline |
