from marshmallow import fields, Schema, post_load, validate
from app.models import Plan

class PlanMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    fecha_inicio = fields.String(required=True, validate=validate.Length(min=1, max=20))
    fecha_fin = fields.String(required=True, validate=validate.Length(min=1, max=20))
    observacion = fields.String(allow_none=True, validate=validate.Length(max=255))

    @post_load
    def nuevo_plan(self, data, **kwargs) -> Plan:
        return Plan(**data)