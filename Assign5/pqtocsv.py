import pandas as pd

rootfile='taxi/yellow_tripdata_2024-01'

# Read Parquet file
parquet_file = rootfile + '.parquet'
df = pd.read_parquet(parquet_file)

# Convert to CSV
csv_file = rootfile + '.csv'
df.to_csv(csv_file, index=False)

print(f"Parquet file '{parquet_file}' has been converted to CSV file '{csv_file}'.")
