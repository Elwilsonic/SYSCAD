from app import db
from app.models import Materia

class MateriaRepository:
    @staticmethod
    def crear(materia: Materia) -> Materia:
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def buscar_por_id(materia_id: int) -> Materia:
        return Materia.query.get(materia_id)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        return Materia.query.all()

    @staticmethod
    def actualizar(materia_id: int, nuevos_datos: Materia) -> Materia:
        materia = Materia.query.get(materia_id)
        if materia:
            materia.nombre = nuevos_datos.nombre
            materia.codigo = nuevos_datos.codigo
            materia.observacion = nuevos_datos.observacion
            db.session.commit()
        return materia

    @staticmethod
    def borrar_por_id(materia_id: int) -> None:
        materia = Materia.query.get(materia_id)
        if materia:
            db.session.delete(materia)
            db.session.commit()