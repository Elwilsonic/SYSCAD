from flask import Blueprint, jsonify, request
from app.mapping import TipoDocumentoMapping
from app.services import TipoDocumentoService

tipodocumento_bp = Blueprint('tipodocumento', __name__)
tipodocumento_mapping = TipoDocumentoMapping()

@tipodocumento_bp.route('/tipodocumento', methods=['GET'])
def buscar_todos():
    tipodocumentos = TipoDocumentoService.buscar_todos()
    return tipodocumento_mapping.dump(tipodocumentos, many=True), 200

@tipodocumento_bp.route('/tipodocumento/<int:id>', methods=['GET'])
def buscar_por_id(id):
    tipodocumento = TipoDocumentoService.buscar_por_id(id)
    if tipodocumento:
        return tipodocumento_mapping.dump(tipodocumento), 200
    return jsonify({'error': 'No encontrado'}), 404

@tipodocumento_bp.route('/tipodocumento', methods=['POST'])
def crear():
    data = request.get_json()
    errors = tipodocumento_mapping.validate(data)
    if errors:
        return jsonify(errors), 400
    tipodocumento = TipoDocumentoService.crear(data)
    return tipodocumento_mapping.dump(tipodocumento), 201

@tipodocumento_bp.route('/tipodocumento/<int:id>', methods=['PUT'])
def actualizar(id):
    tipodocumento = tipodocumento_mapping.load(request.get_json())
    TipoDocumentoService.actualizar(id, tipodocumento)
    return jsonify("TipoDocumento actualizado exitosamente"), 200

@tipodocumento_bp.route('/tipodocumento/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    exito = TipoDocumentoService.borrar_por_id(id)
    if exito:
        return jsonify({'mensaje': 'TipoDocumento borrado exitosamente'}), 200
    return jsonify({'error': 'No encontrado'}), 404
