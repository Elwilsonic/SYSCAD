from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Autoridad

class AutoridadRepository:
    model = Autoridad
    
    @staticmethod
    def actualizar(autoridad_id, nuevos_datos):
        autoridad = Autoridad.query.get(autoridad_id)
        if not autoridad:
            return None
        autoridad.nombre = nuevos_datos.nombre
        autoridad.telefono = nuevos_datos.telefono
        autoridad.email = nuevos_datos.email
        # Agrega aquí otros campos si los hay
        db.session.commit()
        return autoridad