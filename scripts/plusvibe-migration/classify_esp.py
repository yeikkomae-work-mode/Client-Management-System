"""Classify every lead across the 4 live campaigns by recipient mail
provider (Google Workspace / Microsoft 365 / other) via MX record lookup,
so they can be split into "<name> - Google" / "<name> - Microsoft" legs.
Read-only — no PlusVibe writes here, just reconstructs lead lists (same
source data as split_uk_us.py) and resolves DNS.
"""
import csv, json, os, re
from concurrent.futures import ThreadPoolExecutor, as_completed

import dns.resolver

SCRATCH = os.path.dirname(__file__)
resolver = dns.resolver.Resolver()
resolver.timeout = 4
resolver.lifetime = 4


def classify_domain(domain):
    try:
        answers = resolver.resolve(domain, "MX")
        mx_hosts = " ".join(str(a.exchange).lower() for a in answers)
    except Exception as e:
        return "UNRESOLVED"
    if "google.com" in mx_hosts or "googlemail.com" in mx_hosts:
        return "GOOGLE"
    if "outlook.com" in mx_hosts or "protection.outlook.com" in mx_hosts:
        return "MICROSOFT"
    return "OTHER"


def domain_of(email):
    return email.split("@")[-1].strip().lower()


def build_c1():
    CSV_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/3_UK_USA_Amazon_Seller_CLEANED.csv")
    DUP_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/cross_file_duplicate_emails.csv")
    dupes = {r["Email"].strip().lower() for r in csv.DictReader(open(DUP_PATH, encoding="utf-8-sig"))}
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    out = []
    for r in rows:
        email = r["Email"].strip().lower()
        if email in dupes:
            continue
        out.append({"email": email, "country": r["Country"].strip()})
    return out


def build_c2():
    raw964 = json.load(open(os.path.join(SCRATCH, "amazon_seller_leads_full.json"), encoding="utf-8"))
    out, seen = [], set()
    for r in raw964:
        p = r.get("payload", {}) or {}
        e = r["email"].strip().lower()
        seen.add(e)
        out.append({"email": e, "country": p.get("Country", "").strip()})
    raw363 = json.load(open(os.path.join(SCRATCH, "leftover_rating_leads.json"), encoding="utf-8"))
    for r in raw363:
        e = r["email"].strip().lower()
        if e in seen:
            continue
        seen.add(e)
        out.append({"email": e, "country": r["country"]})
    return out


def main():
    c1 = build_c1()
    c2 = build_c2()
    c1_uk = [l for l in c1 if l["country"] == "United Kingdom"]
    c1_us = [l for l in c1 if l["country"] != "United Kingdom"]
    c2_uk = [l for l in c2 if l["country"] == "United Kingdom"]
    c2_us = [l for l in c2 if l["country"] != "United Kingdom"]

    legs = {
        "Amazon Seller US/CA": c1_us,
        "Amazon Seller UK": c1_uk,
        "Amazon Seller - Rating US": c2_us,
        "Amazon Seller - Rating UK": c2_uk,
    }

    all_domains = set()
    for leads in legs.values():
        for l in leads:
            all_domains.add(domain_of(l["email"]))
    print(f"total unique domains to resolve: {len(all_domains)}")

    domain_class = {}
    with ThreadPoolExecutor(max_workers=20) as ex:
        futs = {ex.submit(classify_domain, d): d for d in all_domains}
        done = 0
        for fut in as_completed(futs):
            d = futs[fut]
            domain_class[d] = fut.result()
            done += 1
            if done % 100 == 0:
                print(f"  resolved {done}/{len(all_domains)}")

    with open(os.path.join(SCRATCH, "domain_esp_classification.json"), "w") as f:
        json.dump(domain_class, f, indent=2)

    print()
    for name, leads in legs.items():
        counts = {"GOOGLE": 0, "MICROSOFT": 0, "OTHER": 0, "UNRESOLVED": 0}
        for l in leads:
            counts[domain_class[domain_of(l["email"])]] += 1
        print(f"{name:30s} total={len(leads):4d}  google={counts['GOOGLE']:4d}  "
              f"microsoft={counts['MICROSOFT']:4d}  other={counts['OTHER']:4d}  "
              f"unresolved={counts['UNRESOLVED']:4d}")


if __name__ == "__main__":
    main()
