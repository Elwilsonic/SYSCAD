from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Cargo

class CargoRepository(BaseRepository):
    model = Cargo
    
    @staticmethod
    def actualizar(cargo_id, nuevos_datos):
        cargo = Cargo.query.get(cargo_id)
        if not cargo:
            return None
        cargo.nombre = nuevos_datos.nombre
        cargo.puntos = nuevos_datos.puntos
        cargo.categoria_cargo_id = nuevos_datos.categoria_cargo_id
        cargo.tipo_dedicacion_id = nuevos_datos.tipo_dedicacion_id
        db.session.commit()
        return cargo