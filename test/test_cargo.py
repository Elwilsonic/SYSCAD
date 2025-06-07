import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion
from app.services.cargo_service import CargoService

class CargoTestCase(unittest.TestCase):
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

    def test_crear_cargo(self):
        categoria = CategoriaCargo(nombre="Cat A")
        tipo = TipoDedicacion(nombre="Exclusiva", observacion="Obs")
        db.session.add_all([categoria, tipo])
        db.session.commit()
        cargo = Cargo(nombre="Profesor", puntos=10, categoria_cargo_id=categoria.id, tipo_dedicacion_id=tipo.id)
        resultado = CargoService.crear(cargo)
        self.assertIsNotNone(resultado.id)
        self.assertEqual(resultado.nombre, "Profesor")
        self.assertEqual(resultado.puntos, 10)
        self.assertEqual(resultado.categoria_cargo_id, categoria.id)
        self.assertEqual(resultado.tipo_dedicacion_id, tipo.id)

    def test_leer_cargo(self):
        categoria = CategoriaCargo(nombre="Cat B")
        tipo = TipoDedicacion(nombre="Simple", observacion="Obs2")
        db.session.add_all([categoria, tipo])
        db.session.commit()
        cargo = Cargo(nombre="JTP", puntos=5, categoria_cargo_id=categoria.id, tipo_dedicacion_id=tipo.id)
        db.session.add(cargo)
        db.session.commit()
        resultado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "JTP")
        self.assertEqual(resultado.puntos, 5)

    def test_actualizar_cargo(self):
        categoria = CategoriaCargo(nombre="Cat C")
        tipo = TipoDedicacion(nombre="Semi", observacion="Obs3")
        db.session.add_all([categoria, tipo])
        db.session.commit()
        cargo = Cargo(nombre="Ayudante", puntos=2, categoria_cargo_id=categoria.id, tipo_dedicacion_id=tipo.id)
        db.session.add(cargo)
        db.session.commit()
        nuevos_datos = Cargo(nombre="Ayudante Actualizado", puntos=3, categoria_cargo_id=categoria.id, tipo_dedicacion_id=tipo.id)
        resultado = CargoService.actualizar(cargo.id, nuevos_datos)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Ayudante Actualizado")
        self.assertEqual(resultado.puntos, 3)

    def test_borrar_cargo(self):
        categoria = CategoriaCargo(nombre="Cat D")
        tipo = TipoDedicacion(nombre="Parcial", observacion="Obs4")
        db.session.add_all([categoria, tipo])
        db.session.commit()
        cargo = Cargo(nombre="Auxiliar", puntos=1, categoria_cargo_id=categoria.id, tipo_dedicacion_id=tipo.id)
        db.session.add(cargo)
        db.session.commit()
        CargoService.borrar_por_id(cargo.id)
        resultado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()