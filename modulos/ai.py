from flask import Blueprint, request, jsonify

ai_blueprint = Blueprint("ai", __name__)


def ai_engine(topic, level="medio"):
    return {
        "tema": topic,
        "explicacion": f"Explicación estructurada de {topic} nivel {level}",
        "ejemplo": f"Ejemplo aplicado de {topic}",
        "preguntas": [
            f"Define {topic}",
            f"Explica su uso",
            f"Da un ejemplo de {topic}"
        ]
    }


@ai_blueprint.route("/lesson", methods=["POST"])
def lesson():
    data = request.json
    return jsonify(ai_engine(data["topic"], data.get("level", "medio")))


@ai_blueprint.route("/exam", methods=["POST"])
def exam():
    data = request.json
    lesson_data = ai_engine(data["topic"])

    return jsonify({
        "topic": data["topic"],
        "questions": lesson_data["preguntas"]
    })