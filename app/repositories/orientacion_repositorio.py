from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Orientacion

class OrientacionRepository(BaseRepository):
    model = Orientacion

    @staticmethod
    def actualizar(orientacion) -> Orientacion:
        orientacion_existente = db.session.merge(orientacion)
        if not orientacion_existente:
            return None
        return orientacion_existente