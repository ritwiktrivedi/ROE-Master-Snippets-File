import sqlite3
import duckdb
import pandas as pd
from google.colab import files
import io

# 📌 Step 1: Upload the database file
uploaded = files.upload()
db_file = list(uploaded.keys())[0]  # Get uploaded filename

# 📌 Step 2: Function to Convert DB to Excel
def convert_db_to_excel(db_file):
    """
    Converts an uploaded SQLite or DuckDB database into an Excel file.
    Each table in the database is saved as a separate sheet in the Excel file.
    """
    db_extension = db_file.split(".")[-1]
    
    # Connect to the correct database type
    if db_extension == "db":
        conn = sqlite3.connect(db_file)
        query = "SELECT name FROM sqlite_master WHERE type='table';"
    elif db_extension == "duckdb":
        conn = duckdb.connect(db_file)
        query = "SHOW TABLES;"
    else:
        print("❌ Unsupported database format. Please upload a .db (SQLite) or .duckdb (DuckDB) file.")
        return

    # Fetch all table names
    tables = pd.read_sql(query, conn)

    # Use in-memory Excel file
    excel_buffer = io.BytesIO()

    # Write to Excel file
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        for table in tables.iloc[:, 0]:  # Extract table names
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            df.to_excel(writer, sheet_name=table, index=False)

    conn.close()

    # Save the file for download
    excel_buffer.seek(0)
    with open("converted_database.xlsx", "wb") as f:
        f.write(excel_buffer.read())

    print("✅ Database successfully converted to converted_database.xlsx")

# 📌 Step 3: Run the function
convert_db_to_excel(db_file)

# 📌 Step 4: Download the Excel file
files.download("converted_database.xlsx")