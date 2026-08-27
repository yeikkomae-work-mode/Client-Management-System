"""Cüneyt's answer came back: fix SalesFix -> SellerVate, same as Starfix.
Patch sequences only on the already-built campaign; leave leads, mailboxes,
schedule, and PAUSED status untouched per his explicit instruction.
"""
import json, os
import build_batch2 as B

CID = "6a9023eb0d0bcf449012149a"

seqs = json.load(open(os.path.join(os.path.dirname(__file__), "salesfix_sequences_fixed.json")))

B.call("PATCH", "campaign/update/campaign", {
    "workspace_id": B.WS,
    "campaign_id": CID,
    "sequences": seqs,
})
print("sequences updated")
