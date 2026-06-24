from flask import Flask, render_template
from infra.db import init_db

from api.routes_students import students_bp
from api.routes_ai import ai_bp
from api.routes_auth import auth_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "change_this_in_production"

app.register_blueprint(students_bp, url_prefix="/api/students")
app.register_blueprint(ai_bp, url_prefix="/api/ai")
app.register_blueprint(auth_bp, url_prefix="/api/auth")


@app.before_first_request
def startup():
    init_db()


@app.route("/")
def home():
    return render_template("dashboard.html")