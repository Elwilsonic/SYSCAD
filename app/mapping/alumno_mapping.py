from app.models.alumno import Alumno
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AlumnoMapping(SQLAlchemyAutoSchema):
    class Meta:
        model = Alumno
        load_instance = True