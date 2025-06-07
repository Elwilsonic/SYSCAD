import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import TipoDedicacion
from app.services import TipoDedicacionService

class TipoDedicacionTestCase(unittest.TestCase):
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

    def test_crear_tipo_dedicacion(self):
        tipo = TipoDedicacion(nombre="Simple", observacion="Obs 1")
        resultado = TipoDedicacionService.crear(tipo)
        self.assertIsNotNone(resultado.id)
        self.assertEqual(resultado.nombre, "Simple")
        self.assertEqual(resultado.observacion, "Obs 1")

    def test_leer_tipo_dedicacion(self):
        tipo = TipoDedicacion(nombre="Exclusiva", observacion="Obs 2")
        db.session.add(tipo)
        db.session.commit()
        resultado = TipoDedicacionService.buscar_por_id(tipo.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Exclusiva")
        self.assertEqual(resultado.observacion, "Obs 2")

    def test_actualizar_tipo_dedicacion(self):
        tipo = TipoDedicacion(nombre="Parcial", observacion="Obs 3")
        db.session.add(tipo)
        db.session.commit()
        nuevos_datos = TipoDedicacion(nombre="Parcial Actualizado", observacion="Obs 3 Modificada")
        resultado = TipoDedicacionService.actualizar(tipo.id, nuevos_datos)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Parcial Actualizado")
        self.assertEqual(resultado.observacion, "Obs 3 Modificada")

    def test_borrar_tipo_dedicacion(self):
        tipo = TipoDedicacion(nombre="Temporal", observacion="Obs 4")
        db.session.add(tipo)
        db.session.commit()
        TipoDedicacionService.borrar_por_id(tipo.id)
        resultado = TipoDedicacionService.buscar_por_id(tipo.id)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()