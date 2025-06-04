from app import db
from app.models import Area

class AreaRepository:
    @staticmethod
    def crear(area: Area) -> Area:
        """
        Crea un nuevo área en la base de datos.
        :param area: Objeto Area a crear.
        :return: Objeto Area creado.
        """
        db.session.add(area)
        db.session.commit()
        return area

    @staticmethod
    def buscar_por_id(id: int) -> Area:
        """
        Busca un área en la base de datos por su id.
        :param id: Id del área a buscar.
        :return: Objeto Area encontrado o None si no existe.
        """
        return db.session.query(Area).filter_by(id=id).first()

    @staticmethod
    def buscar_todos() -> list[Area]:
        """
        Busca todos los áreas en la base de datos.
        :return: Lista de objetos Area encontrados.
        """
        return db.session.query(Area).all()

    @staticmethod
    def actualizar_area(area: Area) -> Area:
        """
        Actualiza un área en la base de datos.
        :param area: Objeto Area a actualizar.
        :return: Objeto Area actualizado.
        """
        area_existente = db.session.merge(area)
        if not area_existente:
            return None
        db.session.commit()
        return area_existente

    @staticmethod
    def borrar_por_id(id: int) -> Area:
        """
        Borra un área en la base de datos por su id.
        :param id: Id del área a borrar.
        :return: Objeto Area borrado o None si no existe.
        """
        area = db.session.query(Area).filter_by(id=id).first()
        if not area:
            return None
        db.session.delete(area)
        db.session.commit()
        return area
