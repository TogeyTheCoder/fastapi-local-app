table1 = """
CREATE TABLE IF NOT EXISTS
stores(
    store_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    store_name TEXT UNIQUE,
    location TEXT, 
    unique_id TEXT UNIQUE
)
"""

cmd1 = """
        INSERT INTO stores
        (store_name, location, unique_id)
        VALUES (?, ?, ?)
    """