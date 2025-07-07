import sqlite3
import os

DB_PATH = "backend/siem.db"

def init_db():
    os.makedirs("backend", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_logs(logs):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for log in logs:
        cursor.execute('''
            INSERT INTO logs (timestamp, event_type, description)
            VALUES (?, ?, ?)
        ''', (log["timestamp"], log["event_type"], log["description"]))

    conn.commit()
    conn.close()
