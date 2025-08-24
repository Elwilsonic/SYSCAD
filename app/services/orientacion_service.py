from app.repositories import OrientacionRepository
from app.models.orientacion import Orientacion

class OrientacionService:
    @staticmethod
    def listar_orientaciones():
        return OrientacionRepository.get_all()

    @staticmethod
    def obtener_orientacion(orientacion_id):
        return OrientacionRepository.get_by_id(orientacion_id)

    @staticmethod
    def crear(nombre, especialidad, plan, materias):
        orientacion = Orientacion()
        orientacion.nombre = nombre
        orientacion.especialidad = especialidad
        orientacion.plan = plan
        orientacion.materias = materias
        return OrientacionRepository.save(orientacion)

    @staticmethod
    def eliminar_orientacion(orientacion_id):
        orientacion = OrientacionRepository.get_by_id(orientacion_id)
        if orientacion:
            OrientacionRepository.delete(orientacion)
            return True
        return False