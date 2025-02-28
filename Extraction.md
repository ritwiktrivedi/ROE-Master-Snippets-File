Main focus is speed.

- [PDF Extraction](#PDF)
- [.db to csv](#load-data-from-db-file)

# PDF:

https://www.adobe.com/in/acrobat/online/pdf-to-excel.html

- After conversion handle page breakpoints (last row on every page may get split in two). Delete the extra row for this.
- Then copy the entire content in a new sheet and paste as values. (this helps is converting to csv.)

Alternative: [pdf_to_excel.py](./pdf_to_excel.py)

# Load data from .db file

[db_to_csv.py](./db_to_csv.py)
