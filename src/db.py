import sqlite3

def init_db(DB_PATH):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    print(f"Initializing database at: {DB_PATH.resolve()}")

    conn = sqlite3.connect(DB_PATH)
    conn.close()
