from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Grado

class GradoRepository(BaseRepository):
    model = Grado

    @staticmethod
    def actualizar_grado(grado) -> Grado:
        grado_existente = db.session.merge(grado)
        if not grado_existente:
            return None
        return grado_existente