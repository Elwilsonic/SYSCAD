from marshmallow import Schema, fields

class ResponseSchema(Schema):
    message = fields.String(required=True)
    data = fields.Raw(required=False, allow_none=True)
class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    activated = fields.Bool()

class AlumnoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    nrodocumento = fields.Str(required=True)
    tipo_documento_id = fields.Int(required=True)
    fecha_nacimiento = fields.Date(required=True)
    sexo = fields.Str(required=True)
    nro_legajo = fields.Int(required=True)
    fecha_ingreso = fields.Date(required=True)
    usuario = fields.Nested(UsuarioSchema, allow_none=True)

class MateriaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    codigo = fields.Str(required=True)
    observacion = fields.Str(allow_none=True)
    orientacion_id = fields.Int(required=True)

class FacultadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    abreviatura = fields.Str(allow_none=True)
    directorio = fields.Str(allow_none=True)
    sigla = fields.Str(allow_none=True)
    codigoPostal = fields.Str(allow_none=True)
    ciudad = fields.Str(allow_none=True)
    domicilio = fields.Str(allow_none=True)
    telefono = fields.Str(allow_none=True)
    contacto = fields.Str(allow_none=True)
    email = fields.Str(allow_none=True)
    universidad_id = fields.Int(required=True)

class UniversidadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    sigla = fields.Str(required=True)

class AutoridadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    telefono = fields.Str(allow_none=True)
    email = fields.Str(allow_none=True)
    cargo_id = fields.Int(allow_none=True)
    facultad_id = fields.Int(required=True)

class CargoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    puntos = fields.Int(required=True)
    categoria_cargo_id = fields.Int(required=True)
    tipo_dedicacion_id = fields.Int(allow_none=True)

class CategoriaCargoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class TipoDedicacionSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    observacion = fields.Str(allow_none=True)

class EspecialidadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    letra = fields.Str(required=True)
    observacion = fields.Str(allow_none=True)
    tipo_especialidad_id = fields.Int(required=True)

class TipoEspecialidadSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    # Si tienes el campo nivel, descomenta la siguiente línea
    # nivel = fields.Str(allow_none=True)

class PlanSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    fecha_inicio = fields.Str(required=True)
    fecha_fin = fields.Str(required=True)
    observacion = fields.Str(allow_none=True)

class OrientacionSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    observacion = fields.Str(allow_none=True)
    especialidad_id = fields.Int(required=True)
    plan_id = fields.Int(required=True)

class AreaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class GrupoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class GradoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str(allow_none=True)

class DepartamentoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

class TipoDocumentoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    dni = fields.Str(required=True)
    libreta_civica = fields.Str(required=True)
    libreta_enrolamiento = fields.Str(required=True)
    pasaporte = fields.Str(required=True)

class NotaSchema(Schema):
    id = fields.Int(dump_only=True)
    valor = fields.Float(required=True)
    fecha = fields.Date(required=True)
    alumno_id = fields.Int(required=True)