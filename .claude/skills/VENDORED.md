# Vendored third-party skills

Skills copied in from outside repos. **Pinned to commit SHAs, not branches.** Nothing here
auto-updates; a bump is a deliberate, reviewed change.

## Inventory

| Skill | Upstream | Pinned SHA | Upstream date | License | Files |
|---|---|---|---|---|---|
| `animate/` | [emilkowalski/skills](https://github.com/emilkowalski/skills) → `skills/animate/` | `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7` | 2026-08-21 | MIT © Emil Kowalski | `SKILL.md`, `RECIPES.md` — both verbatim |
| `design-critique/` | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) → `skills/web-design-engineer/references/critique-guide.md` | `aaf9a82f5efd73e87cc0998edc398e75bfc35901` | 2026-07-12 | MIT © ConardLi | `critique-guide.md` verbatim; `SKILL.md` written locally as a wrapper |

## Review status

Both vendored files were read end-to-end before install. Neither contains scripts, shell
commands, network calls, credential reads, or writes outside the project. The only external
references are two prose links to easing reference sites in `animate/SKILL.md`.

`design-critique/SKILL.md` is ours, not upstream — the upstream file is a reference document
loaded by a larger skill, so it needs a wrapper with frontmatter to be invokable standalone.

## Install policy

- Pin commit SHAs, never track a branch.
- Read every `SKILL.md` end-to-end before installing.
- No auto-update. Re-diff against upstream on any deliberate bump.
- Skills that carry scripts do not go in here — they run in a throwaway container, never in a
  session holding live connector credentials (Gmail, Pipedrive, Smartlead, GitHub).
- Do not edit vendored files in place; the diff check below is only meaningful while they are
  byte-identical to upstream.

## Re-diff against upstream

```sh
# animate
git clone --depth 1 https://github.com/emilkowalski/skills /tmp/emil-skills
git -C /tmp/emil-skills fetch --depth 1 origin d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7
diff -ru /tmp/emil-skills/skills/animate .claude/skills/animate

# critique rubric
git clone --depth 1 https://github.com/ConardLi/garden-skills /tmp/garden-skills
git -C /tmp/garden-skills fetch --depth 1 origin aaf9a82f5efd73e87cc0998edc398e75bfc35901
diff -u /tmp/garden-skills/skills/web-design-engineer/references/critique-guide.md \
        .claude/skills/design-critique/critique-guide.md
```

## Loading rules

- One opinionated design system per session. Do **not** load `apple-design` and
  `design-taste-frontend` together unless the work is gesture/motion UI — that is ~23k tokens
  of partially conflicting direction, and stacked systems average out into mush.
- `animate` builds motion from scratch. It is not the codebase-wide audit — that is upstream's
  `improve-animations`, which is not installed here.
- `design-critique` judges; it does not build. Route its fix list to the building skills.
