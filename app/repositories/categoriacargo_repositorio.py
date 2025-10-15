from app.repositories.base_repository import BaseRepository
from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository(BaseRepository):
    model = CategoriaCargo
    
    @staticmethod
    def actualizar(categoria_cargo_id, nuevos_datos):
        categoria_cargo = CategoriaCargo.query.get(categoria_cargo_id)
        if not categoria_cargo:
            return None
        categoria_cargo.nombre = nuevos_datos.nombre
        db.session.commit()
        return categoria_cargo
