import pandas as pd
import pdfplumber
import os

# Get all PDF files in the directory
pdf_files = [f for f in os.listdir('./mock_roe_4') if f.endswith('.pdf')]

dfs = []
for i in pdf_files:
    with pdfplumber.open(f"./mock_roe_4/{i}") as pdf:
        for i, page in enumerate(pdf.pages):
            table = page.extract_table()
            if table:  # Check if a table is found
                df = pd.DataFrame(table)  # Convert to DataFrame
                dfs.append(df)

# Concatenate all DataFrames into a single one
df_all = pd.concat(dfs, ignore_index=True)

# Save the DataFrame to an Excel file
df_all.to_excel('./processed_files/all_tables.xlsx', index=False)
