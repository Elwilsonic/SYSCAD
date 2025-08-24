from flask import Blueprint, jsonify, request
from app.mapping import CargoMapping
from app.services import CargoService

cargo_bp = Blueprint('cargo', __name__)
cargo_mapping = CargoMapping()

@cargo_bp.route('/cargos', methods=['GET'])
def buscar_todos():
    cargos = CargoService.buscar_todos()
    return jsonify(cargo_mapping.dump(cargos)), 200

@cargo_bp.route('/cargos/<int:id>', methods=['GET'])
def buscar_por_id(id):
    cargo = CargoService.buscar_por_id(id)
    return cargo_mapping.dump(cargo), 200

@cargo_bp.route('/cargos', methods=['POST'])
def crear():
    cargo = cargo_mapping.load(request.get_json())
    CargoService.crear(cargo)
    return jsonify("Cargo creado exitosamente"), 200

@cargo_bp.route('/cargos/<int:id>', methods=['PUT'])
def actualizar(id):
    cargo = cargo_mapping.load(request.get_json())
    CargoService.actualizar(id, cargo)
    return jsonify("Cargo actualizado exitosamente"), 200

@cargo_bp.route('/cargos/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    CargoService.borrar_por_id(id)
    return jsonify("Cargo eliminado exitosamente"), 200
