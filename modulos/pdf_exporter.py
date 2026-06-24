from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def exportar_examen_pdf(examen, nombre_archivo="examen.pdf"):
    if not os.path.exists("exports"):
        os.makedirs("exports")

    ruta = os.path.join("exports", nombre_archivo)

    c = canvas.Canvas(ruta, pagesize=letter)

    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Examen - {examen['materia']}")
    y -= 30

    c.setFont("Helvetica", 12)

    for i, p in enumerate(examen["preguntas"]):
        c.drawString(50, y, f"{i+1}. {p['q']}")
        y -= 20

        if y < 100:
            c.showPage()
            y = 750

    c.save()

    return ruta