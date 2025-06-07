from app.repositories import CargoRepository
from app.models import Cargo

class CargoService:
    @staticmethod
    def crear(cargo: Cargo) -> Cargo:
        """
        Crea un nuevo cargo en la base de datos.
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        return CargoRepository.crear(cargo)

    @staticmethod
    def buscar_por_id(cargo_id: int) -> Cargo:
        """
        Busca un cargo por su ID.
        :param cargo_id: ID del cargo a buscar.
        :return: Objeto Cargo encontrado o None si no existe.
        """
        return CargoRepository.buscar_por_id(cargo_id)

    @staticmethod
    def buscar_todos() -> list:
        """
        Busca todos los cargos en la base de datos.
        :return: Lista de objetos Cargo.
        """
        return CargoRepository.buscar_todos()

    @staticmethod
    def actualizar(cargo_id: int, nuevos_datos: Cargo) -> Cargo:
        """
        Actualiza un cargo existente en la base de datos.
        :param cargo_id: ID del cargo a actualizar.
        :param nuevos_datos: Objeto Cargo con los nuevos datos.
        :return: Objeto Cargo actualizado o None si no existe.
        """
        return CargoRepository.actualizar(cargo_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(cargo_id: int) -> None:
        """
        Elimina un cargo de la base de datos por su ID.
        :param cargo_id: ID del cargo a eliminar.
        """
        CargoRepository.borrar_por_id(cargo_id)