from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(64), nullable=False, unique=True)
    password: str = db.Column(db.String(128), nullable=False)
    activated: bool = db.Column(db.Boolean, default=False)

    # Relación con Alumno (uno a uno)
    alumno = db.relationship('Alumno', uselist=False, back_populates='usuario')