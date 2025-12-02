import logging, os
from flask import Flask 
from flask_migrate import Migrate
from flask_hashids import Hashids
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from app.blueprints import registrar_blueprints

db = SQLAlchemy()
migrate = Migrate()
hashids = Hashids()
ma = Marshmallow()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)
    migrate.init_app(app, db)
    hashids.init_app(app)
    ma.init_app(app)
    
    # Endpoint principal /api/v1/
    from flask import jsonify
    from app.schemas import ResponseSchema
    @app.route('/api/v1/', methods=['GET'])
    def api_v1_index():
        response = {"message": "Bienvenido a la API v1", "data": None}
        return jsonify(ResponseSchema().dump(response)), 200
    
    registrar_blueprints(app)

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
