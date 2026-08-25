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

---

## Third dry-run (2026-08-25) — nested delegation is a platform limit

Re-ran with `Task` **and** `Agent` both declared. **Still no dispatch tool granted.** Two runs, both harnesses' tool names, same result: in this environment a subagent cannot spawn another subagent. Confirmed by inspection — none of the original 10 agents declares a dispatch tool either.

**This is not fixable in a prompt.** `cmo.md` now handles it instead of dying on it: it checks its actual tool grant, and when no dispatch tool exists it completes intake/track-selection/brief, returns an explicit **run-list** (which agents, in what order, with the exact prompt for each including the resolved client key, brief path and skill path), and reports the delegated phases as **blocked, not completed**. It explicitly must not become the specialist and write the copy itself. Eikko or the top-level session runs the list.

**Whether this also applies on Eikko's local Claude Code is untested** — `Task`/`Agent` stay declared so delegation works automatically if the local harness permits it.

**Also fixed this round:** Step 0's shell snippets told a Bash-less agent to run `ls`/`grep` (now Glob-phrased); Step 0 said "read the skill" but not "enumerate `references/`", where the approved copy actually lives; Step 6 created the brief unconditionally with no dry-run carve-out; the stop-and-return gate had nowhere to record which phase it stopped at (**Engagement State** block added to the brief template); and `cmo`'s conflict rule now covers specs asserted by the *caller*, not just specs found in files.

### 🔴 More for Eikko — existing files, out of scope

**8. `copywriter.md` has no pointer to the Satlas skill.** Its Satlas paragraph cites only the profile. So even with delegation working, `copywriter` would most likely write from the profile summary alone and miss the approved copy, the spintax requirement and the merge-field syntax. `cmo.md` now passes the skill path in every handover, which mitigates it — but only for work routed through `cmo`. A direct `@copywriter` call still misses it. One line in `copywriter.md` closes it.

**9. The profile and the skill specify two different 5-part structures.** Profile: Hook (specific stat) → Context → Proof (small number) → Ask → Signature. Skill `references/copywriting.md`: Relevant intro → Pain point → Solution → Soft CTA → Signature. The profile has a Proof slot and no Pain slot; the skill has a Pain slot and no Proof slot. **The launched copy follows the skill's version**, with the proof number folded into the Solution beat. `copywriter.md` restates the *profile's* version. Which is canonical?

**10. Signature spec disagrees too.** Profile: "name + phone + RANDOM close." Skill: "Real name, company, phone." The approved copy uses `{{sender_signature}}` on Emails 1 and 3 and a bare first name on Email 2 — **no RANDOM close appears in any launched email**. The profile's version is not what shipped.

**11. Approved finance-broker copy already exists — and the segment isn't live anywhere.**
`references/copywriting.md` holds launched finance-broker copy verbatim (Email 1 Versions A and B, Email 2 A and B, Email 3 A, fully spintaxed, signed **Tremayne** — not Chris Drew). Meanwhile the four Instantly finance-broker segments are completed/archived and the only PlusVibe one ("Hillary — Finance Broker") sits in draft with zero leads. **So a "new finance-broker campaign" is really a refresh against approved assets, not a blank page** — and it maps directly onto the open "0.66% reply rate vs 2% target" thread. Worth framing that way before commissioning copy.

**12. Cosmetic but corrosive:** the skill's spintax section is still headed **"Instantly copy format"** (line 39) though Instantly is dead and PlusVibe is live. The format carried over intact; only the heading is stale. It's the kind of thing that makes an agent distrust a file it should be following.

---

## copywriter.md updated (2026-08-25, authorized by Eikko)

Scope was widened by explicit request to cover two changes in `copywriter.md` — otherwise untouched, as one of the original 10.

**Added:**
1. **A standing skill-check rule for every client**, not just Satlas. Globs all three skill locations, requires reading `references/` and not just `SKILL.md`, and instructs that a skill's *rules* are authoritative while its *status tables* are a dated snapshot to reconcile against campaign tracking. Written generically so it covers whatever client gets a skill next.
2. **The Satlas skill pointer** — `~/.claude/skills/synced/satlas-cold-email/`, naming what the profile summary omits (approved launched copy, sentence-level RANDOM spintax, PlusVibe merge-field syntax, 50–80 word limit, tracking off) and instructing a check for existing approved copy before drafting from scratch.
3. **The approval gate** — Spencer Hirst and Chris review all new segment copy before launch, with the open question of whether it applies to a *refresh* flagged rather than decided.
4. **The two live profile-vs-skill contradictions** flagged in place, with the instruction to follow what shipped and say so, pending Eikko and Chris settling them.

**Deliberately not done:** the signature spec was *not* resolved. The profile says "name + phone + RANDOM close," the skill says "real name, company, phone," and no RANDOM close appears in any launched email. That's a decision for Eikko and Chris (thread #14), not an edit — picking one silently is exactly what the conflict rule exists to prevent. Frontmatter untouched; `copywriter` still has `Write` and no read-only mode (thread unchanged).

---

## reply-handler.md updated (2026-08-25, authorized by Eikko)

`Bash` added, closing thread #5 — Satlas's PlusVibe inbox is raw-key-only, so without it this agent returned nothing or, via the MCP connector, another client's replies.

Bash on an agent that touches live client systems is a real capability increase, so it came with boundaries rather than on its own:

- **Account confirmation before every call**, with the specific traps named: PlusVibe MCP → Yoni's account, Smartlead MCP → Yoni only, Instantly's two unrelated accounts. Wrong account is worse than no data.
- **Reads free, writes governed, sends never.** Fetching and categorizing needs no approval; state-changing calls follow the client's documented rule; no send endpoint under any circumstances. Explicitly stated that Bash does *not* widen the existing approval permissions.
- **No raw keys in any output.**
- **Standing client-skill check**, same shape as the one added to `copywriter.md`.

**The most important addition came out of the skill, and it contradicts this agent's own general rule.** Per `references/launch-monitor.md`: **do not use PlusVibe's "add to blocklist" button or endpoint for Satlas — it blocks the single email address, not the company domain.** Satlas blocks by adding the domain to a Google Sheet named "Satlas blocklist," and **Tremayne owns that sheet and does it himself.** So on a positive reply this agent surfaces and flags; it does not call a block endpoint. Handing it Bash *without* that rule would have let it call PlusVibe's blocklist API confidently — the call would appear to succeed while the rest of the company kept getting emailed. The general "block the domain" rule now points at the per-client procedure first.

Also captured: **speed-to-lead is 10–15 minutes** on a positive reply (skill), and the Satlas section now says the reply→categorize→sync pipeline is *buildable* with Bash but that only `campaign/list` has ever been verified — probe the replies endpoints and report what actually returns, rather than assuming they exist.

## Open threads

| # | Thread | Owner | Raised | Blocking |
|---|---|---|---|---|
| 1 | Add the routing line to `chief-of-staff`'s table | Whoever builds `chief-of-staff` | 2026-08-25 | `cmo` being reachable through the global router |
| 2 | Diff the built files against the real CMO PRD | Eikko | 2026-08-25 | Sign-off on the build |
| 3 | Confirm `claude-seo`, `ui-ux-pro-max`, `remotion`, `impeccable` commands are installed locally | Eikko | 2026-08-25 | `seo-agent` and `brand-agent` running as written |
| 4 | Create `PROJECTS/Pending/` or drop the references to it | Eikko | 2026-08-25 | Builder pipeline |
| 5 | ~~Give `reply-handler` Bash~~ ✅ **Done 2026-08-25** — with account-safety, write, and send guardrails | — | 2026-08-25 | Closed |
| 6 | Align `copywriter.md`'s Day 0/3/7 to the skill's Day 1/4/8 | Eikko | 2026-08-25 | Nothing yet — same cadence, two notations |
| 7 | Fix the `satlas-cold-email` skill's references path | Eikko | 2026-08-25 | Any agent following the declared pointer |
| 8 | Confirm `copywriter` delegation fires end-to-end on the first real `@cmo` run | Eikko | 2026-08-25 | Untested — registry needed a restart |
| 9 | Document Satlas's launch approval authority (can Ally sign off?) | Eikko | 2026-08-25 | Phase 6 gate has no named owner |
| 10 | Resolve the Hillary — Finance Broker 4-step vs 3-email rule contradiction | Eikko + Chris | 2026-08-25 | Any new finance-broker copy |
| 11 | ~~Fold the Spencer/Chris review gate into `copywriter.md`~~ ✅ **Done 2026-08-25.** Signature-spec half stays open — see #14, it's a decision not an edit | — | 2026-08-25 | Closed |
| 12 | ~~Add a Satlas skill pointer to `copywriter.md`~~ ✅ **Done 2026-08-25** — plus a standing rule for all clients | — | 2026-08-25 | Closed |
| 13 | Decide the canonical 5-part structure — profile's or the skill's | Eikko + Chris | 2026-08-25 | Any conformance check on Satlas copy |
| 14 | Decide the canonical signature spec (RANDOM close isn't in shipped copy) | Eikko + Chris | 2026-08-25 | Same |
| 15 | Reframe the finance-broker ask as a refresh against approved copy, not a new write | Eikko | 2026-08-25 | Wasted work + ignoring launched assets |
| 16 | Fix the skill's stale "Instantly copy format" heading | Eikko | 2026-08-25 | Nothing — cosmetic |
| 17 | Test whether nested delegation works on Eikko's local Claude Code | Eikko | 2026-08-25 | Whether `cmo` can orchestrate directly or must return run-lists |
