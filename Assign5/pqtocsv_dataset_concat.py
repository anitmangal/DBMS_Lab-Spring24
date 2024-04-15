import pandas as pd
import os
import random

data_dir = './taxi'
months = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

concatenated_data = pd.DataFrame()

for month in months:
    file_name = f'yellow_tripdata_2023-{month}.parquet'
    file_path = os.path.join(data_dir, file_name)
    
    if os.path.exists(file_path):
        data = pd.read_parquet(file_path)
        
        num_samples = int(len(data) * 0.1)
        sampled_data = data.sample(n=num_samples, random_state=42)
        
        concatenated_data = pd.concat([concatenated_data, sampled_data], ignore_index=True)
    else:
        print(f"File {file_name} not found.")
        
    print(f"Concatenating data for month {month}")

file_name = 'yellow_tripdata_2024-01.parquet'
file_path = os.path.join(data_dir, file_name)

if os.path.exists(file_path):
    data = pd.read_parquet(file_path)
    num_samples = int(len(data) * 0.1)
    sampled_data = data.sample(n=num_samples, random_state=42)
    
    concatenated_data = pd.concat([concatenated_data, sampled_data], ignore_index=True)
else:
    print(f"File {file_name} not found.")
    
print(f"Concatenating data for month 01")
    
output_file = './taxi/yellow_tripdata_2023_feb_to_dec_2024_jan_10percent.csv'
concatenated_data.to_csv(output_file, index=False)

print(f'Concatenated data (10% sampled) saved to {output_file}')
