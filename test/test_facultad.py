import unittest
from flask import current_app
from app import create_app, db  
from app.models import Facultad, Universidad, Autoridad
from app.services import FacultadService
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

    def test_facultad_universidad(self):
        universidad = Universidad(nombre="UNLP", sigla="UNLP")
        db.session.add(universidad)
        db.session.commit()
        facultad = self.__nuevaFacultad()
        facultad.universidad = universidad
        db.session.add(facultad)
        db.session.commit()
        self.assertEqual(facultad.universidad.nombre, "UNLP")
        self.assertIn(facultad, universidad.facultades)

    def test_facultad_autoridades(self):
        facultad = self.__nuevaFacultad()
        db.session.add(facultad)
        db.session.commit()
        autoridad = Autoridad(nombre="Juan Perez", telefono="123456789", email="jp@unlp.edu.ar")
        autoridad.facultad = facultad
        db.session.add(autoridad)
        db.session.commit()
        self.assertEqual(autoridad.facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertIn(autoridad, facultad.autoridades)

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
