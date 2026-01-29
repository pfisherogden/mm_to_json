
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "MEET"

# Manually inspect parse_table output format
print(f"Parsing {tbl_name}...")
rows = db.parse_table(tbl_name)
print(f"Row count: {len(rows)}")
if rows:
    first_row = rows[0]
    print(f"Type of first row: {type(first_row)}")
    print(f"Content of first row: {first_row}")
    
    # Check if iterating works
    try:
        for x in first_row:
            pass
        print("First row is iterable")
    except:
        print("First row is NOT iterable")
