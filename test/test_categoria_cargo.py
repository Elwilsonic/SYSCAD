import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import CategoriaCargo
from app.services import CategoriaCargoService

class CategoriaCargoTestCase(unittest.TestCase):
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

    def test_crear_categoria_cargo(self):
        categoria = CategoriaCargo(nombre="Docente")
        resultado = CategoriaCargoService.crear(categoria)
        self.assertIsNotNone(resultado.id)
        self.assertEqual(resultado.nombre, "Docente")

    def test_leer_categoria_cargo(self):
        categoria = CategoriaCargo(nombre="No Docente")
        db.session.add(categoria)
        db.session.commit()
        resultado = CategoriaCargoService.buscar_por_id(categoria.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "No Docente")

    def test_actualizar_categoria_cargo(self):
        categoria = CategoriaCargo(nombre="Administrativo")
        db.session.add(categoria)
        db.session.commit()
        nuevos_datos = CategoriaCargo(nombre="Administrativo Actualizado")
        resultado = CategoriaCargoService.actualizar(categoria.id, nuevos_datos)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Administrativo Actualizado")

    def test_borrar_categoria_cargo(self):
        categoria = CategoriaCargo(nombre="Temporal")
        db.session.add(categoria)
        db.session.commit()
        CategoriaCargoService.borrar_por_id(categoria.id)
        resultado = CategoriaCargoService.buscar_por_id(categoria.id)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()