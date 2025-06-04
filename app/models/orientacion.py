from app import db
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

# Tabla intermedia para la relación muchos a muchos entre Orientacion y Materia
orientacion_materias = db.Table('orientacion_materias',
    db.Column('orientacion_id', db.Integer, db.ForeignKey('orientaciones.id'), primary_key=True),
    db.Column('materia_id', db.Integer, db.ForeignKey('materias.id'), primary_key=True)
)

class Orientacion(db.Model):
    __tablename__ = 'orientaciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)

    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    especialidad = db.relationship('Especialidad', backref=db.backref('orientaciones', lazy=True))

    plan_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    plan = db.relationship('Plan', backref=db.backref('orientaciones', lazy=True))

    materias = db.relationship('Materia', secondary=orientacion_materias, backref='orientaciones')