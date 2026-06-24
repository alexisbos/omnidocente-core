from flask import Blueprint, request, jsonify
import sqlite3

api_blueprint = Blueprint("api", __name__)

DB_PATH = "data/lms.db"


def conn():
    return sqlite3.connect(DB_PATH)


@api_blueprint.route("/student", methods=["POST"])
def create_student():
    data = request.json

    c = conn().cursor()
    c.execute(
        "INSERT OR IGNORE INTO students (username, xp, level) VALUES (?, 0, 1)",
        (data["username"],)
    )
    conn().commit()

    return jsonify({"status": "created"})


@api_blueprint.route("/xp", methods=["POST"])
def add_xp():
    data = request.json

    c = conn().cursor()
    c.execute("SELECT xp FROM students WHERE username=?", (data["username"],))
    row = c.fetchone()

    xp = row[0] + data.get("xp", 10)
    level = (xp // 100) + 1

    c.execute(
        "UPDATE students SET xp=?, level=? WHERE username=?",
        (xp, level, data["username"])
    )

    conn().commit()

    return jsonify({"xp": xp, "level": level})


@api_blueprint.route("/leaderboard", methods=["GET"])
def leaderboard():
    c = conn().cursor()
    c.execute("SELECT username, xp, level FROM students ORDER BY xp DESC")

    return jsonify(c.fetchall())


@api_blueprint.route("/grades", methods=["POST"])
def save_grade():
    data = request.json

    c = conn().cursor()
    c.execute(
        "INSERT INTO grades (username, exam, score) VALUES (?, ?, ?)",
        (data["username"], data["exam"], data["score"])
    )

    conn().commit()

    return jsonify({"status": "saved"})