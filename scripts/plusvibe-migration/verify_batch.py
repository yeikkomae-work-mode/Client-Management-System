"""Run every deduped lead through MillionVerifier, concurrently (curl per-call,
since both requests and urllib get 403'd by Cloudflare here). Keeps only
quality == "good". Reports progress periodically since ~2,700 lookups at
~1-2s each takes several minutes even parallelized.
"""
import json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

MV_KEY = os.environ["MV_KEY"]  # never hardcode this — read from the environment
CONCURRENCY = 15

def verify(email):
    url = f"https://api.millionverifier.com/api/v3/?api={MV_KEY}&email={email}&timeout=10"
    try:
        out = subprocess.run(["curl", "-sS", "--max-time", "20", url],
                              capture_output=True, text=True, timeout=25).stdout
        return email, json.loads(out)
    except Exception as e:
        return email, {"error": str(e), "quality": "error"}


def main():
    deduped = json.load(open("deduped_other24_leads.json"))
    emails = list(deduped.keys())
    print(f"verifying {len(emails)} emails, concurrency={CONCURRENCY}")

    results = {}
    quality_counts = {}
    done = 0
    t0 = time.time()

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = {ex.submit(verify, e): e for e in emails}
        for fut in as_completed(futures):
            email, res = fut.result()
            results[email] = res
            q = res.get("quality", "error")
            quality_counts[q] = quality_counts.get(q, 0) + 1
            done += 1
            if done % 200 == 0 or done == len(emails):
                elapsed = time.time() - t0
                rate = done / elapsed
                eta = (len(emails) - done) / rate if rate else 0
                print(f"  {done}/{len(emails)}  elapsed={elapsed:.0f}s  eta={eta:.0f}s  "
                      f"quality so far: {quality_counts}")

    with open("millionverifier_results.json", "w") as f:
        json.dump(results, f)

    print("\nFINAL:", quality_counts)
    good = [e for e, r in results.items() if r.get("quality") == "good"]
    print(f"PASS (quality=good): {len(good)}")
    with open("verified_good_emails.json", "w") as f:
        json.dump(good, f)


if __name__ == "__main__":
    main()
