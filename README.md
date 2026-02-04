# DataScienceProject
## Summary & Strategy Recommendations

# Hyperliquid Sentiment Analysis Project

## Project Goal
Analyze how market sentiment (Fear/Greed) relates to trader behavior and performance on Hyperliquid to uncover patterns for smarter trading.

## Structure
- `dataScienceProject.ipynb`: The main data processing and analysis notebook.
- `Readme.md`: Key insights and strategic recommendations.

## Key Findings
- Market sentiment significantly impacts win rates, with Extreme Greed showing the highest success ($58.7\%$).
- High-leverage traders experience extreme volatility during Fear cycles.
- Frequent trading in Greed environments yields higher median PnL but requires strict risk management.

# Trading Behavior & Sentiment Summary

## Insights

### 1. The Leverage Trap in Fearful Markets
High-risk/size traders show massive PnL volatility during "Fear" days. While they occasionally hit big wins, the standard deviation of their PnL is over $130x$ higher than low-risk traders ($304,757$ vs $2,339$).
- **Evidence**: See `charts/insight1_volatility.png`.
- **Table**:
| Risk Bucket | Avg Win Rate | PnL Volatility |
|-------------|--------------|----------------|
| Low Risk    | 33.9%        | 2,339          |
| High Risk   | 45.9%        | 304,757        |

### 2. Frequency Alpha in Greed
During Greed phases, frequent traders maintain a significantly higher median PnL ($670$) compared to infrequent traders ($5.3$). This suggests that momentum-based high-frequency strategies are more effective when the market sentiment is bullish.
- **Evidence**: See `charts/insight2_median_pnl.png`.

### 3. Consistency vs. Market Noise
Consistent traders (those with low PnL variance per coin) maintain positive PnL across almost all sentiment categories, whereas Inconsistent traders suffer from wild swings, especially in "Fear" and "Greed" where their PnL volatility explodes.
- **Evidence**: See `charts/insight3_consistency.png`.

## Strategy Recommendations

### Rule 1: The "Neutral" Filter
Since win rates drop to their lowest ($20.2\%$) during Neutral sentiment phases, the strategy should be to **halve trade size or sit out** until the Fear/Greed index moves into a trend-defining zone.

### Rule 2: Dynamic Leverage Scaling
During "Fear" phases, **cap maximum trade size** at 25% of the standard "Greed" allocation. The data shows that while win rates are decent in Fear, the risk of catastrophic PnL volatility makes high leverage mathematically unsustainable.


