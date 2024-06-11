import pandas as pd
import os

# Define the folder containing the CSV files relative to the script location
folder_path = os.path.join(os.path.dirname(__file__), 'Resources')

# List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty DataFrame to hold all data
combined_df = pd.DataFrame()

# Loop through each CSV file and concatenate them into a single DataFrame
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Define the row limit for sampling
row_limit = 1000000
chunk_size = 100000

# Ensure that the combined DataFrame has at least the row limit
if len(combined_df) < row_limit:
    raise ValueError(f"The combined DataFrame has fewer than {row_limit} rows")

# Randomly sample rows from the combined DataFrame
sampled_df = combined_df.sample(n=row_limit, random_state=1)

# Define the output folder path for CSV files
output_folder_path = os.path.join(os.path.dirname(__file__), 'sample_output')
os.makedirs(output_folder_path, exist_ok=True)

# Split the DataFrame into chunks of specified size and write each to a separate CSV file
num_chunks = row_limit // chunk_size

for i in range(num_chunks):
    chunk = sampled_df.iloc[i * chunk_size:(i + 1) * chunk_size]
    output_file_path = os.path.join(output_folder_path, f'sampled_output_{i + 1}.csv')
    chunk.to_csv(output_file_path, index=False)
    print(f"Sampled data chunk {i + 1} has been exported to {output_file_path}")

# If there are remaining rows that didn't fit into the even chunks
remaining_rows = row_limit % chunk_size
if remaining_rows > 0:
    chunk = sampled_df.iloc[num_chunks * chunk_size:]
    output_file_path = os.path.join(output_folder_path, f'sampled_output_{num_chunks + 1}.csv')
    chunk.to_csv(output_file_path, index=False)
    print(f"Sampled data remaining chunk has been exported to {output_file_path}")
