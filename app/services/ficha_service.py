from app.repositories import AlumnoRepository
from app.models import Alumno
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

class FichaService:
    def __init__(self, alumno_repository: AlumnoRepository):
        self.alumno_repository = alumno_repository  # DIP

    def obtener_ficha(self, alumno_id: int) -> dict:
        alumno = self.alumno_repository.obtener_por_id(alumno_id)
        return {
            "nro_legajo": alumno.nro_legajo,
            "apellido": alumno.apellido,
            "nombre": alumno.nombre,
            "nrodocumento": alumno.nrodocumento
        }

    def generar_pdf(self, alumno_id: int) -> bytes:
        ficha = self.obtener_ficha(alumno_id)

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph("Ficha del Alumno", styles["Heading1"]))
        story.append(Spacer(1, 12))
        for key, value in ficha.items():
            story.append(Paragraph(f"<b>{key.capitalize()}:</b> {value}", styles["Normal"]))
            story.append(Spacer(1, 8))

        doc.build(story)
        pdf_value = buffer.getvalue()
        buffer.close()
        return pdf_value