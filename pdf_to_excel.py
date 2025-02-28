import pandas as pd
import pdfplumber

# Extract table from PDF
pdf_path = './files/W1.pdf'
data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            data.extend(tables)

# Convert to DataFrame and save
df_pdf = pd.DataFrame(data)
df_pdf.to_excel('./processed_files/w1.xlsx', index=False)