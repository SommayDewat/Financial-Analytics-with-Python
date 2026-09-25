import pandas as pd
import numpy as np
from pathlib import Path

# Reproducible simulated financial dataset
np.random.seed(42)

# Output location
output_path = Path("Week_2/data/raw/stock_market_raw.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Generate 500 business days
dates = pd.bdate_range(start="2024-01-01", periods=500)

# Generate simulated stock prices
close_prices = 100 + np.cumsum(np.random.normal(0.1, 1.5, len(dates)))
open_prices = close_prices + np.random.normal(0, 1, len(dates))

high_prices = np.maximum(open_prices, close_prices) + np.random.uniform(0.1, 2, len(dates))
low_prices = np.minimum(open_prices, close_prices) - np.random.uniform(0.1, 2, len(dates))

volumes = np.random.randint(10000, 500000, len(dates))

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Open": open_prices.round(2),
    "High": high_prices.round(2),
    "Low": low_prices.round(2),
    "Close": close_prices.round(2),
    "Volume": volumes
})

# Introduce controlled data quality issues
df.loc[5, "Close"] = np.nan
df.loc[12, "Volume"] = np.nan
df.loc[20, "Open"] = "N/A"
df.loc[30, "Date"] = "not_a_date"
df.loc[40, "Volume"] = -500
df.loc[50, "High"] = df.loc[50, "Low"] - 5
df.loc[60, "Close"] = "invalid"
df.loc[70, "Open"] = np.nan

# Add duplicate records
df = pd.concat([df, df.iloc[[10, 25, 35]]], ignore_index=True)

# Add inconsistent date formatting
df.loc[80, "Date"] = pd.to_datetime(df.loc[80, "Date"]).strftime("%d-%m-%Y")

# Save raw dataset
df.to_csv(output_path, index=False)

print("Raw dataset created successfully!")
print(f"File: {output_path}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
