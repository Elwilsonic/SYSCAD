from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    @staticmethod
    def crear(tipo_dedicacion):
        """
        Crea un nuevo tipo de dedicación en la base de datos.
        :param tipo_dedicacion: Objeto TipoDedicacion a crear.
        :return: Objeto TipoDedicacion creado.
        """
        db.session.add(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion

    @staticmethod
    def buscar_por_id(tipo_dedicacion_id):
        """
        Busca un tipo de dedicación por su ID.
        :param tipo_dedicacion_id: ID del tipo de dedicación a buscar.
        :return: Objeto TipoDedicacion encontrado o None si no existe.
        """
        return TipoDedicacion.query.get(tipo_dedicacion_id)

    @staticmethod
    def buscar_todos():
        """
        Busca todos los tipos de dedicación en la base de datos.
        :return: Lista de objetos TipoDedicacion.
        """
        return TipoDedicacion.query.all()

    @staticmethod
    def actualizar(tipo_dedicacion_id, nuevos_datos):
        """
        Actualiza un tipo de dedicación existente en la base de datos.
        :param tipo_dedicacion_id: ID del tipo de dedicación a actualizar.
        :param nuevos_datos: Objeto TipoDedicacion con los nuevos datos.
        :return: Objeto TipoDedicacion actualizado o None si no existe.
        """
        tipo_dedicacion = TipoDedicacion.query.get(tipo_dedicacion_id)
        if not tipo_dedicacion:
            return None
        tipo_dedicacion.nombre = nuevos_datos.nombre
        tipo_dedicacion.observacion = nuevos_datos.observacion
        db.session.commit()
        return tipo_dedicacion

    @staticmethod
    def borrar_por_id(tipo_dedicacion_id):
        """
        Elimina un tipo de dedicación de la base de datos por su ID.
        :param tipo_dedicacion_id: ID del tipo de dedicación a eliminar.
        """
        tipo_dedicacion = TipoDedicacion.query.get(tipo_dedicacion_id)
        if tipo_dedicacion:
            db.session.delete(tipo_dedicacion)
            db.session.commit()