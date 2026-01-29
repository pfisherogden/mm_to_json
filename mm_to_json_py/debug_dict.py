
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "MEET"

print(f"Parsing {tbl_name}...")
res = db.parse_table(tbl_name)
if isinstance(res, dict):
    print("Result is a dict.")
    keys = list(res.keys())
    print(f"Keys (first 5): {keys[:5]}")
    if keys:
        first_val = res[keys[0]]
        print(f"Value type for key '{keys[0]}': {type(first_val)}")
        if isinstance(first_val, dict):
            print(f"Nested dict keys: {list(first_val.keys())[:5]}")
        elif hasattr(first_val, '__len__'):
             print(f"Value length: {len(first_val)}")
else:
    print("Result is NOT a dict.")
