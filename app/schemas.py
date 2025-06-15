from marshmallow import Schema, fields

class ResponseSchema(Schema):
    message = fields.String(required=True)
    data = fields.Raw(required=False, allow_none=True)
