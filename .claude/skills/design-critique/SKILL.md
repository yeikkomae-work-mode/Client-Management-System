---
name: design-critique
description: Score an existing design against a five-dimension rubric (philosophy alignment, visual hierarchy, craft quality, functionality, originality) and return a severity-sorted fix list with concrete values. Use when asked to critique, review, score, or grade a design, landing page, slide deck, dashboard, or UI — or as a self-check before shipping a page to a client. For building or animating an interface use design-taste-frontend or animate instead; this skill judges, it does not build.
---

# Design Critique

A judging skill. It scores a design that already exists and returns a prioritized fix list. It does not write or modify code — hand the fix list to `design-taste-frontend` (layout, type, colour), `animate` (motion), or the `impeccable-anti-slop-catalog` (AI tells) to act on.

## How to run it

1. **Read the design.** Screenshot, rendered page, or source — whichever is available. If you only have source, say so: craft-quality scoring is weaker without pixels.
2. **Establish the intent** before scoring. Ask what direction the design was aiming at (editorial? Swiss? Linear-style product?) and what the page's one job is. Scoring "philosophy alignment" against an unstated philosophy is guesswork — if the user can't name it, infer one from the design and state your inference in the output.
3. **Load [critique-guide.md](critique-guide.md)** and score all five dimensions against its rubrics. Weight the dimensions by output type using the weighting table in that file — a dashboard is not scored like a brand film.
4. **Walk the Top 10 common-issue catalog** in the guide as a checklist before writing the output. It catches the misses that free-form looking does not.
5. **Emit the output template** from the end of the guide, verbatim in structure: overall score, per-dimension scores with one-line reasons, Keep, Fix (sorted ⚠️ → ⚡ → 💡), Quick Wins.

## Rules that override instinct

- **Every fix carries a concrete value.** "Increase title from 32px to 56px", never "make titles bigger". A fix a reader cannot execute without asking a follow-up is not a fix.
- **Max 7 fix items.** More than that, group them ("five spacing inconsistencies" is one item).
- **No vague taste claims.** Anchor each judgement to a named principle from the guide.
- **Critique the design, not the person.**
- **A high score is allowed.** Do not manufacture findings to look thorough. If a dimension is genuinely 9, say 9 and move on.

## Iterating

Re-running after fixes is the intended loop, but treat the score as an ordering device, not a target. Chasing 10/10 on every dimension produces a design optimised for the rubric rather than for the page's job — stop when the ⚠️ and ⚡ items are gone.

## Provenance

The rubric in `critique-guide.md` is vendored verbatim from ConardLi's `garden-skills` (`web-design-engineer/references/critique-guide.md`), MIT licensed, pinned to a commit SHA. See `.claude/skills/VENDORED.md` for the SHA and the re-diff command. Do not edit it in place — if it drifts from upstream, the diff check stops being meaningful.
