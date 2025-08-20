from dataclasses import dataclass

from app import db

@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    __tablename__ = 'autoridades'
    id: int = db.Column(db.Integer,primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)

    cargo_id: int = db.Column(db.Integer, db.ForeignKey('cargos.id'))
    cargo = db.relationship('Cargo')
    # Relación inversa para la relación muchos a muchos con Materia
    materias = db.relationship('Materia', secondary='autoridades_materias', back_populates='autoridades')

    facultad_id = db.Column(db.Integer, db.ForeignKey('facultades.id'))
    facultad = db.relationship('Facultad', back_populates='autoridades')