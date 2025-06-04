import unittest
import os
from flask import current_app
from app import create_app,db
from app.models import Materia
from app.services import MateriaService

class MateriaTestCase(unittest.TestCase):
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

    def test_crear_materia(self):
        materia = Materia(nombre="Matemáticas", codigo="MAT101", observacion="Observación de prueba")
        resultado = MateriaService.crear(materia)

        self.assertIsNotNone(resultado.id)
        self.assertEqual(resultado.nombre, "Matemáticas")
        self.assertEqual(resultado.codigo, "MAT101")
        self.assertEqual(resultado.observacion, "Observación de prueba")