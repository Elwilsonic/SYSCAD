from flask import Blueprint, jsonify, request
from app.mapping import EspecialidadMapping
from app.services import EspecialidadService

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_mapping = EspecialidadMapping()

@especialidad_bp.route('/especialidades', methods=['GET'])
def buscar_todos():
    especialidades = EspecialidadService.buscar_todos()
    return jsonify(especialidad_mapping.dump(especialidades)), 200

@especialidad_bp.route('/especialidades/<int:id>', methods=['GET'])
def buscar_por_id(id):
    especialidad = EspecialidadService.buscar_por_id(id)
    return jsonify(especialidad_mapping.dump(especialidad)), 200

@especialidad_bp.route('/especialidades', methods=['POST'])
def crear():
    especialidad = especialidad_mapping.load(request.get_json())
    EspecialidadService.crear(especialidad)
    return jsonify("Especialidad creada exitosamente"), 200

@especialidad_bp.route('/especialidades/<int:id>', methods=['PUT'])
def actualizar(id):
    especialidad = especialidad_mapping.load(request.get_json())
    EspecialidadService.actualizar(id, especialidad)
    return jsonify("Especialidad actualizada exitosamente"), 200

@especialidad_bp.route('/especialidades/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    EspecialidadService.borrar_por_id(id)
    return jsonify("Especialidad eliminada exitosamente"), 200
