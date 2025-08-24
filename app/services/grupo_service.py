from app.models import Grupo
from app.repositories import GrupoRepository

class GrupoService:

    @staticmethod
    def crear(grupo: Grupo):
        """
        Crea un nuevo grupo en la base de datos.
        :param grupo: Objeto Grupo a crear.
        :return: Objeto Grupo creado.
        """
        return GrupoRepository.crear(grupo)

    @staticmethod
    def buscar_por_id(id: int) -> Grupo:
        """
        Busca un grupo por su ID.
        :param id: ID del grupo a buscar.
        :return: Objeto Grupo encontrado o None si no se encuentra.
        """
        return GrupoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Grupo]:
        """
        Busca todos los grupos en la base de datos.
        :return: Lista de objetos Grupo.
        """
        return GrupoRepository.buscar_todos()

    @staticmethod
    def actualizar_grupo(grupo: Grupo):
        """
        Actualiza un grupo en la base de datos.
        :param grupo: Objeto Grupo a actualizar.
        :return: Objeto Grupo actualizado o None si no se encuentra.
        """
        grupo_existente = GrupoRepository.buscar_por_id(grupo.id)
        if not grupo_existente:
            return None
        grupo_existente.nombre = grupo.nombre
        return grupo_existente

    @staticmethod
    def borrar_por_id(id: int) -> Grupo:
        """
        Borra un grupo por su ID.
        :param id: ID del grupo a borrar.
        :return: Objeto Grupo borrado o None si no se encuentra.
        """
        grupo = GrupoRepository.borrar_por_id(id)
        if not grupo:
            return None
        return grupo
