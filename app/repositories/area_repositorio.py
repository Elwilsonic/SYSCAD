from app.repositories.base_repository import BaseRepositoryf
from app import db
from app.models import Area

class AreaRepository:
    model = Area
    @staticmethod
    def actualizar_area(area: Area) -> Area:
        area_existente = db.session.merge(area)
        if not area_existente:
            return None
        db.session.commit()
        return area_existente