from flask import Response, jsonify, Blueprint, request
from app.mapping.alumno_mapping import AlumnoMapping
from app.services.alumno_service import AlumnoService
from app.services.ficha_service import FichaService
from app.repositories.alumno_repositorio import AlumnoRepository

alumno_bp = Blueprint('alumno', __name__)
alumno_mapping = AlumnoMapping()

@alumno_bp.route('/alumno', methods=['GET'])
def buscar_todos():
    alumnos = AlumnoService.buscar_todos()
    return alumno_mapping.dump(alumnos, many=True), 200

@alumno_bp.route("/alumnos/<int:alumno_id>/ficha", methods=["GET"])
def ficha_alumno(alumno_id):
    formato = request.args.get("formato", "json")

    alumno_repo= AlumnoRepository()
    ficha_service= FichaService(alumno_repo)

    if formato == "json":
        data = ficha_service.obtener_ficha(alumno_id)
        if data is None:
            return jsonify({"error": "Alumno no encontrado"}), 404
        return jsonify(data)

    elif formato == "pdf":
        data = ficha_service.obtener_ficha(alumno_id)
        if data is None:
            return jsonify({"error": "Alumno no encontrado"}), 404
        pdf_data = ficha_service.generar_pdf(alumno_id)
        return Response(pdf_data, mimetype="application/pdf",
                        headers={"Content-Disposition": f"attachment;filename=ficha_alumno_{alumno_id}.pdf"})
    else:
        return jsonify({"error": "Formato no soportado"}), 400
    
@alumno_bp.route('/alumno/<int:id>', methods=['GET'])
def buscar_por_id(id):
    alumno = AlumnoService.buscar_por_id(id)
    return alumno_mapping.dump(alumno), 200

@alumno_bp.route('/alumno', methods=['POST'])
def crear():
    alumno = alumno_mapping.load(request.get_json())
    AlumnoService.crear(alumno) 
    return jsonify("Alumno creado exitosamente"), 200

@alumno_bp.route('/alumno/<int:id>', methods=['PUT'])
def actualizar(id):
    alumno = alumno_mapping.load(request.get_json())
    AlumnoService.actualizar(id, alumno)
    return jsonify("Alumno actualizado exitosamente"), 200  

@alumno_bp.route('/alumno/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    AlumnoService.borrar_por_id(id)
    return jsonify("Alumno borrado exitosamente"), 200