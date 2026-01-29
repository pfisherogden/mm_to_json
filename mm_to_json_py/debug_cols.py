
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])
tbl_name = "ENTRY"
if tbl_name in db.catalog:
    table_def = db.get_table(tbl_name)
    print(f"Table Def for {tbl_name}: {table_def}")
    if hasattr(table_def, 'columns'):
        print(f"Columns type: {type(table_def.columns)}")
    if hasattr(table_def, 'columns'):
        cols = sorted(list(table_def.columns.values()), key=lambda x: x.column_index)
        col_names = [c.col_name_str for c in cols]
        print(f"All Columns: {col_names}")
else:
    print(f"{tbl_name} not found")
