from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Universidad

class UniversidadRepository:
    model = Universidad
    
    @staticmethod
    def actualizar_universidad(universidad) -> Universidad:
        facultad_existente = db.session.merge(universidad)
        if not facultad_existente:
            return None
        return facultad_existente