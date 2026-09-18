"""Build the 8 remaining PlusVibe campaigns from the audited Instantly account:
review-removal pitch variants (with Starfix -> SellerVate correction where the
original copy used the wrong brand) + the new Amazon Ops Support offer.

Excluded from this round (per Eikko's decision, 2026-08-27):
- SalesFix-signed group (1,164 raw / 822 verified leads) -- pending Cuneyt's
  answer on whether SalesFix is a real brand or a mistake.
- "Upwork Leads" (0 leads, different SEO-audit offer) -- out of scope.
- "Starfix New UK Leads 2026-08" -- all 45 leads already covered by earlier
  PlusVibe campaigns, 0 remain after dedupe.

All campaigns created PAUSED, sharing the existing 19 SellerVate mailboxes
(per Eikko's explicit decision to share rather than wait for more capacity).
"""
import json, os, re, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]

VAR_MAP = {
    "firstName": "first_name",
    "lastName": "last_name",
    "companyName": "company_name",
    "website": "custom_website",
    "accountSignature": "sender_signature",
    "jobTitle": "custom_job_title",
    "linkedIn": "custom_linkedin",
    "location": "custom_location",
    "phone": "custom_phone",
    "personalization": "custom_personalization",
}

BRAND_FIXES = [
    (r"Starfix Team", "SellerVate Team"),
    (r"at Starfix", "at SellerVate"),
    (r"using Starfix", "using SellerVate"),
    (r"Starfix helps", "SellerVate helps"),
    (r"starfix\.ai", "sellervate.de"),
    (r"^Starfix$", "SellerVate"),  # bare "Starfix" on its own line (e.g. signature)
]

GROUPS = [
    # (group_sig, plusvibe campaign name, needs_starfix_fix, mailboxes_placeholder)
    ("394d8f40d5", "Liste von Dennis + 50K DE Amazon Leads [MIGRATED]", False),
    ("71e456b7fc", "USA Seller [MIGRATED]", True),
    ("dd3876ca9b", "Amazon Seller 2cnd (2) [MIGRATED]", True),
    ("f2e166890e", "Sports & Fitness Reviews (SellerVate) [MIGRATED]", False),
    ("c8d8c16821", "UK Seller [MIGRATED]", True),
    ("d3e3b82506", "Amazon Ops Support [MIGRATED]", False),
    ("6dc14e9985", "Starfix New US Leads 2026-07-29 [MIGRATED]", True),
    ("bd898abf9d", "Review [MIGRATED]", False),
]

SCRATCH = os.path.dirname(__file__)


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


def convert_text(text, fix_brand):
    for old, new in VAR_MAP.items():
        text = re.sub(r"\{\{\s*%s\s*\}\}" % re.escape(old), "{{%s}}" % new, text)
    if fix_brand:
        for pat, repl in BRAND_FIXES:
            text = re.sub(pat, repl, text)
    return text


def convert_sequences(detail, fix_brand):
    seqs = detail.get("sequences") or [{}]
    steps = seqs[0].get("steps", [])
    out = []
    for i, s in enumerate(steps, 1):
        variants = []
        for vi, v in enumerate(s.get("variants", [])):
            variants.append({
                "variation": chr(65 + vi),
                "name": f"Step {i} variant {vi+1}",
                "subject": convert_text(v.get("subject", ""), fix_brand),
                "body": convert_text(v.get("body", ""), fix_brand),
            })
        wait = s.get("delay") or 1
        out.append({"step": i, "wait_time": max(wait, 1), "variations": variants})
    return out


def build_leads(raw_leads, verified_good):
    out = []
    for l in raw_leads:
        email = (l.get("email") or "").strip().lower()
        if email not in verified_good:
            continue
        p = l.get("payload", {}) or {}
        out.append({
            "email": email,
            "first_name": l.get("first_name", "") or p.get("firstName", ""),
            "last_name": l.get("last_name", "") or p.get("lastName", ""),
            "company_name": l.get("company_name", "") or p.get("companyName", ""),
            "company_website": l.get("website", "") or p.get("website", ""),
            "custom_variables": {
                "website": l.get("website", "") or p.get("website", ""),
                "job_title": l.get("job_title", "") or p.get("jobTitle", ""),
                "linkedin": p.get("linkedIn", ""),
                "location": p.get("location", ""),
            },
        })
    return out


def accounts():
    res = call("GET", f"account/list?workspace_id={WS}")
    return [a["id"] for a in res["accounts"] if a["status"] == "ACTIVE"]


def main():
    data = json.load(open(os.path.join(SCRATCH, "other24_full.json")))
    verified_good = set(json.load(open(os.path.join(SCRATCH, "verified_good_emails.json"))))
    all_mailboxes = accounts()
    print(f"sharing {len(all_mailboxes)} existing mailboxes across all new campaigns\n")

    # sig -> representative campaign name (first member) for pulling detail/leads
    import hashlib
    def sig(detail):
        seqs = detail.get("sequences") or [{}]
        steps = seqs[0].get("steps", [])
        bodies = []
        for s in steps:
            for v in s.get("variants", []):
                b = re.sub(r'<[^>]+>', '', v.get("body",""))
                b = re.sub(r'\s+', ' ', b).strip()
                bodies.append(b[:120])
        return hashlib.md5("|".join(bodies).encode()).hexdigest()[:10]

    sig_to_cnames = {}
    for cname, c in data.items():
        s = sig(c["detail"])
        sig_to_cnames.setdefault(s, []).append(cname)

    summary = []
    for group_sig, camp_name, fix_brand in GROUPS:
        members = sig_to_cnames[group_sig]
        detail = data[members[0]]["detail"]
        raw_leads = []
        for m in members:
            raw_leads.extend(data[m]["leads"])

        sequences = convert_sequences(detail, fix_brand)
        lead_rows = build_leads(raw_leads, verified_good)
        print(f"=== {camp_name} === ({', '.join(members)})")
        print(f"  raw leads: {len(raw_leads)}  verified+usable: {len(lead_rows)}  steps: {len(sequences)}  brand_fix: {fix_brand}")

        if not lead_rows:
            print("  SKIPPED (0 usable leads)\n")
            continue

        created = call("POST", "campaign/add/campaign", {"workspace_id": WS, "camp_name": camp_name})
        cid = created["id"]

        call("PATCH", "campaign/update/campaign", {
            "workspace_id": WS,
            "campaign_id": cid,
            "status": "PAUSED",
            "sequences": sequences,
            "email_accounts": all_mailboxes,
            "schedules": [{
                "daily_limit": 30,
                "daily_limit_new_lead": 30,
                "start_date": "2026-09-07",
                "end_date": "",
                "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
                "timezone": "America/New_York",
                "timing": {"from": "09:00", "to": "17:00"},
            }],
            "stop_on_lead_replied": "yes",
            "is_emailopened_tracking": "yes",
            "is_unsubscribed_link": "yes",
            "is_pause_on_bouncerate": "yes",
            "bounce_rate_limit": 4,
            "var_sel_type": "R_ROBIN",
        })

        # PlusVibe caps lead/add at 500 per call.
        CHUNK = 500
        for i in range(0, len(lead_rows), CHUNK):
            chunk = lead_rows[i:i + CHUNK]
            added = call("POST", "lead/add", {
                "workspace_id": WS, "campaign_id": cid, "leads": chunk,
                "skip_if_in_workspace": True,
            })
            print(f"  campaign_id={cid}  batch {i}-{i+len(chunk)}: {json.dumps(added)[:200]}")
        print()
        summary.append({"name": camp_name, "id": cid, "leads": len(lead_rows), "members": members})

    with open(os.path.join(SCRATCH, "batch2_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Built {len(summary)} campaigns.")


if __name__ == "__main__":
    main()
