from app import db
from app.models import Alumno

class AlumnoRepository:
    @staticmethod
    def crear(alumno):
        """
        Crea un nuevo alumno en la base de datos.
        """
        db.session.add(alumno)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca un alumno por su id.
        """
        return db.session.query(Alumno).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        """
        Busca todos los alumnos.
        """
        return db.session.query(Alumno).all()
    
    @staticmethod
    def actualizar(alumno) -> Alumno:
        """
        Actualiza un alumno en la base de datos.
        """
        alumno_existente = db.session.merge(alumno)
        if not alumno_existente:
            return None
        db.session.commit()
        return alumno_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Alumno:
        """
        Borra un alumno por su id.
        """
        alumno = db.session.query(Alumno).filter_by(id=id).first()
        if not alumno:
            return None
        db.session.delete(alumno)
        db.session.commit()
        return alumno