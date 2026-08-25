#!/usr/bin/env python3
"""
build-artifact.py — generate the shareable/hosted Command Center from the
local one.

Run scan.py first, then this. It produces command-center-hosted.html:
a single self-contained file with the data inlined, safe to publish as an
Artifact or open on a phone.

Two deliberate differences from the local dashboard:

  1. REDACTION. Per .claude-dashboard/README.md, the hosted variant omits
     per-client rates/pay type and the task text. Those are the fields that
     would leak one client's commercial terms to another if the link is ever
     shared. Counts survive; the sensitive strings do not.

  2. TYPOGRAPHY. The hosted page loads its own faces (IBM Plex Sans/Mono for
     the operational body and figures, Archivo for display). The local file
     stays on system-ui so it renders instantly with no network.

The data-viz palette is NOT changed — it was validated against these exact
surfaces, and re-tinting them would invalidate the contrast results.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "command-center.html"
DATA = HERE / "dashboard-data.json"
LIVE = HERE / "campaigns-data.json"   # optional; absent until a sync has run
OUT = HERE / "command-center-hosted.html"

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    "family=Archivo:wght@500;600;700&"
    "family=IBM+Plex+Sans:wght@400;500;600&"
    "family=IBM+Plex+Mono:wght@400;500&display=swap\">\n"
)

# Only the two type tokens change; every colour token is inherited untouched.
TYPE_OVERRIDE = """
<style>
  /* Hosted-only type identity. Colour tokens are inherited from the local
     dashboard unchanged — they were validated against those surfaces. */
  :root {
    --sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
    --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    --display: "Archivo", var(--sans);
  }
  .page-title, .stat-val, .brand-name { font-family: var(--display); }
  .stat-val { letter-spacing: -.04em; font-weight: 700; }
  .page-title { font-weight: 600; }
  th, .col-head, .nav-label { font-family: var(--sans); }
</style>
"""

BANNER = """
<div class="note" style="margin:0 0 14px;display:flex;gap:9px;align-items:flex-start">
  <span aria-hidden="true">◔</span>
  <span><strong>Snapshot.</strong> Generated {stamp} from the local system —
  it does not update on its own. Re-run <code>scan.py</code> then
  <code>build-artifact.py</code> to refresh it. Rates and task detail are
  omitted from this hosted copy; open the local dashboard for those.</span>
</div>
"""


def redact(data: dict) -> dict:
    """Strip the fields that would leak commercial terms or work detail."""
    for c in data.get("clients", []):
        f = c.get("financial") or {}
        c["financial"] = {
            # Keep the shape the UI expects; drop the values.
            "rate": "hidden on the hosted copy",
            "payType": f.get("payType") or "—",
            "lifetimeEarned": None,
            "lifetimeNote": "Rates and earnings are shown only in the local dashboard.",
        }
        # Keep the counts (the UI shows "N open"), drop the text.
        for t in c.get("tasks", []):
            t["text"] = "—"
    return data


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"missing {SRC.name} — nothing to build from")
    if not DATA.exists():
        raise SystemExit(f"missing {DATA.name} — run scan.py first")

    html = SRC.read_text(encoding="utf-8")
    data = redact(json.loads(DATA.read_text(encoding="utf-8")))

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Guard the inline <script>: a literal </script> or a U+2028/9 inside the
    # JSON would otherwise terminate or break the block.
    payload = (payload.replace("</", "<\\/")
                      .replace(" ", "\\u2028")
                      .replace(" ", "\\u2029"))

    # The live-platform bundle rides along so the hosted copy shows the same
    # merged picture. It carries no rates or task text, so it needs no redaction.
    live_js = ""
    if LIVE.exists():
        live = json.loads(LIVE.read_text(encoding="utf-8"))
        lp = json.dumps(live, ensure_ascii=False, separators=(",", ":"))
        lp = (lp.replace("</", "<\\/")
                .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
        live_js = f"window.__CAMPAIGNS_DATA__ = {lp};"

    # 1. Swap the cache-busting loader for the inlined data.
    html = re.sub(
        r"<script>\n/\* Cache-bust.*?</script>",
        f"<script>window.__DASHBOARD_DATA__ = {payload};{live_js}</script>",
        html, count=1, flags=re.S,
    )
    if "__DASHBOARD_DATA__ =" not in html.split("<style>")[0]:
        raise SystemExit("data loader not found — did command-center.html change shape?")

    # 2a. Fonts in the head, before the stylesheet.
    html = html.replace("<title>Command Center</title>",
                        "<title>Client Command Center</title>\n" + FONTS, 1)
    # 2b. Type identity AFTER the main stylesheet — the local :root also
    #     defines --sans/--mono, so an earlier override would simply lose.
    html = html.replace('<div class="shell">', TYPE_OVERRIDE + '\n<div class="shell">', 1)

    # 3. Snapshot banner at the top of every view.
    stamp = (data.get("generatedAt", "") or "")[:16].replace("T", " ") + " UTC"
    html = html.replace(
        "  $('#views').replaceChildren(RENDER[current]());",
        "  const v = RENDER[current]();\n"
        "  v.insertAdjacentHTML('afterbegin', BANNER_HTML);\n"
        "  $('#views').replaceChildren(v);", 1)
    html = html.replace('const D = window.__DASHBOARD_DATA__ || {};',
                        'const D = window.__DASHBOARD_DATA__ || {};\n'
                        f'const BANNER_HTML = {json.dumps(BANNER.format(stamp=stamp))};', 1)

    OUT.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print(f"wrote {OUT.name} ({kb:.0f} KB, self-contained) "
          f"— {len(data.get('clients', []))} clients, "
          f"{sum(len(c['campaigns']) for c in data.get('campaigns', []))} documented campaigns, "
          f"live bundle {'inlined' if LIVE.exists() else 'ABSENT'}, "
          f"rates and task text redacted")


if __name__ == "__main__":
    main()
