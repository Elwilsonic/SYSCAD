import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.area import Area
from app.services import AreaService

class AreaTestCase(unittest.TestCase):
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

    def test_area_creation(self):
        area = self.__nueva_area()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Matemática")

    def test_crear_area(self):
        area = self.__nueva_area()
        AreaService.crear(area)
        self.assertIsNotNone(area.id)
        self.assertEqual(area.nombre, "Matemática")

    def test_buscar_area_por_id(self):
        area = self.__nueva_area()
        AreaService.crear(area)
        encontrada = AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Matemática")

    def test_buscar_todas_las_areas(self):
        area1 = self.__nueva_area(nombre="Matemática")
        area2 = self.__nueva_area(nombre="Lengua")
        AreaService.crear(area1)
        AreaService.crear(area2)
        todas = AreaService.buscar_todos()
        self.assertEqual(len(todas), 2)

    def test_actualizar_area(self):
        area = self.__nueva_area()
        AreaService.crear(area)
        area.nombre = "Física"
        area_actualizada = AreaService.actualizar_area(area)
        self.assertEqual(area_actualizada.nombre, "Física")

    def test_borrar_area(self):
        area = self.__nueva_area()
        AreaService.crear(area)
        AreaService.borrar_por_id(area.id)
        resultado = AreaService.buscar_por_id(area.id)
        self.assertIsNone(resultado)

    def __nueva_area(self, nombre="Matemática"):
        area = Area()
        area.nombre = nombre
        return area
