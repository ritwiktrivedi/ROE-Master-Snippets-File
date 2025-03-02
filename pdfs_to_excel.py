import pandas as pd
import pdfplumber
import os

# Define paths
directory_path = './mock4/mock_roe_4/'
output_directory = './processed_files/'
os.makedirs(output_directory, exist_ok=True)

# Get all PDF files in the directory
pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]

dfs = []
for filename in pdf_files:
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path):
        print(f"Processing: {filename}")  # Logging current file
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                table = page.extract_table()
                if table:  # Ensure a table is found
                    # Set headers from first row
                    df = pd.DataFrame(table[1:], columns=table[0])
                    dfs.append(df)
                    print(f"Extracted table from {filename}, Page {page_num}")
    else:
        print(f"File not found: {file_path}")

# Check if any tables were extracted before concatenation
if dfs:
    df_all = pd.concat(dfs, ignore_index=True)
    output_file = os.path.join(output_directory, 'all_tables.xlsx')
    df_all.to_excel(output_file, index=False)
    print(f"Tables saved to {output_file}")
else:
    print("No tables extracted from PDFs.")
