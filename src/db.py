import sqlite3

DB_PATH = "/data/db.sqlite"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.close()
