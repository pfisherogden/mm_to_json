
import sys
from access_parser import AccessParser
import pandas as pd

mdb_path = sys.argv[1]
db = AccessParser(mdb_path)

print("Attempting to parse SESSIONS table raw...")
try:
    # Try to access internal structure if public API fails
    # Or just print catalog info
    print("Catalog info for SESSIONS:")
    print(db.catalog.get('SESSIONS'))
    
    rows = db.parse_table('SESSIONS')
    print(f"Successfully parsed {len(rows)} rows.")
    print("Columns:", rows[0].keys() if rows else "No rows")
except Exception as e:
    print(f"Error parsing SESSIONS: {e}")
    import traceback
    traceback.print_exc()
