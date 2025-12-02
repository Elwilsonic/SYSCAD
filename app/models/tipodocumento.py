from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(HashidMixin, db.Model):
    __tablename__ = "tipodocumentos"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sigla: str = db.Column(db.String(10), nullable=False)
    nombre: str = db.Column(db.String(50), nullable=False)