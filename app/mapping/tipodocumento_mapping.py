from app.models import TipoDocumento
from marshmallow import Schema, fields, post_load, validate

class TipoDocumentoMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    descripcion = fields.String(validate=validate.Length(max=255))

    @post_load
    def nuevo_tipodocumento(self, data, **kwargs):
        return TipoDocumento(**data)