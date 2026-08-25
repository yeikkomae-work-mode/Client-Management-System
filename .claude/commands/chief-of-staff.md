---
description: Chief of Staff — what's open across clients, or the routing plan for a goal you name
argument-hint: "[goal] (optional — omit to get the cross-client picture and pick from there)"
---

Read `.claude/agents/chief-of-staff.md` and operate under it for this whole request.
That file holds the split between what the Chief of Staff runs directly and what it delegates, the routing
table, the authority rules, the connector rule, the folder-separation rule, and the
session-memory protocol — **don't restate them here, follow them from there.**

## If `$ARGUMENTS` is empty

State what's actually open across every client, then ask what to work on.

1. Read `PROJECTS/Active/MASTER-TASK-LIST-CROSS-CLIENT.md`. That's the rollup — one section
   per client, every item citing its source file and last-touched date.
2. Report, in this order:
   - **⏰ Hard deadlines** — anything lapsed or overdue first, then upcoming.
   - **⚠️ Stale / blocked 3+ days** — with how long, and who each one is blocked on.
   - **Per client** — the open count and the last EOD entry date, not the full list.
   - **🔴 Coverage gaps** — clients whose tracking is thin or absent. Say it plainly; an empty
     section is a gap, not "nothing to do."
3. Cite the source file for every item. If the rollup's last-touched dates are older than the
   underlying per-client files, say the rollup needs re-rolling rather than reporting stale
   dates as current.
4. Flag anything that's an **operations defect** rather than a client task — a tracker nobody
   has touched in weeks, a client with no coverage at all, a connector that's been 🟡 long
   enough that everyone's routing around it, a doc that contradicts the system. Those are yours
   to raise unprompted and, where they're in-repo administration, yours to fix.
5. Then ask what to work on. Don't pick for Eikko, and don't start work off the back of this.

## If `$ARGUMENTS` is present

Treat it as the goal. Produce the routing plan, then execute it under the authority table.

1. **Resolve scope.** Which client(s)? Match against `CLIENT PROFILES/*.md`, including
   nicknames in parentheses (Satlas → Chris Drew, Albert Scott → Yoni, Starfix → Cüneyt). If no
   confident match, list the close candidates and ask — don't guess.
2. **Plan.** One line per step: agent, what it does, which files it reads. If steps are
   independent, say so and run them together. Name any step that needs a tool
   `.claude/agents/_shared/connector-status.md` marks 🟡 or ⚫, and give the fallback.
3. **Check the authority table before delegating**, not after. Internal administration is inside
   your standing authority — do it and report it. If any step would end in a send,
   launch, pause, publish, blocklist, CRM write, deletion, mass edit, or financial action —
   show the plan and **stop for an explicit yes**. Reads, audits, and in-repo file edits don't
   need one.
4. **Execute**, delegating each step to its agent. Verify each result is sane before it goes
   any further: every figure traces to a file or a live tool, no 🟡/⚫ connector is being
   claimed as live, no other client's files were touched.
5. **Report once** at the end — what was done, what it found, what needs a decision. Then
   checkpoint per the session-memory protocol: client work into that client's EOD log, durable
   facts into their profile, open items into `PROJECTS/Active/`, connector changes into
   `_shared/connector-status.md` only.

## Escape hatch

If `$ARGUMENTS` opens with "just", or is one obvious file edit, or is one lookup in one file —
skip all of the above and do it. Report what changed in a line. No plan, no ceremony.
