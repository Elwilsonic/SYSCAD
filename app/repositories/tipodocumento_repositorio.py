from app.repositories.base_repository import BaseRepository
from app import db
from app.models import TipoDocumento

class TipoDocumentoRepository(BaseRepository):
    model = TipoDocumento

    @staticmethod
    def actualizar(tipodocumento) -> TipoDocumento:
        tipodocumento_existente = db.session.merge(tipodocumento)
        if not tipodocumento_existente:
            return None
        return tipodocumento_existente