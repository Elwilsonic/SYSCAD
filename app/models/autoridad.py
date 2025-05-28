from dataclasses import dataclass
from app.models import Cargo

from app import db

@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    __tablename__ = 'autoridades'
    id: int = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)

    cargo_id: int = db.Column(db.Integer, db.Foreignkey('cargos.id'))
    cargo = db.relationship('Cargo')