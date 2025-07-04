from flask import jsonify, Blueprint, request
from app.mapping.universidad_mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidad', methods=['GET'])
def buscar_todos():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200
    
@universidad_bp.route('/universidad/<int:id>', methods=['GET'])
def buscar_por_id(id):
    universidad = UniversidadService.buscar_por_id(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['POST'])
def crear():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear(universidad) 
    return jsonify("Universidad creada exitosamente"), 200

@universidad_bp.route('/universidad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    UniversidadService.borrar_por_id(id)
    return jsonify("Universidad borrada exitosamente"), 200