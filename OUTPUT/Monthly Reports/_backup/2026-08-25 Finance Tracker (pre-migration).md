# Finance Tracker — full export, pre-migration backup

**Exported:** 2026-08-25, during the CFO agent build
**Source:** Notion → [Finance Tracker and Bills](https://app.notion.com/p/3bf811e21c7f80ddbcc1ceb7c613dc16) → Finance Tracker
**Data source:** `collection://3bf811e2-1c7f-80d2-9c10-000b0ef13bee`
**Workspace:** WORK Command Center (`443811e2-1c7f-819e-9457-00039bc4d465`)
**Rows:** 9 (complete — `has_more: false`)

> **Why this file exists.** The proposed migration of the free-text `Bills` property into a linked `Expenses` data source is the least reversible step in the CFO build. This is the verbatim pre-migration state of every row and every property. **The migration has NOT been performed** — it is gated on Eikko's approval and had not been granted at the time of this export. This backup was taken first regardless, so the safety net exists before anything is proposed.
>
> Verbatim means verbatim: `Bills` strings are reproduced exactly as stored, including inconsistent capitalisation (`SLoan` / `Sloan`, `HomeCreditCard` / `Homecredit`), spacing, and pipe delimiters. Do not tidy this file.

## All properties, all rows

| # | Received Date | Select | Income (₱) | Details | Bills (verbatim) | Page URL | Created (UTC) |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-17 | Cuneyt | 6400 | received through Wise for 15 hours work 7$ per hour from last week | `Initao - 3100 \| Dongki Allowance - 500` | https://app.notion.com/3bf811e21c7f80efac98d4205e8caba3 | 2026-08-17 00:42:57Z |
| 2 | 2026-08-18 | Yoni | 14400 | Through Wise | `Rent - 9500 \| Laundry - 2000 \| Tubil - 1000 \| EatOut - 3204 \| HBO - 400` | https://app.notion.com/3bf811e21c7f8007899fe32b74b4532b | 2026-08-17 14:21:20Z |
| 3 | 2026-08-20 | Chris Caffera | 8800 | Through Wise | `SLoan - 2128 \| GLoan - 1300 \| HomeCreditCard - 2000` | https://app.notion.com/3c2811e21c7f8086939be01e85350321 | 2026-08-20 12:38:14Z |
| 4 | 2026-08-21 | Darius | 1590 | Through Wise | *(empty)* | https://app.notion.com/3c2811e21c7f80e3baa9f3d58cb32dc4 | 2026-08-20 21:00:30Z |
| 5 | 2026-08-25 | Cuneyt | 6400 | *(empty)* | *(empty)* | https://app.notion.com/3c6811e21c7f805699fcdde50d8109f0 | 2026-08-24 21:24:56Z |
| 6 | 2026-08-25 | Yoni | *(empty)* | *(empty)* | `Homecredit Laptop - 5222 \| Dongki and Nanay Allowance - 1000` | https://app.notion.com/3c2811e21c7f80b5beb9ddd7e6309461 | 2026-08-20 13:23:06Z |
| 7 | 2026-08-26 | Chris Drew | *(empty)* | *(empty)* | *(empty)* | https://app.notion.com/3c2811e21c7f8091856ef5ba542364ff | 2026-08-20 13:29:12Z |
| 8 | 2026-08-28 | Chris Caffera | *(empty)* | *(empty)* | `Loan Ate - 10000` | https://app.notion.com/3c2811e21c7f8079a0fccef8ae440dc9 | 2026-08-20 13:23:38Z |
| 9 | 2026-08-31 | Yoni | *(empty)* | *(empty)* | `Loan Ate - 10000` | https://app.notion.com/3c2811e21c7f80648740fd5e70f5cea1 | 2026-08-20 13:28:48Z |

**Income coverage:** 5 of 9 rows carry a value. Sum = **₱37,590**.
**Bills coverage:** 6 of 9 rows carry a string. Parsed sum = **₱51,354**.

## ⚠️ Row 6 — discrepancy against the 2026-08-25 verified figures

The CFO build brief states that row 6 (Yoni, 2026-08-25) carried **`Income` = ₱16,980** and a `Bills` field containing **`Claude Max Plan - 8000`**, and that August income totalled **₱54,570 across 6 of 9 rows**.

**As exported above, row 6 carries no `Income` value, and its `Bills` string is `Homecredit Laptop - 5222 | Dongki and Nanay Allowance - 1000` — no `Claude Max Plan` entry.** The string `Claude` does not appear in any of the 9 `Bills` values.

₱54,570 − ₱37,590 = **₱16,980** exactly, and 6 − 5 = 1 row. The entire discrepancy is this single row. It appears to have been edited between the 2026-08-25 verification and this export: the income figure cleared and the bills string replaced.

**Nothing has been changed to reconcile this.** The export above is the live state as read. See `2026-08 - Monthly Close.md` for the full reconciliation.

## Bills data source — companion export

Also captured for completeness. Source: `collection://3bf811e2-1c7f-80dc-a615-000be3abd79f`. 19 rows, complete.

| Debt From | Monthly Payment | Total Amount of Debt | Total Amount Paid | Due Date |
|---|---|---|---|---|
| Billease Cristy Account | 2077 | 12457 | *(empty)* | 2026-09-01 |
| Billease Eikko Account | 1602 | 4811 | *(empty)* | 2026-09-01 |
| Wifi | 1500 | *(empty)* | *(empty)* | 2026-09-03 |
| Electricity and Water | *(empty)* | *(empty)* | *(empty)* | 2026-09-07 |
| Sloan | 1900 | 5700 | **3800** | 2026-09-08 |
| Gloan | 1800 | 19102 | *(empty)* | 2026-09-09 |
| Atome | 2662 | 5990 | *(empty)* | 2026-09-09 |
| Sloan | 2971 | 16341 | *(empty)* | 2026-09-11 |
| Tiktok Loan | 1967 | 5900 | *(empty)* | 2026-09-12 |
| HomeCredit Refrigerator | 1336 | 2672 | *(empty)* | 2026-09-13 |
| Sloan | 2186 | 8744 | *(empty)* | 2026-09-14 |
| Tiktok | 2500 | 4300 | *(empty)* | 2026-09-15 |
| Spaylater | 6022 | 57096 | *(empty)* | 2026-09-15 |
| Apartment | 9500 | *(empty)* | *(empty)* | 2026-09-15 |
| Gloan | 1133 | 6796 | *(empty)* | 2026-09-16 |
| Home Credit Card | 2000 | 20648 | *(empty)* | 2026-09-21 |
| Gloan | 1300 | 9200 | *(empty)* | 2026-09-24 |
| HomeCredit (Laptop) | 5222 | 156660 | *(empty)* | 2026-09-29 |
| Sloan | 2128 | 4255 | *(empty)* | 2026-09-30 |

`Monthly Payment ` — 18 of 19 rows, sum **₱49,806**.
`Total Amount of Debt` — 16 of 19 rows, sum **₱340,672**.
`Total Amount Paid` — **1 of 19 rows**, sum ₱3,800.
`Balance` is a formula property and is not queryable via SQL; it is derived from the two columns above and therefore understates progress on the 18 rows where `Total Amount Paid` is empty.

**Note:** five rows share the title `Sloan`/`Gloan` with different amounts and due dates. They are distinct debts distinguished only by due date. Any migration or dedup pass must not merge them.
