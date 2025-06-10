from app import db
from app.models import Usuario

class UsuarioRepository:
    @staticmethod
    def crear(usuario: Usuario) -> Usuario:
        """
        Crea un nuevo usuario en la base de datos.
        :param usuario: Objeto Usuario a crear.
        :return: Objeto Usuario creado.
        """
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def buscar_por_id(usuario_id: int) -> Usuario:
        """
        Busca un usuario por su ID.
        :param usuario_id: ID del usuario a buscar.
        :return: Objeto Usuario encontrado o None si no se encuentra.
        """
        return Usuario.query.get(usuario_id)

    @staticmethod
    def buscar_por_username(username: str) -> Usuario:
        """
        Busca un usuario por su nombre de usuario.
        :param username: Nombre de usuario a buscar.
        :return: Objeto Usuario encontrado o None si no se encuentra.
        """
        return Usuario.query.filter_by(username=username).first()

    @staticmethod
    def buscar_todos() -> list[Usuario]:
        """
        Busca todos los usuarios en la base de datos.
        :return: Lista de objetos Usuario.
        """
        return Usuario.query.all()

    @staticmethod
    def actualizar(usuario_id: int, nuevos_datos: Usuario) -> Usuario:
        """
        Actualiza los datos de un usuario existente.
        :param usuario_id: ID del usuario a actualizar.
        :param nuevos_datos: Objeto Usuario con los nuevos datos.
        :return: Objeto Usuario actualizado o None si no se encuentra.
        """
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            usuario.username = nuevos_datos.username
            usuario.password = nuevos_datos.password
            usuario.activated = nuevos_datos.activated
            db.session.commit()
        return usuario

    @staticmethod
    def borrar_por_id(usuario_id: int) -> Usuario:
        """
        Borra un usuario por su ID.
        :param usuario_id: ID del usuario a borrar.
        :return: Objeto Usuario borrado o None si no se encuentra.
        """
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return usuario
        return None