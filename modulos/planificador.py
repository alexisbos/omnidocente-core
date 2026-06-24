import tkinter as tk
from tkinter import ttk, messagebox
from modulos.banco_tareas import (
    crear_estudiante,
    actualizar_estudiante
)

from modulos.pdf_exporter import exportar_examen_pdf

examen_actual = None


def login_estudiante():
    nombre = entry_estudiante.get()
    if not nombre:
        return

    crear_estudiante(nombre)
    actualizar_estado()


def generar():
    global examen_actual

    nombre = entry_estudiante.get()
    materia = entry_materia.get()
    tema = entry_tema.get()

    if not nombre:
        messagebox.showerror("Error", "Ingresa estudiante")
        return

    est = actualizar_estudiante(nombre, 25)

    examen_actual = {
        "materia": materia,
        "tema": tema,
        "preguntas": [
            {"q": f"Define {tema}"},
            {"q": f"Ejemplo de {tema}"},
            {"q": f"Aplicación de {tema}"}
        ]
    }

    text.delete("1.0", tk.END)
    text.insert(tk.END, f"""
📘 SISTEMA RPG EDUCATIVO

Estudiante: {nombre}

📚 Tema: {tema}

⭐ XP: {est['xp']}
🏆 Nivel: {est['nivel']}
🔥 Combo: {est['combo']}
""")


def exportar():
    if not examen_actual:
        return

    ruta = exportar_examen_pdf(examen_actual, "examen_estudiante.pdf")

    messagebox.showinfo("PDF", f"Examen exportado:\n{ruta}")


def actualizar_estado():
    nombre = entry_estudiante.get()
    if not nombre:
        return

    est = crear_estudiante(nombre)

    label.config(
        text=f"{nombre} | Nivel {est['nivel']} | XP {est['xp']} | 🔥 {est['combo']}"
    )


def iniciar_planificador():
    global entry_estudiante, entry_materia, entry_tema, text, label

    ventana = tk.Tk()
    ventana.title("OmniDocenteCore RPG Nivel 5")
    ventana.geometry("800x600")

    label = ttk.Label(ventana, text="")
    label.pack()

    ttk.Label(ventana, text="Estudiante").pack()
    entry_estudiante = ttk.Entry(ventana)
    entry_estudiante.pack()

    ttk.Button(ventana, text="Login", command=login_estudiante).pack()

    ttk.Label(ventana, text="Materia").pack()
    entry_materia = ttk.Entry(ventana)
    entry_materia.pack()

    ttk.Label(ventana, text="Tema").pack()
    entry_tema = ttk.Entry(ventana)
    entry_tema.pack()

    ttk.Button(ventana, text="Generar Plan + XP", command=generar).pack()

    ttk.Button(ventana, text="Exportar PDF", command=exportar).pack()

    text = tk.Text(ventana, height=20)
    text.pack()

    ventana.mainloop()