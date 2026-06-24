from flask import Blueprint, request, jsonify

ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/generate", methods=["POST"])
def generate():
    topic = request.json["topic"]

    return jsonify({
        "topic": topic,
        "lesson": f"Explicación profesional de {topic}",
        "questions": [
            f"Define {topic}",
            f"Ejemplo de {topic}",
            f"Aplicación de {topic}"
        ]
    })