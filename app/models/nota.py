from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Nota(db.Model):
    __tablename__ = 'notas'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    alumno = db.relationship('Alumno', back_populates='notas')
