from app import db

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    # Relación inversa para la relación muchos a muchos con Autoridad
    autoridades = db.relationship('Autoridad', secondary='autoridades_materias', back_populates='materias')