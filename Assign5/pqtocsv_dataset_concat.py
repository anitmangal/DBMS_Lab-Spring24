import pandas as pd
import os
import random

import pandas as pd

def check_columns_equal(df1, df2,month):
    # Get the column names of each DataFrame
    df1_columns = df1.columns.tolist()
    df2_columns = df2.columns.tolist()

    # Check if the column names and order are equal
    if df1_columns == df2_columns:
        print(f"The columns of both DataFrames are the same and in the same order for month : {month}")
    else:
        print(f"The columns of the DataFrames are either different or not in the same order for month : {month}")



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
        
        check_columns_equal(data,concatenated_data,month)
        
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

concatenated_data['tpep_dropoff_datetime'] = concatenated_data['tpep_dropoff_datetime'].dt.strftime('%Y-%m-%d/%H:%M:%S')
concatenated_data['tpep_pickup_datetime'] = concatenated_data['tpep_pickup_datetime'].dt.strftime('%Y-%m-%d/%H:%M:%S')

print(concatenated_data.head(5))

concatenated_data.to_csv(output_file, index=False)

for column_name in concatenated_data.columns:
    print(column_name)
    
print(f'Concatenated data (10% sampled) saved to {output_file}')
