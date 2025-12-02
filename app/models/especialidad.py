from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Especialidad(HashidMixin, db.Model):
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(1), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)