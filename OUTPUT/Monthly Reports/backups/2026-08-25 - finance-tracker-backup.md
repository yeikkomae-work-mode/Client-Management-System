# Finance Tracker and Bills — pre-migration backup

**Taken:** 2026-08-25, before the Notion Expenses migration.
**Source:** Notion database `Finance Tracker and Bills` (https://app.notion.com/p/3bf811e21c7f80ddbcc1ceb7c613dc16)
**Reason:** the Expenses migration is the only irreversible step in the C-suite build. This is the restore point.

## Data source 1 — Finance Tracker (9 rows)
collection://3bf811e2-1c7f-80d2-9c10-000b0ef13bee

| Received | Client | Income | Bills (free text) | Details |
|---|---|---|---|---|
| 2026-08-17 | Cuneyt | 6400 | Initao - 3100 \| Dongki Allowance - 500 | received through Wise for 15 hours work 7$ per hour from last week |
| 2026-08-18 | Yoni | 14400 | Rent - 9500 \| Laundry - 2000 \| Tubil - 1000 \| EatOut - 3204 \| HBO - 400 | Through Wise |
| 2026-08-20 | Chris Caffera | 8800 | SLoan - 2128 \| GLoan - 1300 \| HomeCreditCard - 2000 | Through Wise |
| 2026-08-21 | Darius | 1590 | (none) | Through Wise |
| 2026-08-25 | Cuneyt | 6400 | (none) | (none) |
| 2026-08-25 | Yoni | (none) | Homecredit Laptop - 5222 \| Dongki and Nanay Allowance - 1000 | (none) |
| 2026-08-26 | Chris Drew | (none) | (none) | (none) |
| 2026-08-28 | Chris Caffera | (none) | Loan Ate - 10000 | (none) |
| 2026-08-31 | Yoni | (none) | Loan Ate - 10000 | (none) |

## Data source 2 — Bills / Debt Paid Tracker (19 rows)
collection://3bf811e2-1c7f-80dc-a615-000be3abd79f

| Debt From | Total Amount of Debt | Total Amount Paid | Monthly Payment | Due Date |
|---|---|---|---|---|
| Billease Cristy Account | 12457 | (none) | 2077 | 2026-09-01 |
| Billease Eikko Account | 4811 | (none) | 1602 | 2026-09-01 |
| Wifi | (none) | (none) | 1500 | 2026-09-03 |
| Electricity and Water | (none) | (none) | (none) | 2026-09-07 |
| Sloan | 5700 | 3800 | 1900 | 2026-09-08 |
| Gloan | 19102 | (none) | 1800 | 2026-09-09 |
| Atome | 5990 | (none) | 2662 | 2026-09-09 |
| Sloan | 16341 | (none) | 2971 | 2026-09-11 |
| Tiktok Loan | 5900 | (none) | 1967 | 2026-09-12 |
| HomeCredit Refrigerator | 2672 | (none) | 1336 | 2026-09-13 |
| Sloan | 8744 | (none) | 2186 | 2026-09-14 |
| Tiktok | 4300 | (none) | 2500 | 2026-09-15 |
| Spaylater | 57096 | (none) | 6022 | 2026-09-15 |
| Apartment | (none) | (none) | 9500 | 2026-09-15 |
| Gloan | 6796 | (none) | 1133 | 2026-09-16 |
| Home Credit Card | 20648 | (none) | 2000 | 2026-09-21 |
| Gloan | 9200 | (none) | 1300 | 2026-09-24 |
| HomeCredit (Laptop) | 156660 | (none) | 5222 | 2026-09-29 |
| Sloan | 4255 | (none) | 2128 | 2026-09-30 |

**Note:** `Total Amount Paid` is populated on exactly 1 of 19 rows (Sloan, 3800). `Balance` is a formula column and is therefore derived, not stored.
