from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
 # HEREDA DE db.Model
class Cargo(db.Model):
    __tablename__ = 'cargos'

    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    puntos: int = db.Column(db.Integer, nullable=False)

    categoria_cargo_id = db.Column(db.Integer, db.ForeignKey('categoria_cargo.id'))
    tipo_dedicacion_id = db.Column(db.Integer, db.ForeignKey('tipo_dedicacion.id'))

    # relaciones opcionales:
    # categoria_cargo = db.relationship('CategoriaCargo')
    # tipo_dedicacion = db.relationship('TipoDedicacion')