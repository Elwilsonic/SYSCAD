from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Facultad(db.Model):
    __tablename__ = 'facultades'
    id : int = db.Column(db.Integer, primary_key=True)
    nombre : str = db.Column(db.String(100), nullable=False)
    abreviatura : str = db.Column(db.String(10),nullable=False)
    directorio : str = db.Column(db.String(100),nullable=False)
    sigla : str = db.Column(db.String(10),nullable=False)
    codigoPostal : str = db.Column(db.String(10),nullable=True)
    ciudad : str = db.Column(db.String(50),nullable=True)
    domicilio : str = db.Column(db.String(100),nullable=True)
    telefono : str = db.Column(db.String(20),nullable=True)
    contacto :  str = db.Column(db.String(100),nullable=True)
    email : str = db.Column(db.String(100),nullable=False)
    
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'))
    universidad = db.relationship('Universidad', back_populates='facultades')
    autoridades = db.relationship('Autoridad', back_populates='facultad', cascade='all, delete-orphan')