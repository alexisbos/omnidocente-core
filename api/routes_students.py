from flask import Blueprint, request, jsonify
from core.services import give_xp

students_bp = Blueprint("students", __name__)


@students_bp.route("/xp", methods=["POST"])
def add_xp():
    data = request.json

    student = give_xp(data["username"], data.get("xp", 10))

    return jsonify({
        "username": student.username,
        "xp": student.xp,
        "level": student.level
    })