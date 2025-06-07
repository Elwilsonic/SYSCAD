from app.repositories import TipoDedicacionRepository
from app.models import TipoDedicacion

class TipoDedicacionService:
    @staticmethod
    def crear(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        """
        Crea un nuevo tipo de dedicación en la base de datos.
        :param tipo_dedicacion: Objeto TipoDedicacion a crear.
        :return: Objeto TipoDedicacion creado.
        """
        return TipoDedicacionRepository.crear(tipo_dedicacion)

    @staticmethod
    def buscar_por_id(tipo_dedicacion_id: int) -> TipoDedicacion:
        """
        Busca un tipo de dedicación por su ID.
        :param tipo_dedicacion_id: ID del tipo de dedicación a buscar.
        :return: Objeto TipoDedicacion encontrado o None si no existe.
        """
        return TipoDedicacionRepository.buscar_por_id(tipo_dedicacion_id)

    @staticmethod
    def buscar_todos() -> list:
        """
        Busca todos los tipos de dedicación en la base de datos.
        :return: Lista de objetos TipoDedicacion.
        """
        return TipoDedicacionRepository.buscar_todos()

    @staticmethod
    def actualizar(tipo_dedicacion_id: int, nuevos_datos: TipoDedicacion) -> TipoDedicacion:
        """
        Actualiza un tipo de dedicación existente en la base de datos.
        :param tipo_dedicacion_id: ID del tipo de dedicación a actualizar.
        :param nuevos_datos: Objeto TipoDedicacion con los nuevos datos.
        :return: Objeto TipoDedicacion actualizado o None si no existe.
        """
        return TipoDedicacionRepository.actualizar(tipo_dedicacion_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(tipo_dedicacion_id: int) -> None:
        """
        Elimina un tipo de dedicación de la base de datos por su ID.
        :param tipo_dedicacion_id: ID del tipo de dedicación a eliminar.
        """
        TipoDedicacionRepository.borrar_por_id(tipo_dedicacion_id)