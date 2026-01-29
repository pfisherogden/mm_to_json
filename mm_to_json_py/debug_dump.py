
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
print("Dumping database to stdout...")
# This method usually prints schema and data
db.print_database()
