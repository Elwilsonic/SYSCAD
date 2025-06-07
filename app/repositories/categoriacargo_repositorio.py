from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    @staticmethod
    def crear(categoria_cargo):
        """
        Crea una nueva categoría de cargo en la base de datos.
        :param categoria_cargo: Objeto CategoriaCargo a crear.
        :return: Objeto CategoriaCargo creado.
        """
        db.session.add(categoria_cargo)
        db.session.commit()
        return categoria_cargo

    @staticmethod
    def buscar_por_id(categoria_cargo_id):
        """
        Busca una categoría de cargo por su ID.
        :param categoria_cargo_id: ID de la categoría a buscar.
        :return: Objeto CategoriaCargo encontrado o None si no existe.
        """
        return CategoriaCargo.query.get(categoria_cargo_id)

    @staticmethod
    def buscar_todos():
        """
        Busca todas las categorías de cargo en la base de datos.
        :return: Lista de objetos CategoriaCargo.
        """
        return CategoriaCargo.query.all()

    @staticmethod
    def actualizar(categoria_cargo_id, nuevos_datos):
        """
        Actualiza una categoría de cargo existente en la base de datos.
        :param categoria_cargo_id: ID de la categoría a actualizar.
        :param nuevos_datos: Objeto CategoriaCargo con los nuevos datos.
        :return: Objeto CategoriaCargo actualizado o None si no existe.
        """
        categoria_cargo = CategoriaCargo.query.get(categoria_cargo_id)
        if not categoria_cargo:
            return None
        categoria_cargo.nombre = nuevos_datos.nombre
        db.session.commit()
        return categoria_cargo

    @staticmethod
    def borrar_por_id(categoria_cargo_id):
        """
        Elimina una categoría de cargo de la base de datos por su ID.
        :param categoria_cargo_id: ID de la categoría a eliminar.
        """
        categoria_cargo = CategoriaCargo.query.get(categoria_cargo_id)
        if categoria_cargo:
            db.session.delete(categoria_cargo)
            db.session.commit()