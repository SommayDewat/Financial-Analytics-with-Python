import pandas as pd
import numpy as np
from pathlib import Path

# File paths
raw_path = Path("Week_2/data/raw/stock_market_raw.csv")
clean_path = Path("Week_2/data/cleaned/stock_market_cleaned.csv")

# Load raw dataset
df = pd.read_csv(raw_path)

print("=" * 60)
print("FINANCIAL DATA CLEANING PROCESS")
print("=" * 60)

print("\nOriginal dataset shape:", df.shape)

# 1. Remove duplicate records
before = len(df)
df = df.drop_duplicates().copy()
print("\n1. Duplicate records removed:", before - len(df))

# 2. Convert data types
df["Date"] = pd.to_datetime(
    df["Date"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)

numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 3. Remove rows with invalid dates
invalid_dates = df["Date"].isna().sum()
df = df.dropna(subset=["Date"]).copy()

print("2. Rows removed due to invalid dates:", invalid_dates)

# 4. Sort data chronologically
df = df.sort_values("Date").reset_index(drop=True)

# 5. Handle missing price values using time interpolation
price_columns = ["Open", "High", "Low", "Close"]

missing_prices_before = df[price_columns].isna().sum().sum()

df[price_columns] = df[price_columns].interpolate(
    method="linear",
    limit_direction="both"
)

print("3. Missing price values filled:", missing_prices_before)

# 6. Handle missing volume using median
missing_volume_before = df["Volume"].isna().sum()

volume_median = df.loc[df["Volume"] >= 0, "Volume"].median()
df.loc[df["Volume"].isna(), "Volume"] = volume_median

print("4. Missing volume values filled:", missing_volume_before)

# 7. Handle negative volume
negative_volume_count = (df["Volume"] < 0).sum()
df.loc[df["Volume"] < 0, "Volume"] = volume_median

print("5. Negative volume values corrected:", negative_volume_count)

# 8. Correct invalid OHLC relationships
invalid_ohlc = (
    (df["High"] < df[["Open", "Close", "Low"]].max(axis=1)) |
    (df["Low"] > df[["Open", "Close", "High"]].min(axis=1))
)

invalid_ohlc_count = invalid_ohlc.sum()

# Recalculate High and Low using available OHLC prices
df.loc[invalid_ohlc, "High"] = df.loc[
    invalid_ohlc, ["Open", "Close", "Low"]
].max(axis=1)

df.loc[invalid_ohlc, "Low"] = df.loc[
    invalid_ohlc, ["Open", "Close", "High"]
].min(axis=1)

print("6. Invalid OHLC rows corrected:", invalid_ohlc_count)

# 9. Feature engineering
df["Price_Change"] = df["Close"].diff()
df["Daily_Return_Pct"] = df["Close"].pct_change() * 100

# 10. Final validation
df = df.sort_values("Date").reset_index(drop=True)

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECK")
print("=" * 60)

print("\nFinal dataset shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())
print("\nData types:")
print(df.dtypes)

# Save cleaned dataset
clean_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(clean_path, index=False)

print("\nCleaned dataset saved to:", clean_path)
print("\nFirst 5 cleaned rows:")
print(df.head())

print("\nCleaning process completed successfully!")
