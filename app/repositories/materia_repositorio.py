from app.repositories.base_repository import BaseRepository
from app.models import Materia
from app import db

class MateriaRepository(BaseRepository):
    model = Materia

    @staticmethod
    def actualizar(materia_id: int, nuevos_datos: Materia) -> Materia:
        materia = Materia.query.get(materia_id)
        if materia:
            materia.nombre = nuevos_datos.nombre
            materia.codigo = nuevos_datos.codigo
            materia.observacion = nuevos_datos.observacion
            db.session.commit()
        return materia