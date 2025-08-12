from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    response = {"message": "OK", "data": None}
    return jsonify(response), 200