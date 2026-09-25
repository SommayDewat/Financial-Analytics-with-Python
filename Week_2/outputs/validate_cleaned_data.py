import pandas as pd
from pathlib import Path

file_path = Path("Week_2/data/cleaned/stock_market_cleaned.csv")
df = pd.read_csv(file_path)

print("=" * 60)
print("FINAL CLEANED DATASET VALIDATION")
print("=" * 60)

print("\n1. Dataset Shape:", df.shape)

print("\n2. Duplicate Records:", df.duplicated().sum())

print("\n3. Missing Values:")
print(df.isna().sum())

print("\n4. Negative Volume Records:", (df["Volume"] < 0).sum())

print("\n5. Invalid OHLC Records:")

invalid_ohlc = (
    (df["High"] < df[["Open", "Close", "Low"]].max(axis=1)) |
    (df["Low"] > df[["Open", "Close", "High"]].min(axis=1))
)

print("Count:", invalid_ohlc.sum())

print("\n6. Date Range:")
print("Start Date:", df["Date"].min())
print("End Date:", df["Date"].max())

print("\n7. Numeric Summary:")
print(df[["Open", "High", "Low", "Close", "Volume"]].describe())

print("\n8. Final Validation Status:")
if (
    df.duplicated().sum() == 0
    and df[["Date", "Open", "High", "Low", "Close", "Volume"]].isna().sum().sum() == 0
    and (df["Volume"] < 0).sum() == 0
    and invalid_ohlc.sum() == 0
):
    print("PASS: Dataset passed all core quality checks.")
else:
    print("CHECK REQUIRED: Some quality issues remain.")

print("\nValidation completed.")
