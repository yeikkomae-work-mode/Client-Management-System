# Starfix Lead Database Cleaning — 2026-08-21

Source: 3 files Eikko uploaded (Amazon USA Product Review 2nd SMB, Amazon Leads MAIN List, UK_USA Amazon Seller). A 4th leftover file (SellerVeta Database) was already in uploads from a prior request and was **not** included here — flag if it should be merged in too.

## What was cleaned

| File | Raw rows | Removed (missing/invalid email) | Removed (duplicate email) | Final clean rows |
|---|---|---|---|---|
| 1_Amazon_USA_Product_Review_2nd | 654 | 41 | 0 | **613** |
| 2_Amazon_Leads_MAIN_List | 735 | 1 (blank row) | 20 | **714** |
| 3_UK_USA_Amazon_Seller | 109 | 0 | 0 | **109** |
| **Total unique clean leads** | | | | **1,436** |

Also fixed:
- **File 2** had 6 stray empty trailing columns from the Google Sheet export (`Unnamed: 21–26`) — dropped.
- All 3 files had stray embedded `\r` characters inside some cells (mostly the Country/Comment fields), which corrupted row alignment when re-parsed. Stripped from every cell so the CSVs open cleanly in Excel/Instantly without split rows.
- **4 cross-file duplicate rows** (2 unique emails — `philip@palladiobeauty.com`, `prudence@beautybyearth.com`) appear in both File 2 (MAIN List) and File 3 (UK_USA Seller). Not removed automatically — see `cross_file_duplicate_emails.csv`. Recommend keeping them in File 2 only and removing from File 3 before upload, since MAIN List is the larger/primary list.

## Personalization fields — what's real per file

| File | Star rating | Product name (clean) | Negative review count | Product Type |
|---|---|---|---|---|
| 1 — Product Review 2nd SMB | ✅ 613/613 populated | ⚠️ no clean column (Company name only) | ❌ not present | — |
| 2 — MAIN List | ✅ 714/714 populated | ⚠️ no clean column (Company name only) | ❌ not present | — |
| 3 — UK_USA Seller | ❌ not present | — | — | ✅ 109/109 populated |

Bottom line: Files 1 & 2 can use `{{star_rating}}` personalization (the "realistic version" sequence already drafted on 2026-08-20). File 3 has no rating data at all — its only usable personalization field is `Product Type` (category-level, e.g. "Health Products," "Pet Animals Accessories"), which needs a different angle since it can't reference star rating or review issues.

## Files in this folder

- `1_Amazon_USA_Product_Review_2nd_CLEANED.csv`
- `2_Amazon_Leads_MAIN_List_CLEANED.csv`
- `3_UK_USA_Amazon_Seller_CLEANED.csv`
- `cross_file_duplicate_emails.csv`
