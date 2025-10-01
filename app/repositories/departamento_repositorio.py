from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Departamento

class DepartamentoRepository:
    model = Departamento

    @staticmethod
    def actualizar(departamento) -> Departamento:
        departamento_existente = db.session.merge(departamento)
        if not departamento_existente:
            return None
        return departamento_existente
    
   