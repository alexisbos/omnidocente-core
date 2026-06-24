from flask import Blueprint, request, jsonify
import sqlite3
import os

auth_blueprint = Blueprint("auth", __name__)

DB_PATH = "data/lms.db"


def conn():
    return sqlite3.connect(DB_PATH)


@auth_blueprint.route("/register", methods=["POST"])
def register():
    data = request.json

    c = conn().cursor()
    try:
        c.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (data["username"], data["password"], data.get("role", "student"))
        )
        conn().commit()
    except:
        return jsonify({"error": "user exists"})

    return jsonify({"status": "ok"})


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json

    c = conn().cursor()
    c.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (data["username"], data["password"])
    )

    user = c.fetchone()

    if not user:
        return jsonify({"status": "error"})

    return jsonify({
        "status": "ok",
        "role": user[0],
        "token": f"TOKEN-{data['username']}"
    })