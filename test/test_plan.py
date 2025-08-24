import unittest
import os
from flask import current_app
from app import create_app
from app.models.plan import Plan
from app.services import PlanService
from app import db

class PlanTestCase(unittest.TestCase):
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

    def test_plan_creation(self):
        plan = self.__nuevoplan()
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, "Plan A")
        self.assertEqual(plan.fecha_inicio, "2023-01-01")
        self.assertEqual(plan.fecha_fin, "2023-12-31")
    
    def test_crear_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        self.assertIsNotNone(plan.id)
    
    def test_buscar_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        encontrado = PlanService.buscar_por_id(plan.id)
        self.assertEqual(encontrado.nombre, "Plan A")
    
    def test_buscar_todos(self):
        PlanService.crear(self.__nuevoplan("Plan A"))
        PlanService.crear(self.__nuevoplan("Plan B", "2024-01-01", "2024-12-31"))
        todos = PlanService.buscar_todos()
        self.assertGreaterEqual(len(todos), 2)
    
    def test_actualizar_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        plan.nombre = "Plan Actualizado"
        actualizado = PlanService.actualizar_plan(plan)
        self.assertEqual(actualizado.nombre, "Plan Actualizado")
    
    def test_borrar_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        PlanService.borrar_por_id(plan.id)
        self.assertIsNone(PlanService.buscar_por_id(plan.id))
    
    def __nuevoplan(self, nombre="Plan A", fecha_inicio="2023-01-01", fecha_fin="2023-12-31", observacion="Observacion de prueba"):
        plan = Plan()
        plan.nombre = nombre
        plan.fecha_inicio = fecha_inicio
        plan.fecha_fin = fecha_fin
        plan.observacion = observacion
        return plan