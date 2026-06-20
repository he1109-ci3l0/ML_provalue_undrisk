# OilyGiant · Oil Region Selection with Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-LinearRegression-orange)
![Method](https://img.shields.io/badge/risk-Bootstrapping%20%2F%20VaR-green)

Machine learning pipeline that selects the most profitable oil region while keeping loss risk under 2.5% — Linear Regression + bootstrapping for profit & risk analysis.

## Recommendation

**Develop the 200 new wells in Region 1.** It is the only region with a loss risk below the 2.5% threshold, and it also offers the highest expected profit. Its 95% confidence interval has a positive lower bound: even in the worst reasonable scenario, the investment earns.

| Region | Avg. profit | 95% CI | Loss risk |
|---|---|---|---|
| Region 0 | $3,961,650 | [−$1.11M, $9.10M] | 6.9% |
| **Region 1** | **$4,560,451** | **[$0.34M, $8.52M]** | **1.5%** |
| Region 2 | $4,044,039 | [−$1.63M, $9.50M] | 7.6% |

## Business problem

A $100M budget funds 200 new wells in one of three regions. A linear model predicts reserve volume per well; the 200 best-predicted wells are selected; bootstrapping (1000 resamples) estimates the profit distribution, 95% confidence interval, and probability of loss for each region.

## Key findings

- The average well is below break-even (111.1k barrels) in all three regions — profit depends entirely on selecting the best wells.
- Region 1's model is near-perfect (RMSE 0.89), making its well selection reliable and its profit distribution tight and rarely negative.
- Highest single-pass profit (Region 0) is **not** the safest bet: bootstrapping reveals it loses money in 6.9% of scenarios.

## Structure
