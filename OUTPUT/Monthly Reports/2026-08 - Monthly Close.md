# August 2026 — Monthly Close

**Generated:** 2026-08-25 · by `cfo` (first real close ever produced from this system)
**FX rate:** **NOT SET** — `CLIENT PROFILES/Important info.md` → `## FX Rate (set monthly by Eikko)` is empty. No currency conversion performed anywhere in this report.
**Source:** Notion → [Finance Tracker and Bills](https://app.notion.com/p/3bf811e21c7f80ddbcc1ceb7c613dc16) · read live, nothing written back.

**Coverage**
| Data source | Rows | Carrying a value | |
|---|---|---|---|
| Finance Tracker — `Income` | 9 | **5** | 4 rows pending |
| Finance Tracker — `Bills` | 9 | 6 | 3 rows empty |
| Bills — `Monthly Payment ` | 19 | 18 | |
| Bills — `Total Amount of Debt` | 19 | 16 | |
| Bills — `Total Amount Paid` | 19 | **1** | see Debt Payoff Plan |

> **Read the coverage line before the totals.** ₱37,590 from 5 of 9 rows is a different fact from ₱37,590 from 9 of 9. Four August rows have no income figure recorded and are reported as **pending**, not as zero.

---

## 1. Income received

| Date | Client | Income ₱ | Details as logged |
|---|---|---|---|
| 2026-08-17 | Cüneyt (Sellervate) | 6,400 | received through Wise for 15 hours work 7$ per hour from last week |
| 2026-08-18 | Yoni | 14,400 | Through Wise |
| 2026-08-20 | Chris Caffera | 8,800 | Through Wise |
| 2026-08-21 | **Darius** | 1,590 | Through Wise |
| 2026-08-25 | Cüneyt (Sellervate) | 6,400 | — |
| 2026-08-25 | Yoni | **pending — not recorded** | — |
| 2026-08-26 | Chris Drew (Satlas) | **pending — not recorded** | — |
| 2026-08-28 | Chris Caffera | **pending — not recorded** | — |
| 2026-08-31 | Yoni | **pending — not recorded** | — |
| | **Total recorded** | **₱37,590** | from 5 of 9 rows |

## 2. Income by client

| Client | Recorded ₱ | Pending rows |
|---|---|---|
| Yoni (Albert Scott) | 14,400 | 2 — 08-25, 08-31 |
| Chris Caffera | 8,800 | 1 — 08-28 |
| Cüneyt (Sellervate) | 12,800 | — |
| Darius | 1,590 | — |
| Chris Drew (Satlas) | **0 recorded** | 1 — 08-26 |
| **Total** | **₱37,590** | **4 pending** |

Chris Drew is on a **$200 AUD/month flat** arrangement — his row is a scheduled flat payment, not an hourly total. With FX unset, that AUD figure is not converted here.

## 3. Expenses — parsed from the `Bills` free-text field

Every line traced to its Finance Tracker row. Each row's parsed total is reconciled back against the original string.

**Paid to date (on or before 2026-08-25) — ₱31,354**

| Row date | Item | ₱ | Category |
|---|---|---|---|
| 08-17 | Initao | 3,100 | **ambiguous — needs Eikko** |
| 08-17 | Dongki Allowance | 500 | **ambiguous — needs Eikko** |
| 08-18 | Rent | 9,500 | Housing |
| 08-18 | Laundry | 2,000 | Other |
| 08-18 | Tubil | 1,000 | **ambiguous — needs Eikko** |
| 08-18 | EatOut | 3,204 | Food |
| 08-18 | HBO | 400 | Subscriptions (Personal) |
| 08-20 | SLoan | 2,128 | Debt service |
| 08-20 | GLoan | 1,300 | Debt service |
| 08-20 | HomeCreditCard | 2,000 | Debt service |
| 08-25 | Homecredit Laptop | 5,222 | Debt service |
| 08-25 | Dongki and Nanay Allowance | 1,000 | **ambiguous — needs Eikko** |

**Scheduled later this month — ₱20,000**

| Row date | Item | ₱ | Category |
|---|---|---|---|
| 08-28 | Loan Ate | 10,000 | **ambiguous — needs Eikko** |
| 08-31 | Loan Ate | 10,000 | **ambiguous — needs Eikko** |

**Reconciliation check:** every one of the 6 non-empty `Bills` strings re-sums to its parsed total exactly — 3,600 / 16,104 / 5,428 / 6,222 / 10,000 / 10,000 = **₱51,354**. ✅ No row failed to reconcile.

Categories above are **proposed, not applied** — nothing has been written to Notion. Six line items across four distinct names (`Initao`, `Dongki Allowance`, `Dongki and Nanay Allowance`, `Tubil`, `Loan Ate`) are genuinely ambiguous and have deliberately **not** been guessed.

## 4. Business vs personal

**Business expenses: not recorded.**

The Tools & Subscriptions register does not exist yet — its creation is gated on Eikko's approval and had not been granted when this close was run. Without the `Type` tag there is no way to separate business from personal spend.

Every parsed line above reads as **personal** (housing, food, allowances, debt service, HBO). **No business expense line appears anywhere in the August Finance Tracker data** — notably, no Claude subscription line and no iCloud line. This is reported as *not recorded*, **not as ₱0**. Eikko's known business tooling (Claude ₱7,000/mo, Apple iCloud ₱600/mo) is real spend that this close cannot see.

## 5. Net — actuals only

| | ₱ |
|---|---|
| Income recorded (5 of 9 rows) | 37,590 |
| Expenses paid to date | (31,354) |
| **Net, recorded-to-date** | **6,236** |
| | |
| Expenses scheduled 08-28 → 08-31 | (20,000) |
| **Net if the month closes with no further income recorded** | **(13,764)** |

**No income target is reported.** This system has never had one set — `Important info.md` contains no target section. Actuals only, by design.

**This is not a full-month P&L.** Four income rows are blank and business expenses are invisible. It is an honest partial: what is recorded, and what is missing.

## 6. Data quality — every gap, named

1. **Four income rows carry no amount** — Yoni 08-25, Chris Drew 08-26, Chris Caffera 08-28, Yoni 08-31. Fill these and the close completes.
2. **Business expenses are entirely absent** from the tracker. The register that would capture them is not built.
3. **Billable hours: not logged, for every client, for the whole month.** No EOD log in `OUTPUT/End-of-Day Reports/` records an hours figure — the only `Hours:` string in that folder is an example inside `README.md`'s template. TimeDoctor (Yoni's intended source of truth) is not connected. **No hours figure appears in this report for any client, and none can be produced.**
4. **Chris Caffera's contracted hours are contested** — 20h/wk vs 15h/wk, unresolved since 2026-08-24. Even if hours were logged, his monthly total could not be computed.
5. **Yoni's rate is a live mismatch** — `$5/hr` in his profile header, `(TBD)` in `Important info.md`.
6. **Chris Soriano's EOD log is still the unfilled `[DATE]` template** — zero real entries.
7. **`Bills` is free text**, so every figure in §3 required hand-parsing. Migration to a linked `Expenses` data source is proposed but not approved.
8. **Opening cash balance is not recorded anywhere** — not in Notion, not locally. Net figures above are flows, not a position. Solvency cannot be stated.
9. **FX rate not set** — see below.

## 7. Bridge

> **Bridge — August 2026:** FX rate not set for August — business-to-personal bridge not computed. Business net cannot be expressed in ₱, and the ₱49,806 of fixed personal obligations therefore cannot be set against it. Fill `## FX Rate (set monthly by Eikko)` in `CLIENT PROFILES/Important info.md` and re-run.

---

## Reconciliation against the 2026-08-25 verified figures

Checked by hand, row by row, against live Notion data.

| Measure | Expected | Live | Result |
|---|---|---|---|
| Fixed monthly obligations | ₱49,806 | **₱49,806** | ✅ exact — 18 of 19 rows, confirmed twice (direct sum, and as the September total in the runway ledger) |
| Total outstanding debt | ₱340,672 | **₱340,672** | ✅ exact — 16 of 19 rows |
| August income received | ₱54,570 (6 of 9 rows) | **₱37,590 (5 of 9 rows)** | ❌ **short by ₱16,980, one row** |

**The discrepancy has not been adjusted to fit.** It traces entirely to **one row: Yoni, 2026-08-25** (`https://app.notion.com/3c2811e21c7f80b5beb9ddd7e6309461`).

- ₱54,570 − ₱37,590 = **₱16,980** — exactly the figure the build brief attributes to that row.
- 6 − 5 = **1 row**.
- That row now carries **no `Income` value**, and its `Bills` string reads `Homecredit Laptop - 5222 | Dongki and Nanay Allowance - 1000` — **not** the `Claude Max Plan - 8000` the brief describes. The string `Claude` appears in none of the 9 `Bills` values.

**Most likely explanation:** the row was edited between the 2026-08-25 verification and this run — income cleared, bills string replaced. It is not a new row added since (a new row would push income up, not down), and it is not an arithmetic error on either side, since the other two measures reconcile to the peso.

**Needs Eikko:** was ₱16,980 removed from that row deliberately, or lost? And where did the `Claude Max Plan - 8000` entry go — the one the CFO build was meant to correct to ₱7,000?
