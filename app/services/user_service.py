from app.models import Usuario
from app.repositories import UsuarioRepository

class UsuarioService:
    @staticmethod
    def crear(usuario: Usuario) -> Usuario:
        """
        Crea un nuevo usuario en la base de datos.
        :param usuario: Objeto Usuario a crear.
        :return: Objeto Usuario creado.
        """
        return UsuarioRepository.crear(usuario)

    @staticmethod
    def buscar_por_id(usuario_id: int) -> Usuario:
        """
        Busca un usuario por su ID.
        :param usuario_id: ID del usuario a buscar.
        :return: Objeto Usuario encontrado o None si no se encuentra.
        """
        return UsuarioRepository.buscar_por_id(usuario_id)

    @staticmethod
    def buscar_por_username(username: str) -> Usuario:
        """
        Busca un usuario por su nombre de usuario.
        :param username: Nombre de usuario a buscar.
        :return: Objeto Usuario encontrado o None si no se encuentra.
        """
        return UsuarioRepository.buscar_por_username(username)

    @staticmethod
    def buscar_todos() -> list[Usuario]:
        """
        Busca todos los usuarios en la base de datos.
        :return: Lista de objetos Usuario.
        """
        return UsuarioRepository.buscar_todos()

    @staticmethod
    def actualizar(usuario_id: int, nuevos_datos: Usuario) -> Usuario:
        """
        Actualiza los datos de un usuario existente.
        :param usuario_id: ID del usuario a actualizar.
        :param nuevos_datos: Objeto Usuario con los nuevos datos.
        :return: Objeto Usuario actualizado o None si no se encuentra.
        """
        return UsuarioRepository.actualizar(usuario_id, nuevos_datos)

    @staticmethod
    def borrar_por_id(usuario_id: int) -> Usuario:
        """
        Borra un usuario por su ID.
        :param usuario_id: ID del usuario a borrar.
        :return: Objeto Usuario borrado o None si no se encuentra.
        """
        usuario = UsuarioRepository.borrar_por_id(usuario_id)
        if not usuario:
            return None
        return usuario
