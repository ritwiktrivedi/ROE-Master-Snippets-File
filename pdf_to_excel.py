import pandas as pd
import pdfplumber
import os

# Define file paths
pdf_path = './files/W1.pdf'
output_directory = './processed_files/'
output_file = os.path.join(output_directory, 'w1.xlsx')

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

data = []
headers = None  # Store headers to maintain consistency

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        table = page.extract_table()
        if table:
            if headers is None:  # Set headers from the first page
                headers = table[0]
            data.extend(table[1:])  # Append data (excluding headers)
            print(f"Extracted table from page {page_num}")

# Convert to DataFrame and save
if data:
    df_pdf = pd.DataFrame(data, columns=headers)  # Apply headers
    df_pdf.to_excel(output_file, index=False)
    print(f"Table saved to {output_file}")
else:
    print("No tables found in the PDF.")
