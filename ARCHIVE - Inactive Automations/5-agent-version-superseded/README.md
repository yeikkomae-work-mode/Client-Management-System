# 5-Agent Version — Superseded by the 10-Agent Team

**Archived:** 2026-08-13 (the five agent files) · 2026-08-25 (`ECO - Chief of Staff Guide.md`)

These five (`clients.md`, `comms.md`, `ops.md`, `metrics.md`, `strategy.md`) were the original functional-split Claude Code subagents, built earlier the same day before Eikko brought in a researched 10-agent front-office/back-office architecture. They were replaced by the 10 agents now in `.claude/agents/` at the repo root.

**Added 2026-08-25 — `ECO - Chief of Staff Guide.md`.** This is the orchestrator doc for exactly those five agents: it describes coordinating CLIENTS · COMMS · OPS · METRICS · STRATEGY, so it belongs with them rather than in the top-level automations archive. It came from `TEMPLATES/01 Automation Daily Routine/`, where its title collided with the current `.claude/agents/chief-of-staff.md` (built 2026-08-25) and its 3-client narrative roster was five clients short of the real one. Moved, not deleted, with a historical banner at the top of the file explaining what superseded it and where each still-accurate piece of its content actually lives now.

**If you're here looking for how routing works today, you want `.claude/agents/chief-of-staff.md`, not this folder.** Nothing in here is live.

**Why they moved here specifically (not just a subfolder inside `.claude/agents/`):** Claude Code scans `.claude/agents/` recursively, so leaving them in a nested `_archived-...` folder inside that directory still surfaced them in the live agent list, duplicating/conflicting with the real 10. Moving them fully outside `.claude/agents/` — into this repo-wide archive, alongside the other retired automation docs — is what actually keeps them out of Claude Code's agent scan.

Kept for reference only. If any phrasing here is useful when refining the current 10, copy it over — don't move these files back into `.claude/agents/`.
