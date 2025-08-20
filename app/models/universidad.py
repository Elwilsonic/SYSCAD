from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Universidad(HashidMixin, db.Model):
    __allow_unmapped__ = True
    __tablename__ = "universidad"
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    sigla: str = db.Column(db.String(10), nullable=False)

    facultades = db.relationship('Facultad', back_populates='universidad', cascade='all, delete-orphan')