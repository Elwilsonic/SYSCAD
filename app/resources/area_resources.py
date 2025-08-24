from flask import Blueprint, jsonify, request
from app.mapping import AreaMapping
from app.services import AreaService

area_bp = Blueprint('area', __name__)
area_mapping = AreaMapping()

@area_bp.route('/area', methods=['GET'])
def buscar_todos():
    page: int = request.headers.get('X-Page', 1, type=int)
    par_page: int = request.headers.get('X-Per-Size', 10, type=int)
    areas = AreaService.buscar_todos()
    return area_mapping.dump(areas, many=True), 200

@area_bp.route('/area/<int:id>', methods=['GET'])
def buscar_por_id(id):
    area = AreaService.buscar_por_id(id)
    return area_mapping.dump(area), 200

@area_bp.route('/area', methods=['POST'])
def crear():
    area = area_mapping.load(request.get_json())
    AreaService.crear(area)
    return jsonify("Area creada exitosamente"), 200

@area_bp.route('/area/<int:id>', methods=['PUT'])
def actualizar(id):
    area = area_mapping.load(request.get_json())
    AreaService.actualizar(id, area)
    return jsonify("Area actualizada exitosamente"), 200

@area_bp.route('/area/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    AreaService.borrar_por_id(id)
    return jsonify("Area borrada exitosamente"), 200