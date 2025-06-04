from app import db
from app.models import Grupo

class GrupoRepository:

    @staticmethod
    def crear(grupo):
        """
        Crea un nuevo grupo en la base de datos.
        :param grupo: Objeto Grupo a crear.
        :return: Objeto Grupo creado.
        """
        db.session.add(grupo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca un grupo por su ID.
        :param id: ID del grupo a buscar.
        :return: Objeto Grupo encontrado o None si no se encuentra.
        """
        return db.session.query(Grupo).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        """
        Busca todos los grupos en la base de datos.
        :return: Lista de objetos Grupo.
        """
        return db.session.query(Grupo).all()

    @staticmethod
    def actualizar_grupo(grupo):
        """
        Actualiza un grupo en la base de datos.
        :param grupo: Objeto Grupo a actualizar.
        :return: Objeto Grupo actualizado o None si no se encuentra.
        """
        grupo_existente = db.session.merge(grupo)
        if not grupo_existente:
            return None
        return grupo_existente

    @staticmethod
    def borrar_por_id(id: int):
        """
        Borra un grupo por su ID.
        :param id: ID del grupo a borrar.
        :return: Objeto Grupo borrado o None si no se encuentra.
        """
        grupo = db.session.query(Grupo).filter_by(id=id).first()
        if not grupo:
            return None
        db.session.delete(grupo)
        db.session.commit()
        return grupo
