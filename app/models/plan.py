from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = 'planes'
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    fecha_inicio: str = db.Column(db.String(20), nullable=False)
    fecha_fin: str = db.Column(db.String(20), nullable=False)
    observacion: str = db.Column(db.String(255))