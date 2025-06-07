import unittest
import os
from flask import current_app
from app import create_app
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion
from app.services.autoridad_service import AutoridadService
from app import db

class AutoridadTestCase(unittest.TestCase):
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

    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        cargo.nombre= "Decano"
        cargo.puntos= 100
        self.__new_object(autoridad, cargo, tipo_dedicacion)
        db.session.add(autoridad.cargo.categoria_cargo)
        db.session.add(tipo_dedicacion)
        db.session.add(cargo)
        db.session.add(autoridad)
        db.session.commit()
        resultado = AutoridadService.crear(autoridad)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Juan Perez")
        self.assertIsNotNone(resultado.cargo)
        self.assertEqual(resultado.cargo.nombre, "Decano")
        self.assertEqual(resultado.telefono, "123456789")
        self.assertEqual(resultado.email, "abc@gmail.com")
        self.assertIsNotNone(resultado.cargo.categoria_cargo)
        self.assertEqual(resultado.cargo.categoria_cargo.nombre, "Categoria 1")

    def test_autoridad_read(self):
        autoridad = Autoridad(nombre="Ana Lopez", telefono="987654321", email="ana@uni.edu")
        db.session.add(autoridad)
        db.session.commit()
        resultado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Ana Lopez")
        self.assertEqual(resultado.telefono, "987654321")
        self.assertEqual(resultado.email, "ana@uni.edu")

    def test_autoridad_update(self):
        autoridad = Autoridad(nombre="Pedro", telefono="111", email="p@uni.edu")
        db.session.add(autoridad)
        db.session.commit()
        nuevos_datos = Autoridad(nombre="Pedro Actualizado", telefono="222", email="p2@uni.edu")
        resultado = AutoridadService.actualizar(autoridad.id, nuevos_datos)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Pedro Actualizado")
        self.assertEqual(resultado.telefono, "222")
        self.assertEqual(resultado.email, "p2@uni.edu")

    def test_autoridad_delete(self):
        autoridad = Autoridad(nombre="Borrar", telefono="000", email="b@uni.edu")
        db.session.add(autoridad)
        db.session.commit()
        AutoridadService.borrar_por_id(autoridad.id)
        resultado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNone(resultado)

    def __new_object(self, autoridad, cargo, tipo_dedicacion):
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        cargo.tipo_dedicacion.nombre = "Simple"
        cargo.tipo_dedicacion.observacion = "Observacion 1"
        autoridad.nombre = "Juan Perez"
        autoridad.cargo= cargo
        autoridad.telefono= "123456789"
        autoridad.email= "abc@gmail.com"
        
if __name__ == '__main__':
    unittest.main()