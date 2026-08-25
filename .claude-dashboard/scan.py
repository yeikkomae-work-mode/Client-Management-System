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


# ── Campaigns ────────────────────────────────────────────────────────
# Parses OUTPUT/Campaign Tracking/*.md. Two things are extracted:
#   1. Header fields (**Client:**, **Tool:**, **Status:**, **Launched:**)
#   2. Per-campaign metric tables, when a table clearly is one.
# A file with no parseable table gets metrics=None rather than zeros —
# "documented but not measured" is a real state and the UI says so.

CAMPAIGN_DIR_NAME = "Campaign Tracking"

# Column header -> canonical metric key. Matched case-insensitively on the
# stripped, de-bolded header cell.
METRIC_COLUMNS = {
    "sent": "sent", "emails sent": "sent",
    "leads contacted": "leads", "total leads": "leads", "leads": "leads",
    "replies": "replies", "replies (unique)": "replies", "unique replies": "replies",
    "opens": "opens", "clicks": "clicks",
    "bounces": "bounces", "bounced": "bounces",
    "opportunities": "opportunities", "opps": "opportunities",
    "completed leads": "completed",
}

STATUS_TONES = [
    ("\U0001F7E2", "good"),    # 🟢
    ("\u2705", "good"),        # ✅
    ("\U0001F7E1", "warn"),    # 🟡
    ("\U0001F534", "bad"),     # 🔴
]


def _cell(text: str) -> str:
    """Strip markdown emphasis and whitespace from one table cell."""
    return re.sub(r"[*`]", "", text).strip()


def _num(text: str):
    """'1,699' -> 1699. Returns None when the cell isn't a plain number,
    so a '—' or 'N/A' never silently becomes 0."""
    t = _cell(text).replace(",", "")
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    return None


def _status_tone(status: str) -> str:
    for glyph, tone in STATUS_TONES:
        if glyph in status:
            return tone
    return "neutral"


def parse_metric_table(lines: list, start: int):
    """Given the index of a table header row, return (rows, total, consumed).
    Returns (None, None, 0) if this table isn't a per-campaign metric table."""
    header_cells = [_cell(c).lower() for c in lines[start].strip().strip("|").split("|")]
    # Needs a name column plus at least one recognised metric column.
    if not header_cells or "campaign" not in header_cells[0]:
        return None, None, 0
    mapped = {i: METRIC_COLUMNS[h] for i, h in enumerate(header_cells) if h in METRIC_COLUMNS}
    if not mapped:
        return None, None, 0

    status_idx = next((i for i, h in enumerate(header_cells) if h == "status"), None)
    rows, total, i = [], None, start + 1
    if i < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i].strip()):
        i += 1  # separator row

    while i < len(lines) and lines[i].lstrip().startswith("|"):
        cells = lines[i].strip().strip("|").split("|")
        name = _cell(cells[0]) if cells else ""
        if not name or set(name) <= set("-: "):
            i += 1
            continue
        rec = {"name": name}
        for idx, key in mapped.items():
            if idx < len(cells):
                v = _num(cells[idx])
                if v is not None:
                    rec[key] = v
        if status_idx is not None and status_idx < len(cells):
            rec["status"] = _cell(cells[status_idx])
        # A bolded "Combined total" / "Totals" row is the file's own sum.
        if re.search(r"\b(combined\s+)?totals?\b", name, re.IGNORECASE):
            total = rec
        elif len(rec) > 1:
            rows.append(rec)
        i += 1

    return (rows or None), total, i - start


# Field-style tables ( | **Total Leads** | 40 | ) describe ONE campaign per
# file — Krishna's Apollo campaign logs use this shape. Only consulted when
# no per-campaign table was found, so it never overrides richer data.
FIELD_METRICS = {
    "total leads": "leads", "leads": "leads",
    "emails sent": "sent", "sent": "sent",
    "replies": "replies", "opens": "opens",
    "bounces": "bounces", "opportunities": "opportunities",
}


def parse_field_table_campaign(text: str, fallback_name: str):
    """Return a single-campaign record from | **Field** | value | rows,
    or None when the file carries no recognised metric field."""
    rec, found = {}, False
    for label, key in FIELD_METRICS.items():
        m = re.search(rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|\s*([^|\n]+)\|",
                      text, re.IGNORECASE)
        if m:
            v = _num(m.group(1))
            if v is not None:
                rec[key] = v
                found = True
    if not found:
        return None
    m = re.search(r"\|\s*\*\*Campaign Name\*\*\s*\|\s*([^|\n]+)\|", text, re.IGNORECASE)
    rec["name"] = _cell(m.group(1)) if m else fallback_name
    m = re.search(r"\|\s*\*\*Status\*\*\s*\|\s*([^|\n]+)\|", text, re.IGNORECASE)
    if m:
        rec["status"] = _cell(m.group(1))
    return rec


def match_known_client(text: str, filename: str, roster: list) -> str:
    """Attribute a campaign file to a real client from CLIENT PROFILES.
    Matches the declared **Client:** value, then the filename, then the body —
    always against the roster, so it can only ever return a real client name."""
    head = text[:1500]
    for c in roster:
        # First token of the profile name ("Cüneyt", "Chris Caffera" -> "Chris")
        full = c["name"]
        base = re.split(r"\s*\(", full)[0].strip()
        needles = {full, base}
        # Distinguish the two Chrises by their bracketed qualifier.
        for n in sorted(needles, key=len, reverse=True):
            if len(n) < 4:
                continue
            if re.search(rf"\b{re.escape(n)}\b", filename, re.IGNORECASE) or \
               re.search(rf"\b{re.escape(n)}\b", head, re.IGNORECASE):
                return full
    return ""


def scan_campaigns(roster=None) -> list:
    roster = roster or []
    camp_dir = ROOT / "OUTPUT" / CAMPAIGN_DIR_NAME
    out = []
    if not camp_dir.is_dir():
        return out

    for f in sorted(camp_dir.rglob("*.md")):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = text.splitlines()

        h1 = next((l.lstrip("# ").strip() for l in lines if l.startswith("# ")), f.stem)
        client = extract_field(text, "Client")
        tool = extract_field(text, "Tool") or extract_field(text, "Platform")
        status = extract_field(text, "Status")
        launched = (extract_field(text, "Launched")
                    or extract_field(text, "Launch Date")
                    or extract_field(text, "Report date"))

        # Field-style tables ( | **Client** | value | ) as a fallback.
        def field_row(label):
            m = re.search(rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|\s*([^|\n]+)\|", text, re.IGNORECASE)
            return m.group(1).strip() if m else ""
        client = client or field_row("Client")
        client = client or match_known_client(text, f.name, roster)
        tool = tool or field_row("Tool")
        status = status or field_row("Status")
        launched = launched or field_row("Launch Date")

        rows, total = None, None
        i = 0
        while i < len(lines):
            if lines[i].lstrip().startswith("|"):
                r, t, consumed = parse_metric_table(lines, i)
                if r or t:
                    rows, total = r, t
                    i += max(consumed, 1)
                    continue
            i += 1

        if not rows and not total:
            single = parse_field_table_campaign(text, h1)
            if single:
                rows = [single]

        metrics = None
        if rows or total:
            keys = ("sent", "leads", "replies", "opens", "clicks", "bounces",
                    "opportunities", "completed")
            if total:
                metrics = {k: total[k] for k in keys if k in total}
            else:
                metrics = {}
                for k in keys:
                    vals = [r[k] for r in (rows or []) if k in r]
                    if vals:
                        metrics[k] = sum(vals)
            if metrics.get("sent"):
                metrics["replyRate"] = round(
                    100 * metrics.get("replies", 0) / metrics["sent"], 2)
                metrics["bounceRate"] = round(
                    100 * metrics.get("bounces", 0) / metrics["sent"], 2)

        canonical = match_known_client(text, f.name, roster)
        out.append({
            "title": h1,
            "clientCanonical": canonical or client,
            "fileName": f.name,
            "client": client,
            "tool": tool,
            "status": status,
            "statusTone": _status_tone(status),
            "launched": launched,
            "relPath": str(f.relative_to(ROOT)),
            "modified": iso(f.stat().st_mtime),
            "campaigns": rows or [],
            "metrics": metrics,
            "hasMetrics": bool(metrics),
        })

    return out


def campaign_totals(campaigns: list) -> dict:
    """Roll up every file that had parseable metrics. Files without metrics
    are counted separately so the UI can be honest about coverage."""
    keys = ("sent", "leads", "replies", "opens", "clicks", "bounces", "opportunities")
    totals = {k: 0 for k in keys}
    measured = 0
    for c in campaigns:
        if not c["hasMetrics"]:
            continue
        measured += 1
        for k in keys:
            totals[k] += c["metrics"].get(k, 0)
    if totals["sent"]:
        totals["replyRate"] = round(100 * totals["replies"] / totals["sent"], 2)
        totals["bounceRate"] = round(100 * totals["bounces"] / totals["sent"], 2)
    totals["filesMeasured"] = measured
    totals["filesTotal"] = len(campaigns)
    totals["campaignCount"] = sum(len(c["campaigns"]) for c in campaigns)
    return totals


def main():
    DASHBOARD_DIR.mkdir(exist_ok=True)

    clients = scan_clients()
    agents = scan_agents()
    skills = scan_skills()
    pipeline = scan_pipeline()
    activity = scan_activity()
    campaigns = scan_campaigns(clients)

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
        "campaigns": campaigns,
        "campaignTotals": campaign_totals(campaigns),
        "history": history,
    }
    payload = json.dumps(data, indent=2)
    OUTPUT_FILE.write_text(payload, encoding="utf-8")

    js_safe_payload = payload.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    OUTPUT_JS_FILE.write_text(f"window.__DASHBOARD_DATA__ = {js_safe_payload};\n", encoding="utf-8")

    print(f"[{data['generatedAt']}] wrote {OUTPUT_FILE.name} + {OUTPUT_JS_FILE.name} "
          f"({len(data['clients'])} clients, {len(data['agents'])} agents, "
          f"{len(data['skills'])} skills, "
          f"{data['campaignTotals']['filesMeasured']}/{len(campaigns)} campaign files measured)")


if __name__ == "__main__":
    main()
