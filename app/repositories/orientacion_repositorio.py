from app import db
from app.models.orientacion import Orientacion

class OrientacionRepository:
    @staticmethod
    def get_all():
        return db.session.query(Orientacion).all()

    @staticmethod
    def get_by_id(orientacion_id):
        return db.session.query(Orientacion).get(orientacion_id)

    @staticmethod
    def save(orientacion):
        db.session.add(orientacion)
        db.session.commit()
        return orientacion

    @staticmethod
    def delete(orientacion):
        db.session.delete(orientacion)
        db.session.commit()