from app import db
from app.models import Autoridad

class AutoridadRepository:
    @staticmethod
    def crear(autoridad):
        """
        Crea una nueva autoridad en la base de datos.
        :param autoridad: Instancia de Autoridad con los datos a guardar.
        :return: La instancia de Autoridad creada.
        """
        db.session.add(autoridad)
        db.session.commit()
        return autoridad

    @staticmethod
    def buscar_por_id(autoridad_id):
        """
        Busca una autoridad por su ID.
        :param autoridad_id: ID de la autoridad a buscar.
        :return: La instancia de Autoridad si se encuentra, de lo contrario None.
        """
        return Autoridad.query.get(autoridad_id)

    @staticmethod
    def buscar_todos():
        """
        Busca todas las autoridades en la base de datos.
        :return: Lista de todas las instancias de Autoridad.
        """
        return Autoridad.query.all()

    @staticmethod
    def actualizar(autoridad_id, nuevos_datos):
        """ 
        Actualiza los datos de una autoridad existente.
        :param autoridad_id: ID de la autoridad a actualizar.
        """
        autoridad = Autoridad.query.get(autoridad_id)
        if not autoridad:
            return None
        autoridad.nombre = nuevos_datos.nombre
        autoridad.telefono = nuevos_datos.telefono
        autoridad.email = nuevos_datos.email
        # Agrega aquí otros campos si los hay
        db.session.commit()
        return autoridad

    @staticmethod
    def borrar_por_id(autoridad_id):
        """
        Elimina una autoridad por su ID.
        :param autoridad_id: ID de la autoridad a eliminar.
        :return: None
        """
        autoridad = Autoridad.query.get(autoridad_id)
        if autoridad:
            db.session.delete(autoridad)
            db.session.commit()
