from app.repositories.base_repository import BaseRepository
from app import db
from app.models import Plan

class PlanRepository:
    model = Plan

    @staticmethod
    def actualizar_plan(plan):
        plan_existente = db.session.merge(plan)
        db.session.commit()
        return plan_existente
