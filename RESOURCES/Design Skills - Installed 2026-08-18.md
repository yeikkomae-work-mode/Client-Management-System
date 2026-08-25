# Design/Frontend Skills — Installed 2026-08-18

Eikko found and asked to apply these third-party design resources. All saved as account-wide Cowork skills (visible in every session, not folder-specific) via `save_skill`. Logged here so future sessions know they exist without re-explaining.

## What's installed

| Skill | Source | What it's for |
|---|---|---|
| `design-taste-frontend` | github.com/Leonxlnx/taste-skill | Anti-slop frontend design rules for landing pages, portfolios, redesigns. Dial-based (variance/motion/density), design-system selection, typography/color/layout discipline, em-dash ban, full AI-tells list, pre-flight checklist. **Explicitly not for dashboards.** |
| `emil-design-eng` | github.com/emilkowalski/skills | Emil Kowalski's (Vercel/Linear, creator of Sonner) animation and UI-polish philosophy. Animation decision framework (should it animate / what easing / what duration), spring physics, component details (button press feedback, popover origin-awareness), performance rules. Reviews must output a Before/After/Why markdown table. |
| `animation-vocabulary` | github.com/emilkowalski/skills | Reverse-lookup glossary — turns a vague description ("the bouncy popover thing") into the precise animation term, for naming effects when prompting. |
| `apple-design` | github.com/emilkowalski/skills | Apple's WWDC design principles translated for the web — gesture/spring interactions, momentum, translucent materials, typography (tracking/leading), and Apple's 8 design foundations (purpose, agency, craft, etc.). |
| `impeccable-anti-slop-catalog` | impeccable.style (Paul Bakaus) | Reference checklist of 64 patterns that mark an interface as AI-generated (purple gradients, side-tab cards, nested cards, italic serif heroes, em-dash overuse, etc.) — extracted as static knowledge since the real Impeccable tool needs a live dev server + CLI hooks that don't run in Cowork. |

## Why these and not others

Two things were evaluated and **not** installed wholesale:
- Most of taste-skill's and emilkowalski's code-specific instructions (React/Next.js, Tailwind v4, the Motion/`framer-motion` library, GSAP skeletons, Phosphor icons, npm install commands) assume a real dev project with a build pipeline. Cowork artifacts don't run that pipeline — HTML artifacts are single self-contained files (only Chart.js/Grid.js/Mermaid via CDN), React artifacts are capped to a fixed library allowlist. Each installed skill has a note at the bottom flagging which parts are Cowork-applicable (the design judgment) vs. dev-project-only (the framework code).
- Impeccable itself (the actual tool, not its anti-pattern list) is a CLI + hooks + live-browser-injection system requiring `npx impeccable install` and a running app to hook into — there's nothing to "install" as a Cowork skill in the literal sense, so only its anti-pattern catalog was extracted.

## When these trigger

Any time I build or review something visual: HTML artifacts, dashboards, landing pages/sales assets (`sales:create-an-asset`), the budget-dashboard skill's output, or anything client-facing that has a UI. They stack — e.g. `design-taste-frontend` for overall layout/typography/color discipline, `emil-design-eng`/`apple-design` for any animation, `impeccable-anti-slop-catalog` as a final pass to catch AI-tell defaults before shipping.

## Found but not applicable to Cowork

**pixel-agents** — github.com/pixel-agents-hq/pixel-agents. Not a skill or reference doc — it's a real software app (VS Code extension + standalone `npx pixel-agents` CLI) that renders running **Claude Code CLI** terminal sessions as animated pixel-art characters in a virtual office (walks to desk, types while editing, flags when waiting for input). Requires the Claude Code CLI installed locally, runs its own local server, and installs hooks into `~/.claude/settings.json`.

Doesn't apply here — it watches terminal/VS Code Claude Code sessions, a different product from Cowork, and there's nothing to install as a Cowork skill. Logged only in case Eikko ever runs Claude Code CLI directly outside Cowork and wants a visual multi-agent dashboard for it.
