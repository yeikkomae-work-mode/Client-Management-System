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

---

## Dry-run findings (2026-08-25, Satlas)

`cmo.md` + `cmo-intake.md` were executed against Satlas read-only. **Step 0 worked** — it produced 7 genuine questions out of 30+ possible, with everything else recovered from files. The connector-status-first rule earned its place immediately: without it the run would have reported PlusVibe as MCP-connected and pulled a different client's numbers into a Satlas brief.

**Fixed during the build** (all in the new files):

| Finding | Fix |
|---|---|
| `<Client>` didn't resolve — "Satlas" globs nothing, the file is `Chris Drew - Profile (Satlas).md`. Would have produced two Marketing Briefs for one client across sessions | Client-key resolution rule added to `cmo-intake.md` Step 0 — files are keyed by **person name**, company in parens |
| Step 0 never checked client-specific **skills**. `satlas-cold-email` holds approved copy verbatim, merge-field syntax, warmup floors, segmentation rules — none of it in any profile | Skills added as Step 0 source #3, with why |
| `cmo` has no Bash but intake told it to cross-check infra against Zapmail/InboxKit/Porkbun — APIs it structurally can't reach | Line rewritten to delegate the live check to `outbound-agent` and date any quoted figures |
| Phase gates assume an interactive session; a subagent runs once and returns | Gate mechanics documented in `cmo.md` — a gate is stop-and-return, re-invocation is the sign-off |
| No procedure for when documented sources disagree with each other | Added to `cmo.md`: report all versions with paths, say which the live artefacts reflect, don't pick |
| Delegation table never handed over the Marketing Brief path | Added to all three specialist rows |

---

## 🔴 Cannot fix in scope — for Eikko

These are defects in **existing** files. The build was scoped not to touch the 10 existing agents, client profiles, or skills, so they're recorded rather than fixed.

**1. `reply-handler` can't reach Satlas's inbox — cross-client data risk.**
`reply-handler.md` has `tools: Read, Grep, Glob, Write` — no Bash. Satlas's PlusVibe Master Inbox is reachable *only* by raw API key over Bash, and the native PlusVibe MCP connector points at Yoni's account. So routing Satlas replies to `reply-handler` returns either nothing or **another client's replies**. `cmo.md` now warns about this and routes around it, but the underlying agent still can't do the job. Fix is one word in its frontmatter — `Bash` — plus a per-client reach note.

**2. Satlas cadence is written two ways.** `copywriter.md` says Day 0/3/7; the `satlas-cold-email` skill says Day 1/4/8 (SKILL.md line 87 and `references/copywriting.md` line 33–35). **These are the same cadence** — both are +3 then +4 days — just different conventions for whether the send day is Day 0 or Day 1. Not a behavioural conflict, but two numbering schemes for one rule will eventually get read as two rules. Worth aligning `copywriter.md` to the skill's Day 1/4/8, since that's what the launched campaigns use.

**3. The `satlas-cold-email` skill points at a path that doesn't exist.** It declares its references at `/mnt/skills/user/satlas-cold-email/references/`; they actually live at `/root/.claude/skills/synced/satlas-cold-email/references/`. An agent following that pointer literally gets nothing.

**4. `copywriter` has `Write` and no read-only mode.** Dry-running anything that delegates to it depends purely on prompt compliance from an agent holding the Write tool. Worth considering a read-only convention for dry runs.

**5. Satlas has no documented approval-authority line.** Yoni's profile has a hard one ("all campaigns through Yoni or Rachel"). Satlas's records that Spencer and Chris review copy, but says nothing about who can approve a *launch*, or whether Ally can. `outbound-agent` will hold at the gate regardless, but the gate has no named owner.

**Not reproduced:** the dry-run could not fire the `copywriter` delegation, because it ran as a `general-purpose` stand-in with no subagent-spawning tool. `cmo.md` declares `Task` in its frontmatter, so a real `cmo` invocation after a Claude Code restart should be able to. **The delegation path is therefore structurally correct but untested end-to-end** — worth confirming on the first real run.

---

## Second dry-run (2026-08-25, Satlas, agents registered)

Re-run once Claude Code picked up the four new agents. It surfaced three defects the stand-in run couldn't, because the stand-in wasn't `cmo` and didn't have `cmo`'s tool grant.

| Finding | Severity | Fix |
|---|---|---|
| **`cmo` declared `Task` but the runtime didn't grant it** — every delegation in the file was dead, making the orchestrator an intake-only agent | 🔴 Blocking | Frontmatter now declares **both `Task` and `Agent`**; harnesses differ on what the subagent-dispatch tool is called, and unknown names are dropped silently rather than erroring |
| **Every `_shared/` path was wrong from the working directory.** Written agent-dir-relative (`_shared/connector-status.md`) while every other path in the same files was repo-root-relative. The existing agents all use the full `.claude/agents/_shared/…` form — my files broke house convention and the first two reads of each run failed | 🔴 Blocking | All 8 occurrences rewritten to `.claude/agents/_shared/…` |
| **The Step 0 skill check produced a false negative.** The run globbed `.claude/skills/` in the repo, found nothing, and reported "no Satlas skill exists" — while `satlas-cold-email` was in the user-level directory the whole time, holding the approved copy verbatim, RANDOM tag format, warmup floors and segmentation rules | 🔴 Blocking | Instruction now checks repo **and** `~/.claude/skills/` **and** `~/.claude/skills/synced/`, and forbids reporting absence from a single glob |

Also tightened: Satlas named explicitly as the archetypal `reply-handler` reach failure; `cmo` now quotes `connector-status.md`'s `Last verified` date rather than just reading the file; and a generic instruction to check the client profile for a copy-review gate before returning any copy.

### 🔴 Two more for Eikko — existing files, out of scope

**6. The Hillary — Finance Broker campaign contradicts the 3-email rule.**
`CLIENT PROFILES/Chris Drew - Profile (Satlas).md` line 106 records it as **4 steps**, migrated. The documented Satlas rule (same profile, lines 187–191) is a 3-step sequence, "not 6 — more steps = more spam flags." It's held in draft, not launched, so nothing is sending — but **this is the exact segment a new finance-broker campaign would target**, and it needs resolving before copy is commissioned: approved exception, or migration artefact to correct?

**7. `copywriter.md`'s Satlas summary drops two rules that are in the profile.**
Missing: the **signature spec** (name + phone + RANDOM close — profile line ~194) and the **Spencer-and-Chris copy review before launch** (line ~192). The file does say "read the full profile before writing — this is a summary, not the whole spec," so it's mitigated by instruction. But the review requirement is an *approval rule*, and an agent trusting the summary would route copy straight past it. `cmo.md` now carries a generic instruction to check the profile for a review gate; folding the two rules into `copywriter.md`'s Satlas line would close it properly.

**Correction to finding 2 above (cadence):** with the skill now actually readable, the profile says Day 0/3/7 and the skill says Day 1/4/8. Still the same cadence — both are +3 then +4 — so this remains notation, not behaviour. Worth aligning, not urgent.

## Open threads

| # | Thread | Owner | Raised | Blocking |
|---|---|---|---|---|
| 1 | Add the routing line to `chief-of-staff`'s table | Whoever builds `chief-of-staff` | 2026-08-25 | `cmo` being reachable through the global router |
| 2 | Diff the built files against the real CMO PRD | Eikko | 2026-08-25 | Sign-off on the build |
| 3 | Confirm `claude-seo`, `ui-ux-pro-max`, `remotion`, `impeccable` commands are installed locally | Eikko | 2026-08-25 | `seo-agent` and `brand-agent` running as written |
| 4 | Create `PROJECTS/Pending/` or drop the references to it | Eikko | 2026-08-25 | Builder pipeline |
| 5 | Give `reply-handler` Bash, or permanently route raw-key-only inboxes to `outbound-agent` | Eikko | 2026-08-25 | Phase 8 on Satlas — live cross-client data risk |
| 6 | Align `copywriter.md`'s Day 0/3/7 to the skill's Day 1/4/8 | Eikko | 2026-08-25 | Nothing yet — same cadence, two notations |
| 7 | Fix the `satlas-cold-email` skill's references path | Eikko | 2026-08-25 | Any agent following the declared pointer |
| 8 | Confirm `copywriter` delegation fires end-to-end on the first real `@cmo` run | Eikko | 2026-08-25 | Untested — registry needed a restart |
| 9 | Document Satlas's launch approval authority (can Ally sign off?) | Eikko | 2026-08-25 | Phase 6 gate has no named owner |
| 10 | Resolve the Hillary — Finance Broker 4-step vs 3-email rule contradiction | Eikko + Chris | 2026-08-25 | Any new finance-broker copy |
| 11 | Fold the signature spec + Spencer/Chris review gate into `copywriter.md`'s Satlas line | Eikko | 2026-08-25 | Copy shipping unsigned or unreviewed |
