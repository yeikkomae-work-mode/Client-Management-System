"""Apply one day's +1 ramp increment to the 12 UK/US x Google/Microsoft/Other
legs launched 2026-08-28 at daily_limit=6. No PlusVibe read endpoint exposes
the current schedule, so this relies on the known prior value (tracked here)
rather than reading it back. Run once per day, by hand, per the classifier's
restriction on unsupervised writes to live campaigns.
"""
import json, os, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]

# (campaign_id, name, timezone, start_date used at creation)
CAMPAIGNS = [
    ("6a8cf6f27e5c6119d8830749", "Amazon Seller US/CA - Google [MIGRATED]", "America/New_York"),
    ("6a90cd6f2dbb802b3e05cc6b", "Amazon Seller US/CA - Microsoft [MIGRATED]", "America/New_York"),
    ("6a90cd70fdaf9c49f3b0ca64", "Amazon Seller US/CA - Other [MIGRATED]", "America/New_York"),
    ("6a90b3bcf68baa1111ed5c7f", "Amazon Seller UK - Google [MIGRATED]", "Europe/London"),
    ("6a90cd72b8f24dca09ef6bb8", "Amazon Seller UK - Microsoft [MIGRATED]", "Europe/London"),
    ("6a90cd742dbb802b3e05cc6c", "Amazon Seller UK - Other [MIGRATED]", "Europe/London"),
    ("6a8ee087c3903d2a71741b72", "Amazon Seller - Rating US - Google [MIGRATED FROM INSTANTLY DRAFT]", "America/New_York"),
    ("6a90cd764fdc64a002d2ca4a", "Amazon Seller - Rating US - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", "America/New_York"),
    ("6a90cd772dbb802b3e05cc6d", "Amazon Seller - Rating US - Other [MIGRATED FROM INSTANTLY DRAFT]", "America/New_York"),
    ("6a90b41d24acfefeb9390a4c", "Amazon Seller - Rating UK - Google [MIGRATED FROM INSTANTLY DRAFT]", "Europe/London"),
    ("6a90cd790d0bcf449012a962", "Amazon Seller - Rating UK - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", "Europe/London"),
    ("6a90cd7b5dddc42c583f1012", "Amazon Seller - Rating UK - Other [MIGRATED FROM INSTANTLY DRAFT]", "Europe/London"),
]

START_DATE = "2026-08-28"
CAP = 30


def call(method, path, body=None):
    cmd = ["curl", "-sS", "-X", method, f"{API}/{path}",
           "-H", f"x-api-key: {KEY}", "-H", "Content-Type: application/json",
           "-w", "\n%{http_code}"]
    if body is not None:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(body, tmp); tmp.close()
        cmd += ["-d", f"@{tmp.name}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    payload, _, code = out.rpartition("\n")
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} on {method} {path}\n{payload}")
    return json.loads(payload or "{}")


def main():
    current = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    new_limit = min(current + 1, CAP)
    print(f"ramping {current} -> {new_limit} (cap {CAP})")
    for cid, name, tz in CAMPAIGNS:
        call("PATCH", "campaign/update/campaign", {
            "workspace_id": WS,
            "campaign_id": cid,
            "schedules": [{
                "daily_limit": new_limit,
                "daily_limit_new_lead": new_limit,
                "start_date": START_DATE,
                "end_date": "",
                "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
                "timezone": tz,
                "timing": {"from": "09:00", "to": "17:00"},
            }],
        })
        print(f"  {name} ({cid}): daily_limit -> {new_limit}")
    print(f"\nDone. {len(CAMPAIGNS)} campaigns now at {new_limit}/day.")


if __name__ == "__main__":
    main()
