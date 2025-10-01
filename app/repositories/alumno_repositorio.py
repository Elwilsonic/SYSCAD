from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Alumno

class AlumnoRepository:
    model = Alumno
    
    @staticmethod
    def actualizar(alumno) -> Alumno:
        alumno_existente = db.session.merge(alumno)
        if not alumno_existente:
            return None
        db.session.commit()
        return alumno_existente