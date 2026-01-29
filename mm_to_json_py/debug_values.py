
import sys
from access_parser import AccessParser
import pandas as pd

# Mocking the sanitization logic from mm_to_json.py
def load_table(db, name):
    rows = db.parse_table(name)
    if isinstance(rows, dict):
        max_len = 0
        for k, v in rows.items():
            if isinstance(v, list):
                max_len = max(max_len, len(v))
        for k, v in rows.items():
            if isinstance(v, list) and len(v) < max_len:
                rows[k] = v + [None] * (max_len - len(v))
        return pd.DataFrame(rows)
    return pd.DataFrame()

db = AccessParser(sys.argv[1])

print("\n--- ENTRY ---")
df_entry = load_table(db, "ENTRY")
print(f"Columns: {list(df_entry.columns)}")
if not df_entry.empty:
    print("First 3 rows:")
    print(df_entry.head(3).to_string())
