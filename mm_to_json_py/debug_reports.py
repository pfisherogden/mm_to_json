
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
candidates = ["CUSTOMRPTS", "JOURNAL", "MEMSETS", "BATCH"]

print(f"Checking candidates: {candidates}")
for tbl in candidates:
    if tbl in db.catalog:
        print(f"\nScanning {tbl}...")
        try:
             # Just get columns and a few rows
             table_def = db.get_table(tbl)
             cols = []
             if hasattr(table_def, 'columns'):
                 cols = sorted(list(table_def.columns.values()), key=lambda x: x.column_index)
                 col_names = [c.col_name_str for c in cols]
                 print(f"Columns: {col_names}")
                 
             rows = db.parse_table(tbl)
             if isinstance(rows, dict):
                 # Print first few items of first few columns
                 keys = list(rows.keys())
                 if keys:
                     print(f"Row count: {len(rows[keys[0]])}")
                     # Print sample data from first row
                     sample = {k: rows[k][0] if rows[k] else None for k in keys[:5]}
                     print(f"Sample Row 0: {sample}")
             elif isinstance(rows, list):
                 print(f"Row count: {len(rows)}")
                 if rows: print(f"Sample: {rows[0]}")
        except Exception as e:
            print(f"Error reading {tbl}: {e}")
    else:
        print(f"{tbl} not found.")
