from app.repositories.base_repository import BaseRepository
from app import db
from app.models import TipoEspecialidad

class TipoEspecialidadRepository(BaseRepository):
    model = TipoEspecialidad

    @staticmethod
    def actualizar(tipoespecialidad) -> TipoEspecialidad:
        tipoespecialidad_existente = db.session.merge(tipoespecialidad)
        if not tipoespecialidad_existente:
            return None
        return tipoespecialidad_existente