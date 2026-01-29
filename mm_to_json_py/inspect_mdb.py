import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
print("Tables found:")
for t in db.catalog:
    print(f" - {t}")
