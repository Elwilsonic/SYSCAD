from flask import Blueprint, jsonify, request
from app.mapping import MateriaMapping
from app.services import MateriaService

materia_bp = Blueprint('materia', __name__)
materia_mapping = MateriaMapping()

@materia_bp.route('/materias', methods=['GET'])
def buscar_todos():
    materias = MateriaService.buscar_todos()
    return jsonify(materia_mapping.dump(materias)), 200

@materia_bp.route('/materias/<int:id>', methods=['GET'])
def buscar_por_id(id):
    materia = MateriaService.buscar_por_id(id)
    return jsonify(materia_mapping.dump(materia)), 200

@materia_bp.route('/materias', methods=['POST'])
def crear():
    materia = materia_mapping.load(request.get_json())
    MateriaService.crear(materia)
    return jsonify("Materia creada exitosamente"), 200

@materia_bp.route('/materias/<int:id>', methods=['PUT'])
def actualizar(id):
    materia = materia_mapping.load(request.get_json())
    MateriaService.actualizar(id, materia)
    return jsonify("Materia actualizada exitosamente"), 200

@materia_bp.route('/materias/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    MateriaService.borrar_por_id(id)
    return jsonify("Materia eliminada exitosamente"), 200
