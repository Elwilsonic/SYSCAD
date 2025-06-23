from app.models.facultad import Facultad
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class FacultadMapping(SQLAlchemyAutoSchema):
    class Meta:
        model = Facultad
        load_instance = True