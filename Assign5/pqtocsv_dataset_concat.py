
import pandas as pd
import os

data_dir = './taxi'
months = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

file_name = 'yellow_tripdata_2024-01.csv'
file_path = os.path.join(data_dir, file_name)

concatenated_data = pd.read_parquet(file_path)

for month in months:
    file_name = f'yellow_tripdata_2023-{month}.csv'
    file_path = os.path.join(data_dir, file_name)
    
    if os.path.exists(file_path):
        data = pd.read_parquet(file_path)
        concatenated_data = pd.concat([concatenated_data, data], ignore_index=True)
    else:
        print(f"File {file_name} not found.")

output_file = './taxi/yellow_tripdata_2023_feb_to_dec_2024_jan.csv'
concatenated_data.to_csv(output_file, index=False)

print(f'Concatenated data saved to {output_file}')