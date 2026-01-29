
import sys
from access_parser import AccessParser

db = AccessParser(sys.argv[1])

# print specific table info
target_tables = ["CUSTOMRPTS", "Batches", "Memos", "Reports"] # Guesses

# inspect internal table defs
defs = getattr(db, "_table_defs", {}) or {} # fallback

interesting = ["CUSTOMRPTS", "RECNAME", "RECORDS", "STDNAME", "MemSets", "MemCirSets"]

# catalog maps Name -> ID
# Force parse to ensure defs are loaded (access_parser loads lazily?)
interesting = ["CUSTOMRPTS", "RECNAME", "RECORDS", "STDNAME", "MemSets", "MemCirSets"]
for n in interesting:
    try:
        db.parse_table(n)
    except: pass

# inspect internal table defs again
defs = getattr(db, "_table_defs", {}) or {} # refresh ref


for name in interesting:
    # Find ID from catalog
    # catalog keys are string names
    # values are the IDs
    
    table_id = None
    for k, v in db.catalog.items():
        if k.lower() == name.lower():
            table_id = v
            break
            
    if table_id is not None:
         if table_id in defs:
             t_def = defs[table_id]
             print(f"\nTable: {name}")
             try:
                 print(f"Columns: {[c.name for c in t_def.columns]}")
             except:
                 print("Error printing columns")
         else:
             print(f"\nTable: {name} ID {table_id} not in _table_defs")
    else:
        print(f"\nTable: {name} not found in catalog")




        
print("\n--- Listing All Table Names for Context ---")
print(sorted(db.catalog.keys()))
