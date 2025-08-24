from marshmallow import fields, Schema, post_load, validate
from app.models import Especialidad

class EspecialidadMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    letra = fields.String(required=True, validate=validate.Length(min=1, max=1))

    @post_load
    def nueva_especialidad(self, data, **kwargs) -> Especialidad:
        return Especialidad(**data)
