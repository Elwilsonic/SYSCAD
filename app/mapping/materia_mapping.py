from marshmallow import fields, Schema, post_load, validate
from app.models import Materia

class MateriaMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    codigo = fields.String(required=True, validate=validate.Length(min=1, max=20))

    @post_load
    def nueva_materia(self, data, **kwargs) -> Materia:
        return Materia(**data)
