from app.repositories import CategoriaCargoRepository
from app.models import CategoriaCargo

class CategoriaCargoService:
    @staticmethod
    def crear(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        """
        Crea una nueva categoría de cargo en la base de datos.
        :param categoria_cargo: Objeto CategoriaCargo a crear.
        :return: Objeto CategoriaCargo creado.
        """
        return CategoriaCargoRepository.crear(categoria_cargo)

    @staticmethod
    def buscar_por_id(categoria_cargo_id: int) -> CategoriaCargo:
        """
        Busca una categoría de cargo por su ID.
        :param categoria_cargo_id: ID de la categoría a buscar.
        :return: Objeto CategoriaCargo encontrado o None si no existe.
        """
        return CategoriaCargoRepository.buscar_por_id(categoria_cargo_id)

    @staticmethod
    def buscar_todos() -> list:
        """
        Busca todas las categorías de cargo en la base de datos.
        :return: Lista de objetos CategoriaCargo.
        """
        return CategoriaCargoRepository.buscar_todos()

    @staticmethod
    def actualizar(categoria_cargo_id: int, nuevos_datos: CategoriaCargo) -> CategoriaCargo:
        """
        Actualiza una categoría de cargo existente en la base de datos.
        :param categoria_cargo_id: ID de la categoría a actualizar.
        :param nuevos_datos: Objeto CategoriaCargo con los nuevos datos.
        :return: Objeto CategoriaCargo actualizado o None si no existe.
        """
        return CategoriaCargoRepository.actualizar(categoria_cargo_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(categoria_cargo_id: int) -> None:
        """
        Elimina una categoría de cargo de la base de datos por su ID.
        :param categoria_cargo_id: ID de la categoría a eliminar.
        """
        CategoriaCargoRepository.borrar_por_id(categoria_cargo_id)