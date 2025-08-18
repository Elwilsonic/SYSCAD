from app.models.area import Area
from app.repositories import AreaRepository

class AreaService:
    @staticmethod
    def crear(area: Area) -> Area:
        return AreaRepository.crear(area)

    @staticmethod
    def buscar_por_id(id: int) -> Area:
        return AreaRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Area]:
        return AreaRepository.buscar_todos()

    @staticmethod
    def actualizar_area(area: Area) -> Area:
        area_existente = AreaRepository.buscar_por_id(area.id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        return AreaRepository.actualizar_area(area_existente)

    @staticmethod
    def borrar_por_id(id: int) -> Area:
        return AreaRepository.borrar_por_id(id)