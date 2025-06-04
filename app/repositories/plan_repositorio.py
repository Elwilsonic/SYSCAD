from app import db
from app.models import Plan

class PlanRepository:

    @staticmethod
    def crear(plan):
        """
        Crea un nuevo plan en la base de datos.
        """
        db.session.add(plan)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca un plan en la base de datos por su id.
        """
        return db.session.query(Plan).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        """
        Busca todos los planes en la base de datos.
        """
        return db.session.query(Plan).all()

    @staticmethod
    def actualizar_plan(plan):
        """
        Actualiza un plan en la base de datos.
        """
        plan_existente = db.session.merge(plan)
        db.session.commit()
        return plan_existente

    @staticmethod
    def borrar_por_id(id: int):
        """
        Borra un plan de la base de datos por su id.
        """
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan