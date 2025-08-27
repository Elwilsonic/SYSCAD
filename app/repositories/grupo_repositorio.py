from app.repositories.base_repository import BaseRepository
from app.models import Grupo
from app import db

class GrupoRepository(BaseRepository):
    model = Grupo

    @staticmethod
    def actualizar_grupo(grupo):
        grupo_existente = db.session.merge(grupo)
        if not grupo_existente:
            return None
        return grupo_existente
