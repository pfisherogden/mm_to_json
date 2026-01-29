
import sys
from access_parser import AccessParser
import pandas as pd

def load_table(db, name):
    rows = db.parse_table(name)
    if isinstance(rows, dict):
        max_len = 0
        for k, v in rows.items():
            if isinstance(v, list):
                max_len = max(max_len, len(v))
        for k, v in rows.items():
            if isinstance(v, list) and len(v) < max_len:
                rows[k] = v + [None] * (max_len - len(v))
        return pd.DataFrame(rows)
    return pd.DataFrame()

db = AccessParser(sys.argv[1])
df_evt = load_table(db, "MTEVENT")
df_entry = load_table(db, "ENTRY") # Restoring
print(f"Events: {len(df_evt)}, Entries: {len(df_entry)}")

if not df_evt.empty and not df_entry.empty:
    ev_ids = set(df_evt['MtEv'].dropna().astype(int).unique())
    en_ids = set(df_entry['MtEvent'].dropna().astype(int).unique())
    
    intersect = ev_ids.intersection(en_ids)
    print(f"Intersection MTEVENT.MtEv <-> ENTRY.MtEvent: {len(intersect)}")
    if len(intersect) > 0:
        print(f"Sample matches: {list(intersect)[:5]}")
    else:
        print(f"Sample Ev IDs: {sorted(list(ev_ids))[:5]}")
        print(f"Sample En IDs: {sorted(list(en_ids))[:5]}")
        
    # Check if MtEvent matches?
    ev_num_ids = set(df_evt['MtEvent'].dropna().astype(int).unique())
    intersect2 = ev_num_ids.intersection(en_ids)
    print(f"Intersection MTEVENT.MtEvent <-> ENTRY.MtEvent: {len(intersect2)}")
