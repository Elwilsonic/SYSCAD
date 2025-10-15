from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Facultad

class FacultadRepository(BaseRepository):
    model = Facultad

    @staticmethod
    def actualizar_facultad(facultad) -> Facultad:
        facultad_existente = db.session.merge(facultad)
        if not facultad_existente:
            return None
        return facultad_existente