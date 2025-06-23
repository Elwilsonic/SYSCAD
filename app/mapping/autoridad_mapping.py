from app.models.autoridad import Autoridad
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AutoridadMapping(SQLAlchemyAutoSchema):
    class Meta:
        model = Autoridad
        load_instance = True