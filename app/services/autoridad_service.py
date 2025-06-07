from app.repositories import AutoridadRepository
from app.models import Autoridad

class AutoridadService:
    @staticmethod
    def crear(autoridad: Autoridad) -> Autoridad:
        """
        Crea una nueva autoridad en la base de datos.
        :param autoridad: Instancia de Autoridad con los datos a guardar.
        :return: La instancia de Autoridad creada.
        """
        return AutoridadRepository.crear(autoridad)

    @staticmethod
    def buscar_por_id(autoridad_id: int) -> Autoridad:
        """
        Busca una autoridad por su ID.
        :param autoridad_id: ID de la autoridad a buscar.
        :return: La instancia de Autoridad si se encuentra, de lo contrario None.
        """
        return AutoridadRepository.buscar_por_id(autoridad_id)

    @staticmethod
    def buscar_todos() -> list:
        """
        Busca todas las autoridades en la base de datos.
        :return: Lista de todas las instancias de Autoridad.
        """
        return AutoridadRepository.buscar_todos()

    @staticmethod
    def actualizar(autoridad_id: int, nuevos_datos: Autoridad) -> Autoridad:
        """
        Actualiza los datos de una autoridad existente.
        :param autoridad_id: ID de la autoridad a actualizar.
        :param nuevos_datos: Instancia de Autoridad con los nuevos datos.
        """
        return AutoridadRepository.actualizar(autoridad_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(autoridad_id: int) -> None:
        """
        Elimina una autoridad por su ID.
        :param autoridad_id: ID de la autoridad a eliminar.
        :return: None
        """
        AutoridadRepository.borrar_por_id(autoridad_id)
