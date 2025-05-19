import unittest
from flask import current_app
from app import create_app, db  # Asegurate de importar db desde app
from app.models import Facultad
from app.services.facultad_service import FacultadService
import os

class FacultadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crear las tablas antes de cada test
        db.create_all()  

    def tearDown(self):
        # Limpiar la sesión
        db.session.remove() 
         # Eliminar las tablas al finalizar cada test     
        db.drop_all()            
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad = self.__nuevaFacultad()
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(facultad.abreviatura, "FCE")

    def test_facultad_busqueda(self):
        facultad = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        facultad_encontrada = FacultadService.buscar_por_id(facultad.id)
        self.assertIsNotNone(facultad_encontrada)
        self.assertEqual(facultad_encontrada.nombre, "Facultad de Ciencias Exactas")

    def __nuevaFacultad(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ciencias Exactas"
        facultad.abreviatura = "FCE"
        facultad.directorio = "Ciencias Exactas"
        facultad.sigla = "FCE"
        facultad.codigoPostal = "12345"
        facultad.ciudad = "La Plata"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email = "abc@gmail.com"
        return facultad

if __name__ == "__main__":
    unittest.main()
