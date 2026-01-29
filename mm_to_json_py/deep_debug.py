
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "MEET"
print(f"Introspecting access-parser for table {tbl_name}...")

# Inspect private attributes
print("DB Attributes:", dir(db))

# Try to find table definition
if hasattr(db, 'table_defs'):
    print("Found table_defs!")
    # likely a dict of offset -> def, or name -> def
    # Let's see keys
    # print(db.table_defs.keys()) 
    pass

# Try checking what ParseTable actually does. 
# It usually reads TDEF page. 
# We might need to access the TableDefinition object.

# If db.catalog maps name -> page_offset (int 204), 
# then maybe we need to parse that page to get columns.
# BUT parse_table(name) returns data.
# Is there a function parse_table_schema(name)?

# Let's inspect what parse_table calls or returns if we use a private method?
# Or check if we can get the columns from a parsed table object?

# Actually, let's look at the library source code if possible via inspect
import inspect
import access_parser.utils
print("Utils:", dir(access_parser.utils))

# Try to read the Table Definition manually if the library exposes it
# access_parser usually has parse_table method.
# Let's simply print the first few lines of `db.parse_table` source to see how it gets columns
# print(inspect.getsource(db.parse_table))

# Wait, `access-parser` v0.0.6 (installed by uv) might return a dict map if configured?
# The output `values` (list of lists) implies it just dumps data.
# But it MUST know columns to parse data types. 
# It usually stores them in `table.columns`. 

# Let's try to get the Table object for MEET
# Since `db.catalog` is `name -> page_num`, maybe there is `db.get_table_def(page_num)`? or `db.parse_table_page`?

# Let's brute force search for 'column' in dir(db)
print([x for x in dir(db) if 'col' in x.lower() or 'tab' in x.lower()])
