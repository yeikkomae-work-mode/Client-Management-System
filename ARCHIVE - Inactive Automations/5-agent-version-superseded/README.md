# 5-Agent Version — Superseded by the 10-Agent Team

**Archived:** 2026-08-13

These five (`clients.md`, `comms.md`, `ops.md`, `metrics.md`, `strategy.md`) were the original functional-split Claude Code subagents, built earlier the same day before Eikko brought in a researched 10-agent front-office/back-office architecture. They were replaced by the 10 agents now in `.claude/agents/` at the repo root.

**Why they moved here specifically (not just a subfolder inside `.claude/agents/`):** Claude Code scans `.claude/agents/` recursively, so leaving them in a nested `_archived-...` folder inside that directory still surfaced them in the live agent list, duplicating/conflicting with the real 10. Moving them fully outside `.claude/agents/` — into this repo-wide archive, alongside the other retired automation docs — is what actually keeps them out of Claude Code's agent scan.

Kept for reference only. If any phrasing here is useful when refining the current 10, copy it over — don't move these files back into `.claude/agents/`.
