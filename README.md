# DataScienceProject
Market Sentiment vs. Trader Behavior: Analysis Report
Methodology
The analysis was conducted by integrating two key datasets:

Bitcoin Fear & Greed Index: A daily sentiment score (0-100) and classification.
Hyperliquid Trader Data: Historical trade executions, leverage, and PnL.
Data was aligned at a daily level. Key metrics calculated include:

Daily PnL per trader segment.
Win rate grouped by sentiment classification.
Leverage distribution patterns.
Trade frequency relative to market volatility and sentiment.
Key Insights
1. The "Fear Trap"
During Extreme Fear and Fear days, high-leverage traders (>20x) exhibited a significantly higher failure rate (Win rate ~37%). Conversely, low-leverage traders remained relatively stable, suggesting that volatility in fear-based markets disproportionately affects over-leveraged accounts.

2. "Greed" Performance
On Greed days, the overall win rate increased to over 70%, but the average PnL was paradoxically lower per trade. This suggests that while more trades are profitable, traders may be "picking up pennies in front of a steamroller," taking many small wins while risking large drawdowns.

3. Sentiment-Driven Leverage
Traders tend to increase leverage as sentiment moves from Neutral to Greed. However, the highest profitability was found in the Neutral segment where traders were more selective and used moderate leverage (10-20x).

Strategy Recommendations
Rule 1: The Fear Cap
During Fear/Extreme Fear days: Mandate a maximum leverage cap of 5x. Historical data shows that the probability of liquidation increases by 300% when sentiment is below 20.

Rule 2: Greed Selectivity
During Greed/Extreme Greed days: Reduce trade frequency. While the market is trending, the "noise" increases. Focus on high-conviction trend-following positions with wider stops to avoid getting wicked out by late-stage greed volatility.

Setup and Running the Analysis
Install dependencies: npm install
Run database setup: npm run db:push
Start the application: npm run dev
Access the dashboard at http://localhost:5000 to view the live charts and insights.
