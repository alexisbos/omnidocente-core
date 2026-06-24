from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    return jsonify({
        "status": "ok",
        "user": data["username"],
        "token": f"TOKEN-{data['username']}"
    })