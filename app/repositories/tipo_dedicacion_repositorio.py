from app.repositories.base_repository import BaseRepository
from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    model = TipoDedicacion

    @staticmethod
    def actualizar(tipo_dedicacion_id, nuevos_datos):
        tipo_dedicacion = TipoDedicacion.query.get(tipo_dedicacion_id)
        if not tipo_dedicacion:
            return None
        tipo_dedicacion.nombre = nuevos_datos.nombre
        tipo_dedicacion.observacion = nuevos_datos.observacion
        db.session.commit()
        return tipo_dedicacion
