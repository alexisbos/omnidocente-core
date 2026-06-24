import json
import os

DATA_PATH = "data/progreso.json"


def cargar_datos():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        data = {"estudiantes": {}}
        guardar_datos(data)
        return data

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_datos(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def crear_estudiante(nombre):
    data = cargar_datos()

    if nombre not in data["estudiantes"]:
        data["estudiantes"][nombre] = {
            "xp": 0,
            "nivel": 1,
            "vidas": 3,
            "logros": []
        }

    guardar_datos(data)
    return data["estudiantes"][nombre]


def actualizar_estudiante(nombre, xp_gain):
    data = cargar_datos()

    if nombre not in data["estudiantes"]:
        crear_estudiante(nombre)
        data = cargar_datos()

    est = data["estudiantes"][nombre]

    est["xp"] += xp_gain
    est["nivel"] = (est["xp"] // 100) + 1

    if est["xp"] >= 100 and "Novato" not in est["logros"]:
        est["logros"].append("Novato 🟢")

    if est["xp"] >= 300 and "Avanzado" not in est["logros"]:
        est["logros"].append("Avanzado 🔵")

    data["estudiantes"][nombre] = est
    guardar_datos(data)

    return est