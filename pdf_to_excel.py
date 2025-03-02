import pandas as pd
import pdfplumber
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of the pdf file")
args = parser.parse_args()
# Extract table from PDF
# pdf_path = './files/W1.pdf'
pdf_path = args.file
data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            data.extend(tables)

# Convert to DataFrame and save
df_pdf = pd.DataFrame(data)
df_pdf.to_excel("./processed_files/w1.xlsx", index=False)

