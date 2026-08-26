"""Fold the leftover rating-ready local leads (not yet in the Instantly-draft-derived
PlusVibe campaign) into that same campaign. No new campaign, no mailbox change.
"""
import json, os, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
CID = os.environ["PV_CAMPAIGN_ID"]

LEFTOVER_PATH = os.path.join(os.path.dirname(__file__), "leftover_rating_leads.json")


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


def leads():
    # Already normalized to a common schema (source files 1 and 2 use different
    # column names for the same fields — see the profile's cleaning notes).
    raw = json.load(open(LEFTOVER_PATH, encoding="utf-8"))
    out = []
    for r in raw:
        out.append({
            "email": r["email"],
            "first_name": r["first_name"],
            "last_name": r["last_name"],
            "company_name": r["company_name"],
            "company_website": r["company_website"],
            "linkedin_person_url": r["linkedin_person_url"],
            "linkedin_company_url": r["linkedin_company_url"],
            "phone_number": r["phone_number"],
            "country": r["country"],
            "custom_variables": {
                "rating": r["rating"],
                "amazon_url": r["amazon_url"],
                "job_title": r["job_title"],
                "industry": r["industry"],
                "employees": r["employees"],
                "review_count": r["review_count"],
            },
        })
    return out


def main():
    lead_rows = leads()
    print(f"leads to add: {len(lead_rows)}")
    assert all(l["custom_variables"]["rating"] for l in lead_rows), "a lead is missing rating"
    assert len({l["email"] for l in lead_rows}) == len(lead_rows), "duplicate emails in source"

    added = call("POST", "lead/add", {
        "workspace_id": WS,
        "campaign_id": CID,
        "leads": lead_rows,
        "skip_if_in_workspace": True,
    })
    print("result:", json.dumps(added, indent=2))


if __name__ == "__main__":
    main()
