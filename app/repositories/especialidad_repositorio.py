from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Especialidad

class EspecialidadRepository:
    model = Especialidad
    
    @staticmethod
    def actualizar(especialidad) -> Especialidad:
        especialidad_existente = db.session.merge(especialidad)
        if not especialidad_existente:
            return None
        return especialidad_existente
