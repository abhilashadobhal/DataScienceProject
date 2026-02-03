import pandas as pd
import numpy as np

# Load datasets

df1 = pd.read_csv(r'C:\Users\Monu\OneDrive\Apps\Desktop\fear_greed_index.csv')
df2 = pd.read_csv(r'C:\Users\Monu\OneDrive\Apps\Desktop\historical_data.csv')
print(df1)
print(df2)

print(df1.info())
print(df2.info())   

# Check for missing values and duplicates
def data_summary(df1, name):
    print(f"--- {name} ---")
    print("Shape:", df1.shape)
    print("\nMissing values:\n", df1.isna().sum())
    print("\nDuplicates:", df1.duplicated().sum())

data_summary(df1, "Fear & Greed Index")
data_summary(df2, "Historical Data")

#  Convert timestamps & align by date
df1["Date"] = pd.to_datetime(df1["Date"]).dt.date

df2["time"] = pd.to_datetime(df2["time"], unit="ms")
df2["date"] = df2["time"].dt.date


df2 = df2.merge(
    df1,
    left_on="date",
    right_on="Date",
    how="left"
)

# Check Key metrics
df2["abs_size"] = df2["size"].abs()
df2["is_win"] = df2["closedPnL"] > 0
df2["is_long"] = df2["side"] == "BUY"

daily_trader = df2.groupby(
    ["date", "account", "Classification"]
).agg(
    daily_pnl=("closedPnL", "sum"),
    trades_count=("closedPnL", "count"),
    win_rate=("is_win", "mean"),
    avg_trade_size=("abs_size", "mean"),
    avg_leverage=("leverage", "mean"),
    long_ratio=("is_long", "mean")
).reset_index()


# Data Analysis
# Does performance differ between Fear vs Greed?

performance_by_sentiment = daily_trader.groupby("Classification").agg(
    avg_pnl=("daily_pnl", "mean"),
    median_pnl=("daily_pnl", "median"),
    avg_win_rate=("win_rate", "mean"),
    pnl_volatility=("daily_pnl", "std")
)

# Do traders change behavior based on sentiment?
behavior_by_sentiment = daily_trader.groupby("Classification").agg(
    avg_trades_per_day=("trades_count", "mean"),
    avg_leverage=("avg_leverage", "mean"),
    avg_trade_size=("avg_trade_size", "mean"),
    avg_long_ratio=("long_ratio", "mean")
)

# Identify 2–3 trader segments
#Segment 1: High vs Low leverage
daily_trader["leverage_bucket"] = pd.qcut(
    daily_trader["avg_leverage"], q=2, labels=["Low", "High"]
)

#Segment 2: Frequent vs Infrequent traders
daily_trader["frequency_bucket"] = pd.qcut(
    daily_trader["trades_count"], q=2, labels=["Infrequent", "Frequent"]
)

#Segment 3: Consistency in performance
consistency = daily_trader.groupby("account")["daily_pnl"].std()
daily_trader = daily_trader.merge(
    consistency.rename("pnl_std"), on="account"
)

daily_trader["consistency_bucket"] = pd.qcut(
    daily_trader["pnl_std"], q=2, labels=["Consistent", "Inconsistent"]
)
