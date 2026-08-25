#!/usr/bin/env bash
#
# setup-cloud-env.sh — provision the CMS cloud environment.
#
# Runs once, after the repo is cloned, from the repo root. Idempotent:
# safe to re-run on every environment rebuild.
#
# This repo is primarily a markdown knowledge base (client profiles, meeting
# notes, campaign tracking). The Node backend in backend/ is a secondary
# dashboard, so its install is best-effort: a failure there warns loudly but
# does not fail the environment, because the document work does not need it.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

grn() { printf '\033[32m✓ %s\033[0m\n' "$*"; }
ylw() { printf '\033[33m! %s\033[0m\n' "$*"; }
red() { printf '\033[31m✗ %s\033[0m\n' "$*"; }
hdr() { printf '\n\033[1m── %s ──\033[0m\n' "$*"; }

hdr "CMS environment setup"
echo "repo root: $REPO_ROOT"

# ── 1. toolchain ──────────────────────────────────────────────────
hdr "Toolchain"
command -v git  >/dev/null || { red "git not found"; exit 1; }
grn "git      $(git --version | awk '{print $3}')"

if command -v node >/dev/null; then
  NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]')"
  if [[ "$NODE_MAJOR" -ge 18 ]]; then grn "node     $(node -v)"
  else ylw "node $(node -v) is below the >=18 required by backend/package.json"; fi
else
  ylw "node not found — backend/ dashboard will be unavailable"
fi

if command -v python3 >/dev/null; then
  grn "python3  $(python3 -V 2>&1 | awk '{print $2}')  (.claude-dashboard/scan.py is stdlib-only, no pip installs needed)"
else
  ylw "python3 not found — .claude-dashboard/scan.py will not run"
fi

command -v curl >/dev/null && grn "curl     present (needed by the sync script's visibility guard)" \
                           || ylw "curl not found — sync script cannot verify repo visibility"

# ── 2. git identity + safe.directory ──────────────────────────────
hdr "Git config"
git config --global --add safe.directory "$REPO_ROOT" 2>/dev/null || true
# Identity comes from GIT_AUTHOR_*/GIT_COMMITTER_* env vars. Mirror them into
# git config so tools that ignore the environment still attribute correctly.
if [[ -n "${GIT_AUTHOR_NAME:-}" ]]; then
  git config --global user.name  "$GIT_AUTHOR_NAME"
  git config --global user.email "${GIT_AUTHOR_EMAIL:-}"
  grn "identity $(git config --global user.name) <$(git config --global user.email)>"
else
  ylw "GIT_AUTHOR_NAME unset — commits from this environment will have no author"
fi

# ── 3. root .env for scripts/sync-to-github.sh ────────────────────
# .env is gitignored, so a fresh clone never has one. Generate it, adapting
# the guards for a non-interactive environment.
hdr "Sync config (.env)"
if [[ -f .env ]]; then
  grn ".env already present — left untouched"
elif [[ -f .env.example ]]; then
  cp .env.example .env
  # No TTY here, so the y/N prompt in the sync script would hang.
  sed -i.bak 's/^CONFIRM_BEFORE_PUSH=.*/CONFIRM_BEFORE_PUSH=false/' .env && rm -f .env.bak
  grn ".env created from .env.example (CONFIRM_BEFORE_PUSH=false — no TTY here)"
  grn "guards: REQUIRE_PRIVATE_REPO and SCAN_FOR_SECRETS left ON"
else
  ylw ".env.example missing — skipping"
fi

# ── 4. backend/.env with the correct checkout path ────────────────
# backend/.env.example hardcodes a macOS path. Resolve it at setup time so it
# points at wherever this environment actually cloned the repo.
hdr "Backend config (backend/.env)"
if [[ -f backend/.env.example ]]; then
  if [[ -f backend/.env ]]; then
    grn "backend/.env already present — left untouched"
  else
    sed "s|^COWORK_DIR=.*|COWORK_DIR=$REPO_ROOT|" backend/.env.example > backend/.env
    [[ -n "${PORT:-}" ]] && sed -i.bak "s|^PORT=.*|PORT=$PORT|" backend/.env && rm -f backend/.env.bak
    grn "backend/.env created, COWORK_DIR=$REPO_ROOT"
  fi
else
  ylw "backend/.env.example missing — skipping"
fi

# ── 5. backend dependencies (best-effort) ─────────────────────────
hdr "Backend dependencies"
if [[ -f backend/package.json ]] && command -v node >/dev/null && command -v npm >/dev/null; then
  # sqlite3 needs a prebuilt binary or node-gyp (python3 + make + a C++
  # toolchain). Non-fatal: the markdown work does not depend on it.
  if (cd backend && npm install --no-audit --no-fund 2>&1 | tail -5); then
    grn "npm install completed"
  else
    ylw "npm install FAILED — the backend dashboard will not start."
    ylw "Most likely sqlite3 could not build. Retry manually with:"
    ylw "    cd backend && npm install --build-from-source"
    ylw "Everything else in this environment still works."
  fi
else
  ylw "skipping npm install (no backend/package.json, or node/npm unavailable)"
fi

# ── 6. executables ────────────────────────────────────────────────
hdr "Permissions"
chmod +x scripts/*.sh 2>/dev/null || true
grn "scripts/*.sh marked executable"

# ── 7. safety assertion ───────────────────────────────────────────
# These are gitignored and must never appear in a clone. If one shows up, the
# ignore rules regressed and this environment is holding credentials.
hdr "Safety check"
LEAKED=0
while IFS= read -r p; do
  [[ -e "$p" ]] && { red "SENSITIVE FILE PRESENT IN CLONE: $p"; LEAKED=1; }
done <<'PATHS'
RESOURCES/Tools & API Details/Albertscott Domains and Emails/Premium Inboxes.csv
RESOURCES/Tools & API Details/tools_api_details.md
ARCHIVE - Inactive Automations/smartlead-pipedrive-automation/.env
PATHS
if [[ "$LEAKED" -eq 1 ]]; then
  red "A gitignored credential file made it into this checkout — investigate before using this environment."
  exit 1
fi
grn "no credential files in the checkout"

hdr "Ready"
cat <<EOF
  Backend dashboard   cd backend && npm start        (http://localhost:${PORT:-3001})
  Dashboard scan      python3 .claude-dashboard/scan.py
  Sync to GitHub      ./scripts/sync-to-github.sh
  Dry run / scan only ./scripts/sync-to-github.sh --dry-run | --scan-only
EOF
