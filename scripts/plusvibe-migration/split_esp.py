"""Further split each of the 4 UK/US legs into Google / Microsoft / Other
sub-campaigns by recipient mail provider (MX-record classification already
run in classify_esp.py -> domain_esp_classification.json). Nothing has sent
yet on any of the 4 legs (verified last_lead_sent empty on all 4 before
starting), so it's safe to rename/re-split without any duplicate-send risk.

For each leg: keep the existing campaign as the "Google" bucket (rename,
drop non-Google leads), and create two new campaigns for Microsoft and
Other (Other includes MX-unresolved domains, per Eikko's decision
2026-08-28). Same schedule/mailboxes/sequences as the parent leg throughout
— only the lead subset differs.
"""
import json, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(__file__))
API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
SCRATCH = os.path.dirname(__file__)
TODAY = "2026-08-28"


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


def domain_of(email):
    return email.split("@")[-1].strip().lower()


def esp_of(email, domain_class):
    c = domain_class.get(domain_of(email), "UNRESOLVED")
    return "OTHER" if c == "UNRESOLVED" else c


def create_and_fill(camp_name, tz, mailbox_ids, sequences, lead_rows):
    cid = call("POST", "campaign/add/campaign", {"workspace_id": WS, "camp_name": camp_name})["id"]
    call("PATCH", "campaign/update/campaign", {
        "workspace_id": WS, "campaign_id": cid,
        "status": "PAUSED",
        "sequences": sequences,
        "email_accounts": mailbox_ids,
        "schedules": [{
            "daily_limit": 6, "daily_limit_new_lead": 6,
            "start_date": TODAY, "end_date": "",
            "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
            "timezone": tz,
            "timing": {"from": "09:00", "to": "17:00"},
        }],
        "stop_on_lead_replied": "yes",
        "is_emailopened_tracking": "yes",
        "is_unsubscribed_link": "yes",
        "is_pause_on_bouncerate": "yes",
        "bounce_rate_limit": 4,
        "var_sel_type": "R_ROBIN",
    })
    CHUNK = 500
    for i in range(0, len(lead_rows), CHUNK):
        chunk = lead_rows[i:i + CHUNK]
        added = call("POST", "lead/add", {
            "workspace_id": WS, "campaign_id": cid, "leads": chunk,
            "skip_if_in_workspace": True,
        })
        print(f"    batch {i}-{i+len(chunk)}: {json.dumps(added)[:180]}")
    call("PATCH", "campaign/update/campaign", {"workspace_id": WS, "campaign_id": cid, "status": "ACTIVE"})
    print(f"  {camp_name} ({cid}) created, {len(lead_rows)} leads, ACTIVE")
    return cid


def split_leg(existing_cid, base_name, tz, mailbox_ids, sequences, lead_rows, domain_class, suffix_style):
    buckets = {"GOOGLE": [], "MICROSOFT": [], "OTHER": []}
    for l in lead_rows:
        buckets[esp_of(l["email"], domain_class)].append(l)
    print(f"{base_name}: total={len(lead_rows)}  google={len(buckets['GOOGLE'])}  "
          f"microsoft={len(buckets['MICROSOFT'])}  other={len(buckets['OTHER'])}")

    google_name, ms_name, other_name = suffix_style(base_name)

    # Existing campaign becomes the Google leg: rename, drop non-Google leads.
    non_google_emails = [l["email"] for l in buckets["MICROSOFT"] + buckets["OTHER"]]
    call("PATCH", "campaign/update/campaign", {
        "workspace_id": WS, "campaign_id": existing_cid, "camp_name": google_name,
    })
    CHUNK = 500
    for i in range(0, len(non_google_emails), CHUNK):
        res = call("POST", "lead/delete", {
            "workspace_id": WS, "campaign_id": existing_cid,
            "delete_list": non_google_emails[i:i + CHUNK],
        })
        print(f"    removed non-Google batch {i}-{i+len(non_google_emails[i:i+CHUNK])}: {json.dumps(res)[:120]}")
    print(f"  {google_name} ({existing_cid}) kept as Google leg, {len(buckets['GOOGLE'])} leads")

    ms_cid = create_and_fill(ms_name, tz, mailbox_ids, sequences, buckets["MICROSOFT"])
    other_cid = create_and_fill(other_name, tz, mailbox_ids, sequences, buckets["OTHER"])
    return {"google": existing_cid, "microsoft": ms_cid, "other": other_cid}


def main():
    domain_class = json.load(open(os.path.join(SCRATCH, "domain_esp_classification.json")))

    import classify_esp as C
    c1 = C.build_c1()
    c2 = C.build_c2()
    c1_uk = [l for l in c1 if l["country"] == "United Kingdom"]
    c1_us = [l for l in c1 if l["country"] != "United Kingdom"]
    c2_uk = [l for l in c2 if l["country"] == "United Kingdom"]
    c2_us = [l for l in c2 if l["country"] != "United Kingdom"]

    # Re-attach full lead payloads (classify_esp only kept email+country) by
    # rebuilding via the same source logic split_uk_us.py used.
    import csv
    CSV_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/3_UK_USA_Amazon_Seller_CLEANED.csv")
    DUP_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/cross_file_duplicate_emails.csv")
    dupes = {r["Email"].strip().lower() for r in csv.DictReader(open(DUP_PATH, encoding="utf-8-sig"))}
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    c1_full = {}
    for r in rows:
        email = r["Email"].strip().lower()
        if email in dupes:
            continue
        c1_full[email] = {
            "email": email,
            "first_name": r["First Name"].strip(), "last_name": r["Last Name"].strip(),
            "company_name": r["Company Name"].strip(), "company_website": r["Website"].strip(),
            "linkedin_person_url": r["Person Linkedin"].strip(), "linkedin_company_url": r["Company Linkedin URL"].strip(),
            "phone_number": r["Contact Number"].strip(), "country": r["Country"].strip(),
            "custom_variables": {
                "product_category": r["Product Type"].strip(), "amazon_url": r["Amazon"].strip(),
                "job_title": r["Title"].strip(), "revenue": r["Revenue"].strip(), "industry": r["Industry"].strip(),
            },
        }
    c1_us_full = [c1_full[l["email"]] for l in c1_us]
    c1_uk_full = [c1_full[l["email"]] for l in c1_uk]

    raw964 = json.load(open(os.path.join(SCRATCH, "amazon_seller_leads_full.json"), encoding="utf-8"))
    c2_full = {}
    for r in raw964:
        p = r.get("payload", {}) or {}
        e = r["email"].strip().lower()
        c2_full[e] = {
            "email": e, "first_name": r.get("first_name", "").strip(), "last_name": r.get("last_name", "").strip(),
            "company_name": r.get("company_name", "").strip(), "company_website": r.get("website", "").strip(),
            "linkedin_person_url": p.get("linkedIn", "").strip(), "linkedin_company_url": p.get("Company LinkedIn", "").strip(),
            "phone_number": p.get("Contact Number", "").strip(), "country": p.get("Country", "").strip(),
            "custom_variables": {
                "rating": p.get("Rating", "").strip().replace(",", "."), "amazon_url": p.get("Amazon URL", "").strip(),
                "job_title": p.get("jobTitle", "").strip(), "industry": p.get("Industry", "").strip(),
                "employees": p.get("Employees", "").strip(), "review_count": p.get("Review Count", "").strip(),
            },
        }
    raw363 = json.load(open(os.path.join(SCRATCH, "leftover_rating_leads.json"), encoding="utf-8"))
    for r in raw363:
        e = r["email"].strip().lower()
        if e in c2_full:
            continue
        c2_full[e] = {
            "email": e, "first_name": r["first_name"], "last_name": r["last_name"],
            "company_name": r["company_name"], "company_website": r["company_website"],
            "linkedin_person_url": r["linkedin_person_url"], "linkedin_company_url": r["linkedin_company_url"],
            "phone_number": r["phone_number"], "country": r["country"],
            "custom_variables": {
                "rating": r["rating"], "amazon_url": r["amazon_url"], "job_title": r["job_title"],
                "industry": r["industry"], "employees": r["employees"], "review_count": r["review_count"],
            },
        }
    c2_us_full = [c2_full[l["email"]] for l in c2_us]
    c2_uk_full = [c2_full[l["email"]] for l in c2_uk]

    res = call("GET", f"account/list?workspace_id={WS}")
    c1_mailboxes = [a["id"] for a in res["accounts"] if a["email"].split("@")[1] in ("sellervate.net", "starfix.online")]
    c2_mailboxes = [a["id"] for a in res["accounts"] if a["email"].split("@")[1] == "hellostarfix.com"]

    import sequences as S1
    import sequences_rating as S2

    results = {}
    results["us_ca"] = split_leg(
        "6a8cf6f27e5c6119d8830749", "Amazon Seller US/CA", "America/New_York",
        c1_mailboxes, S1.build_sequences(), c1_us_full, domain_class,
        lambda b: (f"{b} - Google [MIGRATED]", f"{b} - Microsoft [MIGRATED]", f"{b} - Other [MIGRATED]"),
    )
    results["uk"] = split_leg(
        "6a90b3bcf68baa1111ed5c7f", "Amazon Seller UK", "Europe/London",
        c1_mailboxes, S1.build_sequences(), c1_uk_full, domain_class,
        lambda b: (f"{b} - Google [MIGRATED]", f"{b} - Microsoft [MIGRATED]", f"{b} - Other [MIGRATED]"),
    )
    results["rating_us"] = split_leg(
        "6a8ee087c3903d2a71741b72", "Amazon Seller - Rating US", "America/New_York",
        c2_mailboxes, S2.build_sequences(), c2_us_full, domain_class,
        lambda b: (f"{b} - Google [MIGRATED FROM INSTANTLY DRAFT]", f"{b} - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", f"{b} - Other [MIGRATED FROM INSTANTLY DRAFT]"),
    )
    results["rating_uk"] = split_leg(
        "6a90b41d24acfefeb9390a4c", "Amazon Seller - Rating UK", "Europe/London",
        c2_mailboxes, S2.build_sequences(), c2_uk_full, domain_class,
        lambda b: (f"{b} - Google [MIGRATED FROM INSTANTLY DRAFT]", f"{b} - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", f"{b} - Other [MIGRATED FROM INSTANTLY DRAFT]"),
    )

    with open(os.path.join(SCRATCH, "esp_split_result.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\nAll done:", json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
