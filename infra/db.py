import sqlite3
from config import Config
from core.models import Student
import os


def conn():
    if not os.path.exists("data"):
        os.makedirs("data")
    return sqlite3.connect(Config.DB_PATH)


def init_db():
    c = conn().cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        username TEXT PRIMARY KEY,
        xp INTEGER,
        level INTEGER
    )
    """)

    conn().commit()
    conn().close()


def get_student(username):
    c = conn().cursor()
    c.execute("SELECT username, xp, level FROM students WHERE username=?", (username,))
    row = c.fetchone()

    if not row:
        return None

    return Student(username=row[0], xp=row[1], level=row[2])


def save_student(student):
    c = conn().cursor()

    c.execute("""
    INSERT INTO students (username, xp, level)
    VALUES (?, ?, ?)
    ON CONFLICT(username) DO UPDATE SET
        xp=excluded.xp,
        level=excluded.level
    """, (student.username, student.xp, student.level))

    conn().commit()
    conn().close()