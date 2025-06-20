from app.models import Alumno
from app.repositories import AlumnoRepository
from app.services.facultad_service import FacultadService
from app.services.especialidad_service import EspecialidadService
from datetime import datetime
class AlumnoService:

    @staticmethod
    def crear(alumno):
        AlumnoRepository.crear(alumno)

    @staticmethod
    def buscar_por_id(id: int) -> Alumno:        
        return AlumnoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Alumno]:
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, alumno: Alumno) -> Alumno:
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nrodocumento = alumno.nrodocumento
        alumno_existente.tipo_documento = alumno.tipo_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Alumno:
        departamento = AlumnoRepository.borrar_por_id(id)
        if not departamento:
            return None
        return departamento

    def generar_certificado_alumno_regular(id: int):
        alumno = AlumnoRepository.buscar_alumno(id)
        #TODOS relacionar alumno con facultad y especialidad
        facultad = FacultadService.buscar_facultad(19)
        fecha = datetime.now()
        especialidad = EspecialidadService.buscar_especialidad()