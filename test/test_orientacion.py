import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

class OrientacionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
        db.create_all()

        # Datos relacionados
        self.especialidad = Especialidad(nombre="Especialidad X", letra="A", observacion="Obs esp")
        self.plan = Plan(
            nombre="Plan 2025",
            fecha_inicio="2025-01-01",
            fecha_fin="2026-12-31",
            observacion="Obs plan"
        )
        self.materia = Materia(nombre="Fisica", codigo="FIS101", observacion="Obs mat")

        db.session.add_all([self.especialidad, self.plan, self.materia])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_orientacion(self):
        orientacion = Orientacion(
            nombre="Orientacion A",
            observacion="Observación de prueba",
            especialidad=self.especialidad,
            plan=self.plan,
            materias=[self.materia]
        )
        db.session.add(orientacion)
        db.session.commit()

        self.assertIsNotNone(orientacion.id)
        self.assertEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.plan.nombre, "Plan 2025")
        self.assertEqual(len(orientacion.materias), 1)
        self.assertEqual(orientacion.materias[0].nombre, "Fisica")

    def test_read_orientacion(self):
        orientacion = Orientacion(
            nombre="Orientacion B",
            observacion="Lectura",
            especialidad=self.especialidad,
            plan=self.plan,
            materias=[self.materia]
        )
        db.session.add(orientacion)
        db.session.commit()

        fetched = Orientacion.query.filter_by(nombre="Orientacion B").first()
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.observacion, "Lectura")

    def test_update_orientacion(self):
        orientacion = Orientacion(
            nombre="Orientacion C",
            observacion="Antes de actualizar",
            especialidad=self.especialidad,
            plan=self.plan,
            materias=[self.materia]
        )
        db.session.add(orientacion)
        db.session.commit()

        orientacion.nombre = "Orientacion C Actualizada"
        orientacion.observacion = "Después de actualizar"
        db.session.commit()

        actualizado = Orientacion.query.get(orientacion.id)
        self.assertEqual(actualizado.nombre, "Orientacion C Actualizada")
        self.assertEqual(actualizado.observacion, "Después de actualizar")

    def test_delete_orientacion(self):
        orientacion = Orientacion(
            nombre="Orientacion D",
            observacion="Para eliminar",
            especialidad=self.especialidad,
            plan=self.plan,
            materias=[self.materia]
        )
        db.session.add(orientacion)
        db.session.commit()

        orientacion_id = orientacion.id
        db.session.delete(orientacion)
        db.session.commit()

        eliminado = Orientacion.query.get(orientacion_id)
        self.assertIsNone(eliminado)

if __name__ == '__main__':
    unittest.main()