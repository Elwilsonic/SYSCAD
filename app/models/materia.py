from app import db

class Materia(db.Model):
    _tablename_ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    observacion = db.Column(db.String(255))