
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "MEET"

print(f"Parsing {tbl_name}...")
rows = db.parse_table(tbl_name)
print(f"Total Rows: {len(rows)}")

# Count non-empty rows
valid_rows = [r for r in rows if r]
print(f"Non-empty Rows: {len(valid_rows)}")

if valid_rows:
    print(f"First valid row: {valid_rows[0]}")
    print(f"Type: {type(valid_rows[0])}")
else:
    print("All rows are empty lists?!")
