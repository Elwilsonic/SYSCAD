from app.repositories import MateriaRepository
from app.models import Materia

class MateriaService:
    @staticmethod
    def crear(materia: Materia) -> Materia:
        return MateriaRepository.crear(materia)

    @staticmethod
    def buscar_por_id(materia_id: int) -> Materia:
        return MateriaRepository.buscar_por_id(materia_id)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        return MateriaRepository.buscar_todos()

    @staticmethod
    def actualizar(materia_id: int, nuevos_datos: Materia) -> Materia:
        return MateriaRepository.actualizar(materia_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(materia_id: int) -> None:
        MateriaRepository.borrar_por_id(materia_id)
 