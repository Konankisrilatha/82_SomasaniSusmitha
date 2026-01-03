import sqlite3

def get_db():
    conn = sqlite3.connect("tickets.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint TEXT,
            category TEXT,
            sentiment TEXT,
            priority TEXT
        )
    """)
    return conn
