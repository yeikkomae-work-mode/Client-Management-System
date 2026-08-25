#!/usr/bin/env python3
"""Scans the Client-Management-System and writes dashboard-data.json / .js
for the Central Command dashboard. Run manually or via the scheduled
launchd job (com.eikko.centralcommand.scan).

Never fabricates figures it can't ground in a real file — if a value isn't
actually recorded anywhere (e.g. lifetime earnings, no monthly report on
file yet), it's reported as untracked rather than estimated."""

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = ROOT / ".claude-dashboard"
OUTPUT_FILE = DASHBOARD_DIR / "dashboard-data.json"
OUTPUT_JS_FILE = DASHBOARD_DIR / "dashboard-data.js"

EXCLUDE_NAMES = {".DS_Store", "Important info.md"}

ME = {
    "name": "Eikko Ybanez",
    "role": "Solo VA / Agency Operator",
    "bio": "Cold email infrastructure, lead gen, campaign management, CRM "
           "hygiene, and general VA ops across every client account.",
    "tools": ["Apollo", "PlusVibe", "Smartlead", "Instantly", "Pipedrive",
              "HubSpot", "Gmail (5 accounts)", "Notion", "Fathom"],
}


def iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip().strip('"')
    return fm


MONTH_FORMATS = ["%B %d, %Y", "%b %d, %Y", "%B %Y", "%b %Y", "%Y-%m-%d"]


def parse_human_date(text: str):
    """Best-effort parse of dates like 'Aug 12, 2026' or 'February 2026'.
    Returns a datetime or None — never guesses if the text doesn't match."""
    if not text:
        return None
    cleaned = text.strip().strip(".,")
    cleaned = re.sub(r"\s+", " ", cleaned)
    for fmt in MONTH_FORMATS:
        try:
            return datetime.strptime(cleaned, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def extract_field(text: str, label: str) -> str:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*([^\|\n]+)", text, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def guess_pay_type(rate: str) -> str:
    r = rate.lower()
    if "free" in r or r.strip() in ("$0", "0"):
        return "Free"
    if "/hr" in r or "hour" in r:
        return "Hourly"
    if "/mo" in r or "month" in r or "retainer" in r:
        return "Retainer"
    if not r or "tbd" in r:
        return "Unknown"
    return "Other"


def scan_activity(days: int = 7) -> dict:
    """Real count of EOD log entries per day across all clients — never
    estimated, just tallied from '## YYYY-MM-DD' headers in every End-of-Day
    log. Returns the last `days` as a list (for the bar chart) plus the full
    by-date map (for the calendar, which may span further back)."""
    eod_dir = ROOT / "OUTPUT" / "End-of-Day Reports"
    counts = {}
    if eod_dir.exists():
        for f in eod_dir.glob("*.md"):
            for d in re.findall(r"^## (\d{4}-\d{2}-\d{2})", f.read_text(encoding="utf-8"), re.MULTILINE):
                counts[d] = counts.get(d, 0) + 1

    today = datetime.now(timezone.utc).date()
    week = []
    for offset in range(days - 1, -1, -1):
        d = today - timedelta(days=offset)
        key = d.isoformat()
        week.append({"date": key, "count": counts.get(key, 0)})
    return {"week": week, "byDate": counts}


HISTORY_FILE = DASHBOARD_DIR / "history.json"


def update_history(snapshot: dict) -> list:
    """Appends today's KPI snapshot to a rolling history file so KPI tiles
    can show a real week-over-week delta instead of a fabricated one. Only
    ever reads/writes counts this scan itself produced — nothing invented."""
    today = datetime.now(timezone.utc).date().isoformat()
    history = []
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            history = []

    history = [h for h in history if h.get("date") != today]
    history.append({"date": today, **snapshot})
    history.sort(key=lambda h: h["date"])
    history = history[-60:]

    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return history


def find_eod_earliest_date(client_key: str) -> str:
    """client_key: a lowercase first-name-ish token to fuzzy-match an EOD log."""
    eod_dir = ROOT / "OUTPUT" / "End-of-Day Reports"
    if not eod_dir.exists():
        return ""
    for f in eod_dir.glob("*.md"):
        if client_key in f.stem.lower():
            dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", f.read_text(encoding="utf-8"), re.MULTILINE)
            if dates:
                return min(dates)
    return ""


def find_eod_latest_date(client_key: str) -> str:
    """Same matching as find_eod_earliest_date, but the most recent entry —
    powers 'days since last log' on the Client Health widget. Never guessed:
    empty string if no EOD log matches this client at all."""
    eod_dir = ROOT / "OUTPUT" / "End-of-Day Reports"
    if not eod_dir.exists():
        return ""
    for f in eod_dir.glob("*.md"):
        if client_key in f.stem.lower():
            dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", f.read_text(encoding="utf-8"), re.MULTILINE)
            if dates:
                return max(dates)
    return ""


def clean_task_text(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 160:
        text = text[:157].rstrip() + "…"
    return text


def client_tokens(stem: str) -> list:
    """Unicode-safe word split (so 'Cüneyt' keeps its ü) — filenames only
    use spaces/hyphens/parens as separators, so split on those specifically
    rather than stripping anything non-ASCII."""
    words = re.split(r"[\s\-()]+", stem.lower())
    stop = {"profile", "the", "and"}
    return [w.strip(".,") for w in words if len(w.strip(".,")) >= 3 and w.strip(".,") not in stop]


def scan_tasks_for_client(tokens: list) -> list:
    """Finds PROJECTS/** files that name-match this client (by filename or
    first heading, whole-word) and pulls their top-level checkbox lines into
    a simple To Do / Done task board. Skips files with no checkboxes (design
    docs, notes) rather than inventing task cards for them."""
    projects_dir = ROOT / "PROJECTS"
    if not projects_dir.exists() or not tokens:
        return []
    pattern = re.compile(r"\b(" + "|".join(re.escape(t) for t in tokens) + r")\b", re.IGNORECASE)

    tasks = []
    for f in sorted(projects_dir.rglob("*.md")):
        if f.name.startswith("."):
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        first_heading_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        first_heading = first_heading_match.group(1) if first_heading_match else ""
        searchable = f.stem + " " + first_heading
        if not pattern.search(searchable):
            continue

        bucket = f.parent.name
        checkbox_lines = re.findall(r"^- \[( |x|X)\]\s*(.+)$", text, re.MULTILINE)
        for mark, raw_text in checkbox_lines:
            tasks.append({
                "status": "done" if mark.lower() == "x" else "todo",
                "text": clean_task_text(raw_text),
                "sourceFile": f.name,
                "bucket": bucket,
            })
    return tasks


def scan_client(f: Path, match_tokens: list) -> dict:
    text = f.read_text(encoding="utf-8")
    stat = f.stat()

    status = extract_field(text, "Status")
    rate = extract_field(text, "Rate")
    hours = extract_field(text, "Hours")
    role = extract_field(text, "Role")
    coverage = extract_field(text, "Coverage Period")
    start_field = extract_field(text, "Start date") or extract_field(text, "Start Date")
    meeting_match = re.search(r"\*\*Regular meeting:\*\*\s*([^\n]+)", text, re.IGNORECASE)
    meeting = meeting_match.group(1).strip() if meeting_match else ""

    since_label, since_source, since_dt = "", "unknown", None
    if coverage:
        start_part = re.split(r"[–\-]", coverage)[0].strip()
        parsed = parse_human_date(start_part)
        if parsed:
            since_label, since_source, since_dt = start_part, "coverage_period", parsed
    if not since_dt and start_field:
        parsed = parse_human_date(start_field)
        if parsed:
            since_label, since_source, since_dt = start_field, "start_date_field", parsed
    if not since_dt:
        status_date_match = re.search(r"\(([A-Za-z]+\s+\d{1,2},\s*\d{4})\)", status)
        if status_date_match:
            parsed = parse_human_date(status_date_match.group(1))
            if parsed:
                since_label = status_date_match.group(1)
                since_source = "status_date"
                since_dt = parsed
    if not since_dt:
        client_key = re.split(r"[\s\-(]", f.stem)[0].lower()
        earliest = find_eod_earliest_date(client_key)
        if earliest:
            parsed = parse_human_date(earliest)
            since_label, since_source, since_dt = earliest, "first_logged", parsed

    display_name = (
        f.stem.replace(" - Profile", "")
        .replace(" - Profile (", " (")
    )

    tasks = scan_tasks_for_client(match_tokens)

    client_key = re.split(r"[\s\-(]", f.stem)[0].lower()
    last_eod = find_eod_latest_date(client_key)

    return {
        "name": display_name,
        "fileName": f.name,
        "absPath": str(f.resolve()),
        "relPath": str(f.relative_to(ROOT)),
        "modified": iso(stat.st_mtime),
        "status": status or "Unknown",
        "role": role or "Not documented yet",
        "hours": hours,
        "meeting": meeting,
        "tasks": tasks,
        "lastEOD": last_eod or None,
        "since": {
            "label": since_label or None,
            "source": since_source,
            "date": since_dt.isoformat() if since_dt else None,
        },
        "financial": {
            "rate": rate or "Not documented yet",
            "payType": guess_pay_type(rate),
            "lifetimeEarned": None,
            "lifetimeNote": "Not yet tracked — no completed monthly income "
                             "report on file for this client.",
        },
    }


def scan_clients() -> list:
    clients_dir = ROOT / "CLIENT PROFILES"
    out = []
    if not clients_dir.exists():
        return out

    files = []
    for f in sorted(clients_dir.glob("*.md")):
        if f.name in EXCLUDE_NAMES or f.name.startswith("."):
            continue
        if "quick reference" in f.stem.lower():
            continue  # reference doc, not a distinct client profile
        files.append(f)

    # Some clients share a first name (three "Chris"es) — a shared token like
    # "chris" would match every one of their task files to every Chris. Drop
    # tokens that aren't unique to a single client before matching task files.
    all_tokens = {f: client_tokens(f.stem) for f in files}
    token_freq = {}
    for toks in all_tokens.values():
        for t in set(toks):
            token_freq[t] = token_freq.get(t, 0) + 1

    for f in files:
        toks = all_tokens[f]
        unique = [t for t in toks if token_freq.get(t, 0) == 1]
        out.append(scan_client(f, unique or toks))
    return out


# Grounded in CLAUDE.md's own Front-office/Back-office grouping — not a guess.
AGENT_CATEGORY = {
    "lead-prospector": "Front-office", "copywriter": "Front-office",
    "reply-handler": "Front-office", "market-scout": "Front-office",
    "inbox-triage": "Back-office", "project-manager": "Back-office",
    "billing-auditor": "Back-office", "file-organizer": "Back-office",
    "onboarding-guide": "Back-office", "meeting-summarizer": "Back-office",
}


def scan_agents() -> list:
    agents_dir = ROOT / ".claude" / "agents"
    out = []
    if not agents_dir.exists():
        return out
    for f in sorted(agents_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        name = fm.get("name", f.stem)
        out.append({
            "name": name,
            "description": fm.get("description", ""),
            "tools": fm.get("tools", ""),
            "model": fm.get("model", ""),
            "category": AGENT_CATEGORY.get(name, "Specialized"),
            "relPath": str(f.relative_to(ROOT)),
        })
    return out


def scan_skills() -> list:
    out = []
    skills_dir = ROOT / "SKILLS"
    if skills_dir.exists():
        for f in sorted(skills_dir.iterdir()):
            if f.name.startswith("."):
                continue
            out.append({
                "name": f.stem, "description": "", "kind": "skill",
                "relPath": str(f.relative_to(ROOT)),
            })

    commands_dir = ROOT / ".claude" / "commands"
    if commands_dir.exists():
        for f in sorted(commands_dir.glob("*.md")):
            fm = parse_frontmatter(f.read_text(encoding="utf-8"))
            out.append({
                "name": f"/{f.stem}",
                "description": fm.get("description", ""),
                "kind": "command",
                "relPath": str(f.relative_to(ROOT)),
            })
    return out


def scan_pipeline() -> dict:
    projects_dir = ROOT / "PROJECTS"
    buckets = ["Active", "In-Progress", "Pending", "Done", "Failed", "Prospective"]
    out = {}
    for bucket in buckets:
        bucket_dir = projects_dir / bucket
        items = []
        if bucket_dir.exists():
            for f in sorted(bucket_dir.iterdir()):
                if f.name in EXCLUDE_NAMES or f.name.startswith("."):
                    continue
                stat = f.stat()
                items.append({
                    "name": f.stem if f.is_file() else f.name,
                    "modified": iso(stat.st_mtime),
                    "relPath": str(f.relative_to(ROOT)),
                    "isDir": f.is_dir(),
                })
        out[bucket] = items
    return out


def main():
    DASHBOARD_DIR.mkdir(exist_ok=True)

    clients = scan_clients()
    agents = scan_agents()
    skills = scan_skills()
    pipeline = scan_pipeline()
    activity = scan_activity()

    snapshot = {
        "clients": len(clients),
        "activeClients": sum(1 for c in clients if "active" in c["status"].lower()),
        "agents": len(agents),
        "activeTasks": len(pipeline.get("Active", [])),
    }
    history = update_history(snapshot)

    data = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "systemRoot": str(ROOT),
        "me": {**ME, "clientCount": len(clients)},
        "clients": clients,
        "agents": agents,
        "skills": skills,
        "pipeline": pipeline,
        "activity": activity,
        "history": history,
    }
    payload = json.dumps(data, indent=2)
    OUTPUT_FILE.write_text(payload, encoding="utf-8")

    js_safe_payload = payload.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    OUTPUT_JS_FILE.write_text(f"window.__DASHBOARD_DATA__ = {js_safe_payload};\n", encoding="utf-8")

    print(f"[{data['generatedAt']}] wrote {OUTPUT_FILE.name} + {OUTPUT_JS_FILE.name} "
          f"({len(data['clients'])} clients, {len(data['agents'])} agents, "
          f"{len(data['skills'])} skills)")


if __name__ == "__main__":
    main()
