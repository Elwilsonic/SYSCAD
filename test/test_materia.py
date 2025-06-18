import unittest
import os
from flask import current_app
from app import create_app,db
from app.models import Materia, Orientacion, Autoridad, Cargo, CategoriaCargo, TipoDedicacion, Especialidad, Plan
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
        materia = self.__nuevoMateria()
        MateriaService.crear(materia)
        self._assert_materia(materia, "Matematica",
                             "MAT101", "Matematica basica")
        self.assertIsNotNone(materia.orientacion)
        self.assertIsNotNone(materia.autoridades)

    def test_buscar_por_id(self):
        materia = self.__nuevoMateria()
        MateriaService.crear(materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Matematica","MAT101", "Matematica basica")
        self.assertIsNotNone(encontrado.orientacion)
        self.assertIsNotNone(encontrado.autoridades)

    def test_buscar_todos(self):
        materia1 = self.__nuevoMateria()
        materia2 = self.__nuevaMateria2()
        MateriaService.crear(materia1)
        MateriaService.crear(materia2)
        materias = MateriaService.buscar_todos()
        self._assert_materia(
            materias[0], "Matematica", "MAT101", "Matematica basica")
        self._assert_materia(
            materias[1], "Base de datos", "BD101", "Base de datos basica")
        self.assertEqual(len(materias), 2)
        
    def test_actualizar_materia(self):
        materia = self.__nuevoMateria()
        MateriaService.crear(materia)
        materia.nombre = "Matematica avanzada"
        materia.codigo = "MAT201"
        materia.observacion = "Matematica avanzada basica"
        MateriaService.actualizar(materia.id, materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Matematica avanzada",
                             "MAT201", "Matematica avanzada basica")

    def test_borrar_materia(self):
        materia = self.__nuevoMateria()
        MateriaService.crear(materia)
        MateriaService.borrar_por_id(materia.id)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self.assertIsNone(encontrado)
        
# metodos para crear objetos de prueba

    def __nuevoMateria(self):
        categoria = self.__CategoriaCargo()
        db.session.add(categoria)
        db.session.commit()
        tipo = self.__tipoDeCargo()
        db.session.add(tipo)
        db.session.commit()
        cargo = self.__nuevoCargo()
        db.session.add(cargo)
        db.session.commit()
        autoridad = self.__nuevaAutoridad()
        db.session.add(autoridad)
        db.session.commit()
        orientacion = self.__nuevoOrientacion()
        db.session.add(orientacion)
        db.session.commit()
        materia = Materia()
        materia.nombre = "Matematica"
        materia.codigo = "MAT101"
        materia.observacion = "Matematica basica"
        materia.asociar_autoridad(autoridad)
        materia.orientacion = orientacion
        return materia

    def __nuevaMateria2(self):
        categoria = self.__CategoriaCargo()
        db.session.add(categoria)
        db.session.commit()
        tipo = self.__tipoDeCargo()
        db.session.add(tipo)
        db.session.commit()
        cargo = self.__nuevoCargo()
        db.session.add(cargo)
        db.session.commit()
        autoridad = self.__nuevaAutoridad()
        db.session.add(autoridad)
        db.session.commit()
        orientacion = self.__nuevoOrientacion()
        db.session.add(orientacion)
        db.session.commit()
        materia = Materia()
        materia.nombre = "Base de datos"
        materia.codigo = "BD101"
        materia.observacion = "Base de datos basica"
        materia.asociar_autoridad(autoridad)
        materia.orientacion = orientacion
        return materia

    def __nuevaAutoridad(self):
        autoridad = Autoridad()
        autoridad.nombre = "Juan Perez"
        autoridad.telefono = "123456789"
        autoridad.email = "email123@mail.com"
        autoridad.cargo = self.__nuevoCargo()
        return autoridad
    
    def __nuevoCargo(self):
        cargo = Cargo()
        cargo.nombre = "Profesor"
        cargo.puntos = 10
        cargo.categoria_cargo = self.__CategoriaCargo()
        cargo.tipo_dedicacion = self.__tipoDeCargo()
        return cargo

    def __tipoDeCargo(self):
        tipo = TipoDedicacion.query.filter_by(nombre="Tiempo completo").first()
        if tipo is None:
            tipo = TipoDedicacion()
            tipo.nombre = "Tiempo completo"
            db.session.add(tipo)
            db.session.commit()
        return tipo
        
    def __CategoriaCargo(self):
        categoria = CategoriaCargo.query.filter_by(nombre="Docente").first()
        if categoria is None:
            categoria = CategoriaCargo()
            categoria.nombre = "Docente"
            db.session.add(categoria)
            db.session.commit()
        return categoria
    
    def __nuevoOrientacion(self):
        especialidad = Especialidad()
        especialidad.nombre = "Especialidad Test"
        especialidad.letra = "A"
        especialidad.observacion = "Obs especialidad"
        db.session.add(especialidad)
        db.session.commit()
        plan = Plan()
        plan.nombre = "Plan Test"
        plan.fecha_inicio = "2025-01-01"
        plan.fecha_fin = "2026-12-31"
        plan.observacion = "Obs plan"
        db.session.add(plan)
        db.session.commit()
        orientacion = Orientacion()
        orientacion.nombre = "Orientacion1"
        orientacion.especialidad = especialidad
        orientacion.plan = plan
        return orientacion   
    
    def _assert_materia(self, materia, nombre, codigo, observacion):
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, nombre)
        self.assertEqual(materia.codigo, codigo)
        self.assertEqual(materia.observacion, observacion)
        self.assertIsNotNone(materia.id)
        self.assertGreaterEqual(materia.id, 1)

if __name__ == '__main__':
    unittest.main()
