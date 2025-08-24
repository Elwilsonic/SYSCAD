from flask import Blueprint, jsonify, request
from app.mapping import OrientacionMapping
from app.services import OrientacionService

orientacion_bp = Blueprint('orientacion', __name__)
orientacion_mapping = OrientacionMapping()

@orientacion_bp.route('/orientaciones', methods=['GET'])
def buscar_todos():
    orientaciones = OrientacionService.buscar_todos()
    return jsonify(orientacion_mapping.dump(orientaciones)), 200

@orientacion_bp.route('/orientaciones/<int:id>', methods=['GET'])
def buscar_por_id(id):
    orientacion = OrientacionService.buscar_por_id(id)
    return jsonify(orientacion_mapping.dump(orientacion)), 200

@orientacion_bp.route('/orientaciones', methods=['POST'])
def crear():
    orientacion = orientacion_mapping.load(request.get_json())
    OrientacionService.crear(orientacion)
    return jsonify("Orientación creada exitosamente"), 200

@orientacion_bp.route('/orientaciones/<int:id>', methods=['PUT'])
def actualizar(id):
    orientacion = orientacion_mapping.load(request.get_json())
    OrientacionService.actualizar(id, orientacion)
    return jsonify("Orientación actualizada exitosamente"), 200

@orientacion_bp.route('/orientaciones/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    OrientacionService.borrar_por_id(id)
    return jsonify("Orientación eliminada exitosamente"), 200
