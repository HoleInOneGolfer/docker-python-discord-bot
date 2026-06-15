import sqlite3

def init_db(DB_PATH):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS guilds (guild_id INTEGER PRIMARY KEY,guild_name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def save_guild(DB_PATH, guild_id, guild_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO guilds (guild_id, guild_name)VALUES (?, ?)ON CONFLICT(guild_id) DO UPDATE SET guild_name = excluded.guild_name''', (guild_id, guild_name))
    conn.commit()
    conn.close()
