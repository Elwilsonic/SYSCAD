from app import db

# Relación muchos a muchos entre Autoridad y Materia
autoridades_materias = db.Table(
    'autoridades_materias',
    db.Column('autoridad_id', db.Integer, db.ForeignKey('autoridades.id'), primary_key=True),
    db.Column('materia_id', db.Integer, db.ForeignKey('materias.id'), primary_key=True),
    extend_existing=True
)

# Relación muchos a muchos entre Orientacion y Materia
orientacion_materias = db.Table(
    'orientacion_materias',
    db.Column('orientacion_id', db.Integer, db.ForeignKey('orientaciones.id', ondelete="CASCADE"), primary_key=True),
    db.Column('materia_id', db.Integer, db.ForeignKey('materias.id', ondelete="CASCADE"), primary_key=True),
    extend_existing=True
)
