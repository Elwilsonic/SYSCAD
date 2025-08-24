import unittest
import os
from flask import current_app
from app import create_app
from app.models import Grupo
from app.services import GrupoService
from app import db

class GrupoTestCase(unittest.TestCase):
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

    def test_grupo_creation(self):
        grupo = self.__nuevogrupo()
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre, "Grupo A")
    
    def test_crear_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        self.assertIsNotNone(grupo.id)
    
    def test_buscar_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        encontrado = GrupoService.buscar_por_id(grupo.id)
        self.assertEqual(encontrado.nombre, "Grupo A")
    
    def test_buscar_todos(self):
        GrupoService.crear(self.__nuevogrupo("Grupo A"))
        GrupoService.crear(self.__nuevogrupo("Grupo B"))
        todos = GrupoService.buscar_todos()
        self.assertGreaterEqual(len(todos), 2)

    def test_actualizar_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        grupo.nombre = "Grupo Actualizado"
        actualizado = GrupoService.actualizar_grupo(grupo)
        self.assertEqual(actualizado.nombre, "Grupo Actualizado")

    def test_borrar_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        GrupoService.borrar_por_id(grupo.id)
        self.assertIsNone(GrupoService.buscar_por_id(grupo.id))

    def __nuevogrupo(self, nombre="Grupo A"):
        grupo = Grupo()
        grupo.nombre = nombre
        return grupo
        