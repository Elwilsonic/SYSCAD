from app import db

class BaseRepository:
    model = None

    @classmethod
    def crear(cls, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def buscar_por_id(cls, id):
        return cls.model.query.get(id)

    @classmethod
    def buscar_todos(cls):
        return cls.model.query.all()

    @classmethod
    def borrar_por_id(cls, id):
        obj = cls.model.query.get(id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
