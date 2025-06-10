import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Usuario
from app.services import UsuarioService

class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_usuario(self):
        usuario = self.__nuevo_usuario()
        UsuarioService.crear(usuario)
        self.assertIsNotNone(usuario.id)
        self.assertEqual(usuario.username, "testuser")
        self.assertFalse(usuario.activated)

    def test_buscar_por_id(self):
        usuario = self.__nuevo_usuario()
        UsuarioService.crear(usuario)
        encontrado = UsuarioService.buscar_por_id(usuario.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.username, "testuser")

    def test_buscar_por_username(self):
        usuario = self.__nuevo_usuario()
        UsuarioService.crear(usuario)
        encontrado = UsuarioService.buscar_por_username("testuser")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.username, "testuser")

    def test_actualizar_usuario(self):
        usuario = self.__nuevo_usuario()
        UsuarioService.crear(usuario)
        usuario.username = "updateduser"
        usuario.activated = True
        UsuarioService.actualizar(usuario.id, usuario)
        actualizado = UsuarioService.buscar_por_id(usuario.id)
        self.assertEqual(actualizado.username, "updateduser")
        self.assertTrue(actualizado.activated)

    def test_borrar_usuario(self):
        usuario = self.__nuevo_usuario()
        UsuarioService.crear(usuario)
        UsuarioService.borrar_por_id(usuario.id)
        resultado = UsuarioService.buscar_por_id(usuario.id)
        self.assertIsNone(resultado)

    def __nuevo_usuario(self):
        usuario = Usuario()
        usuario.username = "testuser"
        usuario.password = "testpass"
        usuario.activated = False
        return usuario

if __name__ == '__main__':
    unittest.main()