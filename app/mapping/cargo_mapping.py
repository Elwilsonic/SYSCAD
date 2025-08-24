from marshmallow import Schema, fields, post_load, validate
from app.models import Cargo

class CargoMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    puntos = fields.Integer(required=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs) -> Cargo:
        return Cargo(**data)
