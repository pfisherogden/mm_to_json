
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "MEET"

print(f"Parsing {tbl_name}...")
res = db.parse_table(tbl_name)
print(f"Type of result: {type(res)}")
if hasattr(res, '__iter__'):
    print("Result is iterable.")
    try:
        first = next(iter(res))
        print(f"First item: {first} (Type: {type(first)})")
    except StopIteration:
        print("Result is empty.")
print(f"Result length: {len(res) if hasattr(res, '__len__') else 'Unknown'}")
