import unittest
import os
from flask import current_app
from app import create_app
from app.models.area import Area
from app import db

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
        area = Area()
        area.nombre = "matematica"
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.nombre)
        self.assertEqual(area.nombre, "matematica")
    
    def test_crear_area(self):
        area = Area(nombre="Matemática")
        db.session.add(area)
        db.session.commit()
        self.assertIsNotNone(area.id)
        self.assertEqual(area.nombre, "Matemática")

    def test_buscar_area(self):
        area = Area(nombre="Matemática")
        db.session.add(area)
        db.session.commit()
        encontrada = Area.query.get(area.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Matemática")
    
    def test_buscar_todos(self):
        db.session.add(Area(nombre="Matemática"))
        db.session.add(Area(nombre="Ingles"))
        db.session.commit()
        areas = Area.query.all()
        self.assertGreaterEqual(len(areas), 2)
    
    def test_actualizar_area(self):
        area = Area(nombre="Matemática")
        db.session.add(area)
        db.session.commit()
        area.nombre = "Matemáticas Aplicadas"
        db.session.commit()
        actualizada = Area.query.get(area.id)
        self.assertEqual(actualizada.nombre, "Matemáticas Aplicadas")
    
    def test_borrar_area(self):
        area = Area(nombre="Temporal")
        db.session.add(area)
        db.session.commit()
        db.session.delete(area)
        db.session.commit()
        eliminada = Area.query.get(area.id)
        self.assertIsNone(eliminada)