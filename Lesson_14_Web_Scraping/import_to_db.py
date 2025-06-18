


import os
import sqlite3
import pandas as pd

# Configuration
csv_folder = "./csv_data"  
database_file = "oldest_living_players_cleaned.csv"

# Create/connect to SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Helper function to infer SQLite types from pandas types
def infer_sqlite_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "REAL"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TEXT" 
    else:
        return "TEXT"

# Loop through all CSV files in the folder
for filename in os.listdir(csv_folder):
    print(filename)
    if filename.endswith(".csv"):
        try:
            table_name = os.path.splitext(filename)[0]
            file_path = os.path.join(csv_folder, filename)
            print(f"Importing {file_path} as table `{table_name}`...")

            # Load CSV into DataFrame
            df = pd.read_csv(file_path)

            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors="ignore")
                except:
                    pass

            # Build CREATE TABLE statement
            columns_with_types = [
                f'"{col}" {infer_sqlite_type(df[col])}' for col in df.columns
            ]
            create_stmt = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(columns_with_types)});'
            cursor.execute(create_stmt)

            # Insert data
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Successfully imported `{table_name}` ({len(df)} rows).")

        except Exception as e:
            print(f"Failed to import {filename}: {e}")

# Close connection
conn.close()
print("\nAll done.")


