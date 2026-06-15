import sqlite3

DB_PATH = "/data/db.sqlite"


def init_db():
    """Creates the guilds table with an auto-incrementing key."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guilds (
                key INTEGER PRIMARY KEY AUTOINCREMENT,
                server_id INTEGER UNIQUE
            )
        """)
        conn.commit()


def add_guild(server_id: int):
    """Inserts a server ID. 'OR IGNORE' handles existing servers smoothly."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO guilds (server_id) VALUES (?)", (server_id,)
        )
        conn.commit()
