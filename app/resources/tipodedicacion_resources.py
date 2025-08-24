from flask import Blueprint, jsonify, request
from app.mapping import TipoDedicacionMapping
from app.services import TipoDedicacionService

tipodedicacion_bp = Blueprint('tipodedicacion', __name__)
tipodedicacion_mapping = TipoDedicacionMapping()

@tipodedicacion_bp.route('/tipodedicacion', methods=['GET'])
def buscar_todos():
    tipodedicaciones = TipoDedicacionService.buscar_todos()
    return tipodedicacion_mapping.dump(tipodedicaciones, many=True), 200

@tipodedicacion_bp.route('/tipodedicacion/<int:id>', methods=['GET'])
def buscar_por_id(id):
    tipodedicacion = TipoDedicacionService.buscar_por_id(id)
    if tipodedicacion:
        return tipodedicacion_mapping.dump(tipodedicacion), 200
    return jsonify({'error': 'No encontrado'}), 404

@tipodedicacion_bp.route('/tipodedicacion', methods=['POST'])
def crear():
    data = request.get_json()
    errors = tipodedicacion_mapping.validate(data)
    if errors:
        return jsonify(errors), 400
    tipodedicacion = TipoDedicacionService.crear(data)
    return tipodedicacion_mapping.dump(tipodedicacion), 201

@tipodedicacion_bp.route('/tipodedicacion/<int:id>', methods=['PUT'])
def actualizar(id):
    tipodedicacion = tipodedicacion_mapping.load(request.get_json())
    TipoDedicacionService.actualizar(id, tipodedicacion)
    return jsonify("TipoDedicacion actualizada exitosamente"), 200

@tipodedicacion_bp.route('/tipodedicacion/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    exito = TipoDedicacionService.borrar_por_id(id)
    if exito:
        return jsonify({'mensaje': 'TipoDedicacion borrada exitosamente'}), 200
    return jsonify({'error': 'No encontrado'}), 404