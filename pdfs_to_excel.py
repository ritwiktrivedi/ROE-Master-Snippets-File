import pandas as pd
import pdfplumber
import os

# Get all PDF files in the directory
directory_path = './mock4/mock_roe_4/'
pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]

dfs = []
for filename in pdf_files:
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:  # Check if a table is found
                    if not dfs:
                        df = pd.DataFrame(table[1:], columns=table[0])  # Set the header row as column names
                    else:
                        df = pd.DataFrame(table[1:])  # Exclude the header row
                    dfs.append(df)
    else:
        print(f"File not found: {file_path}")

# Concatenate all DataFrames into a single one
df_all = pd.concat(dfs, ignore_index=True)

# Save the DataFrame to an Excel file
output_directory = './processed_files/'
os.makedirs(output_directory, exist_ok=True)
df_all.to_excel(os.path.join(output_directory, 'all_tables.xlsx'), index=False)

