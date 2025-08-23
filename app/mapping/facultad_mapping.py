from marshmallow import Schema, fields, post_load, validate
from app.models.facultad import Facultad

class FacultadMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    abreviatura = fields.String(required=True, validate=validate.Length(min=1, max=10))
    directorio = fields.String(required=True, validate=validate.Length(min=1, max=100))
    sigla = fields.String(required=True, validate=validate.Length(min=1, max=10))
    email = fields.Email(required=True, validate=validate.Length(max=100))

    @post_load
    def nueva_facultad(self, data, **kwargs) -> Facultad:
        return Facultad(**data)
