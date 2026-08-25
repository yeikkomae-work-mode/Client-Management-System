# Debt Payoff Plan — **PROVISIONAL**

> **PROVISIONAL.** `Total Amount Paid` is populated on 1 of 19 rows and is not maintained, so `Balance` understates progress on 18 debts. Every payoff date below is a ceiling, not a forecast.

**Generated:** 2026-08-25 · by `cfo`
**FX rate:** **NOT SET** (`CLIENT PROFILES/Important info.md`). All figures natively ₱; no conversion performed.
**Source:** Notion → Bills data source (`collection://3bf811e2-1c7f-80dc-a615-000be3abd79f`), read live.

**Coverage:** 19 rows · `Total Amount of Debt` on **16** · `Monthly Payment ` on **18** · `Total Amount Paid` on **1**.

**This is arithmetic, not advice.** It is a projection of what the numbers do if nothing changes. It is not a recommendation about which debt to pay, whether to consolidate, or how to prioritise against living costs. Those are Eikko's decisions.

---

## Assumptions — all of them, stated

1. **Modelled against `Total Amount of Debt` (gross), not remaining balance.** Only one row (Sloan, due 09-08) records anything paid — ₱3,800 of ₱5,700. The other 15 debt-carrying rows are modelled from their full original amount. **Real balances are lower than modelled; real payoff is sooner.** This is why every date is a ceiling.
2. **No interest is applied.** The Bills data source has **no interest-rate field**. This is straight amortisation of principal. Real-world payoff with interest will be **slower** than modelled — which cuts against assumption 1. The two errors point in opposite directions and their net effect is unknown.
3. **Payments held flat** at the recorded `Monthly Payment ` values.
4. **No new borrowing.**
5. **Rollover applied** — when a debt clears, its payment redirects to the next target. Total monthly pool held constant at **₱38,806**.
6. **Three rows excluded** — `Wifi` (₱1,500/mo), `Electricity and Water` (no amount), `Apartment` (₱9,500/mo) carry no `Total Amount of Debt`. They are recurring living costs, not debts with a balance. They are part of the ₱49,806 monthly obligation but not part of the ₱340,672 payoff.
7. **"Avalanche" here means highest-balance-first, not highest-rate-first** — because no rate data exists. This is a substitute, and a poor one: true avalanche minimises interest, and without rates that optimisation cannot be performed at all.

---

## The book — ₱340,672 across 16 debts

| Debt | Monthly ₱ | Total ₱ | Share | Months at own payment |
|---|---|---|---|---|
| **HomeCredit (Laptop)** | 5,222 | **156,660** | **46.0%** | 30.0 |
| **Spaylater** | 6,022 | **57,096** | **16.8%** | 9.5 |
| Home Credit Card | 2,000 | 20,648 | 6.1% | 10.3 |
| Gloan (09-09) | 1,800 | 19,102 | 5.6% | 10.6 |
| Sloan (09-11) | 2,971 | 16,341 | 4.8% | 5.5 |
| Billease Cristy Account | 2,077 | 12,457 | 3.7% | 6.0 |
| Gloan (09-24) | 1,300 | 9,200 | 2.7% | 7.1 |
| Sloan (09-14) | 2,186 | 8,744 | 2.6% | 4.0 |
| Gloan (09-16) | 1,133 | 6,796 | 2.0% | 6.0 |
| Atome | 2,662 | 5,990 | 1.8% | 2.3 |
| Tiktok Loan | 1,967 | 5,900 | 1.7% | 3.0 |
| Sloan (09-08) | 1,900 | 5,700 | 1.7% | 3.0 *(₱3,800 already paid — the one maintained row)* |
| Billease Eikko Account | 1,602 | 4,811 | 1.4% | 3.0 |
| Tiktok | 2,500 | 4,300 | 1.3% | 1.7 |
| Sloan (09-30) | 2,128 | 4,255 | 1.2% | 2.0 |
| HomeCredit Refrigerator | 1,336 | 2,672 | 0.8% | 2.0 |
| **Total** | **38,806** | **340,672** | 100% | |

### Concentration

**HomeCredit (Laptop) is ₱156,660 — 46.0% of the total book, in one row.** Add SPayLater's ₱57,096 (16.8%) and **two debts are 62.8% of everything owed**. The remaining 14 debts together are ₱126,916.

At its own ₱5,222/month the laptop takes **30 months** standalone — more than three times any other debt on the book. It is the single item that determines when this ends.

---

## Avalanche vs snowball

**Both strategies clear the book in the same month.** With a fixed ₱38,806 pool, no interest, and full rollover, total ÷ pool = 340,672 ÷ 38,806 = **8.8 months**, and the ordering cannot change that arithmetic. Ordering changes *which* debts clear *when* — not the finish line.

| | Avalanche (highest balance first) | Snowball (smallest balance first) |
|---|---|---|
| **Debt-free** | **Month 9** | **Month 9** |
| Debts cleared by month 3 | 6 | 9 |
| Debts cleared by month 6 | 11 | 15 |
| Debts left at month 8 | 4 | 1 |

### Clearing order

| Month | Avalanche clears | Snowball clears |
|---|---|---|
| 2 | Tiktok · Sloan (09-30) · HomeCredit Refrigerator | HomeCredit Refrigerator · Sloan (09-30) · Tiktok |
| 3 | Atome · Tiktok Loan · Sloan (09-08) | Billease Eikko · Sloan (09-08) · Tiktok Loan · Atome · Gloan (09-16) · Sloan (09-14) |
| 4 | Sloan (09-14) · Billease Eikko | Gloan (09-24) · Billease Cristy · Sloan (09-11) |
| 5 | — | Gloan (09-09) · Home Credit Card |
| 6 | Sloan (09-11) · Billease Cristy · Gloan (09-16) | **Spaylater** |
| 8 | Gloan (09-24) | — |
| 9 | **HomeCredit (Laptop)** · **Spaylater** · Home Credit Card · Gloan (09-09) | **HomeCredit (Laptop)** |

**What the comparison actually shows:** since the end date is identical, the only real difference is the shape of the middle. **Snowball clears 15 of 16 debts by month 6**, leaving only the laptop — fewer due dates to track, fewer ways to miss a payment. Avalanche leaves four debts running into month 9 with no compensating benefit, because the interest saving that normally justifies it **cannot be calculated without rate data**.

On these numbers, as pure arithmetic, snowball is the less error-prone schedule. **That is an observation about the arithmetic, not advice** — and it would likely change if interest rates were recorded, since ₱156,660 sitting for 9 months could easily accrue more than the ordering saves.

---

## Caveats that matter more than the model

1. **The ₱38,806 pool is not free cash.** It sits inside ₱49,806 of total monthly obligations, against August income of ₱37,590 recorded (₱54,570 at the verified figure). The model assumes the pool is paid every month; the cash-flow report shows that is not obviously affordable. **Read `Cash Flow - Rolling 60 Day.md` alongside this.**
2. **Maintain `Total Amount Paid`.** One row of 19 is populated. Filling the rest is the difference between a ceiling and a forecast — and it is the single change that would make this report actually predictive.
3. **Record interest rates.** Without them, "avalanche" is a guess wearing the name of an optimisation.
4. **Five rows share the names `Sloan`/`Gloan`** with different amounts and due dates. They are distinct debts, distinguished here by due date. Do not merge them in any migration or dedup pass.
