> This is a snippets file for TDS ROE.

## Note:

Although an initiative by Ritwik Trivedi, this repo is a common resource. Please feel free to add to it via PRs. Hopefully it helps reduce the complexity of the Remote Online Exam. Thanks also to the TAs which inspired us to create such a resource.

# Key steps:

- Activate venv using:

```CMD
source .venv/bin/activate
```

- Install dependencies from the requirements.txt file.

```CMD
pip install -r requirements.txt
```

> **Note:** Main focus is speed.

# Notes on Extraction

- [PDF Extraction](#pdf)
- [db_to_csv.py](./db_to_csv.py) (direct link to file)

## PDF:

https://www.adobe.com/in/acrobat/online/pdf-to-excel.html

- After conversion handle page breakpoints (last row on every page may get split in two). Delete the extra row for this.
- Then copy the entire content in a new sheet and paste as values. (this helps is converting to csv.)

Alternative: [pdf_to_excel.py](./pdf_to_excel.py)

## Parsing HTML
