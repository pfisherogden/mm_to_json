
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
# Check just one table to see schema format
tbl_name = "MEET"
if tbl_name in db.catalog:
    print(f"Schema for {tbl_name}:")
    # catalog[tbl_name] is usually a dict or object with schema info
    schema = db.catalog[tbl_name]
    print(schema)
else:
    print(f"{tbl_name} not found")
