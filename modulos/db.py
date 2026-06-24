import sqlite3
from config import Config
import os

def get_conn():
    if not os.path.exists("data"):
        os.makedirs("data")
    return sqlite3.connect(Config.DB_PATH)


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        xp INTEGER,
        level INTEGER
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        exam TEXT,
        score REAL
    )""")

    conn.commit()
    conn.close()