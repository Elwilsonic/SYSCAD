from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(db.Model):
    __tablename__ = 'tipo_dedicacion'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    observacion = db.Column(db.String(255), nullable=True)
