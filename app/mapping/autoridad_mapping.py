from marshmallow import fields, Schema, post_load, validate
from app.models.autoridad import Autoridad

class AutoridadMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    telefono = fields.String(validate=validate.Length(max=20))

    @post_load
    def nueva_autoridad(self, data, **kwargs) -> Autoridad:
        return Autoridad(**data)
    