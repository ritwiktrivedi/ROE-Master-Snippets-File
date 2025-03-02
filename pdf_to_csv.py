import tabula
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help="name of th pdf file")
args = parser.parse_args()
# Read PDF File
# this contain a list
df = tabula.read_pdf(args.file, pages=1)[0]

# Convert into Excel File
df.to_csv(f"./processed_files/{args.file.split('.')[0]}.csv")
