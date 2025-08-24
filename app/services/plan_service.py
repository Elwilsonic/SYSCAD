from app.models import Plan
from app.repositories import PlanRepository

class PlanService:

    @staticmethod
    def crear(plan: Plan):
        """
        Crea un plan en la base de datos.
        """
        return PlanRepository.crear(plan)

    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        """
        Busca un plan en la base de datos por su id.
        """
        return PlanRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Plan]:
        """
        Busca todos los planes en la base de datos.
        """
        return PlanRepository.buscar_todos()

    @staticmethod
    def actualizar_plan(plan: Plan):
        """
        Actualiza un plan en la base de datos.
        """
        existente = PlanRepository.buscar_por_id(plan.id)
        if not existente:
            return None
        existente.nombre = plan.nombre
        existente.fecha_inicio = plan.fecha_inicio
        existente.fecha_fin = plan.fecha_fin
        existente.observacion = plan.observacion
        return existente

    @staticmethod
    def borrar_por_id(id: int):
        """
        Borra un plan en la base de datos por su id.
        """
        return PlanRepository.borrar_por_id(id)