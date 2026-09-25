import pandas as pd
from pathlib import Path

# Load raw dataset
file_path = Path("Week_2/data/raw/stock_market_raw.csv")
df = pd.read_csv(file_path)

print("=" * 60)
print("RAW DATASET QUALITY ASSESSMENT")
print("=" * 60)

print("\n1. DATASET DIMENSIONS")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n2. COLUMN DATA TYPES")
print(df.dtypes)

print("\n3. MISSING VALUES")
print(df.isnull().sum())

print("\n4. DUPLICATE RECORDS")
print("Duplicate rows:", df.duplicated().sum())

print("\n5. UNIQUE VALUES PER COLUMN")
print(df.nunique())

print("\n6. NUMERIC SUMMARY")
print(df.describe())

print("\n7. SAMPLE OF POTENTIAL INVALID VALUES")
for column in ["Date", "Open", "High", "Low", "Close", "Volume"]:
    print(f"\n{column}:")
    print(df[column].astype(str).value_counts().head(5))

print("\nAssessment completed.")
