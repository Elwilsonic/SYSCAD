from app import db
from app.models import Cargo

class CargoRepository:
    @staticmethod
    def crear(cargo):
        """
        Crea un nuevo cargo en la base de datos.
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        db.session.add(cargo)
        db.session.commit()
        return cargo

    @staticmethod
    def buscar_por_id(cargo_id):
        """
        Busca un cargo por su ID.
        :param cargo_id: ID del cargo a buscar.
        :return: Objeto Cargo encontrado o None si no existe.
        """
        return Cargo.query.get(cargo_id)

    @staticmethod
    def buscar_todos():
        """
        Busca todos los cargos en la base de datos.
        :return: Lista de objetos Cargo.
        """
        return Cargo.query.all()

    @staticmethod
    def actualizar(cargo_id, nuevos_datos):
        """
        Actualiza un cargo existente en la base de datos.
        :param cargo_id: ID del cargo a actualizar.
        :param nuevos_datos: Objeto Cargo con los nuevos datos.
        :return: Objeto Cargo actualizado o None si no existe.
        """
        cargo = Cargo.query.get(cargo_id)
        if not cargo:
            return None
        cargo.nombre = nuevos_datos.nombre
        cargo.puntos = nuevos_datos.puntos
        cargo.categoria_cargo_id = nuevos_datos.categoria_cargo_id
        cargo.tipo_dedicacion_id = nuevos_datos.tipo_dedicacion_id
        db.session.commit()
        return cargo

    @staticmethod
    def borrar_por_id(cargo_id):
        """
        Elimina un cargo de la base de datos por su ID.
        :param cargo_id: ID del cargo a eliminar.
        """
        cargo = Cargo.query.get(cargo_id)
        if cargo:
            db.session.delete(cargo)
            db.session.commit()