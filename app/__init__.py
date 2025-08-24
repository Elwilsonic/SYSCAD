import logging, os
from flask import Flask 
from flask_migrate import Migrate
from flask_hashids import Hashids
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app.config import config

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
    
    from app.resources import (
        alumno_bp, area_bp, autoridad_bp, categoriacargo_bp, certificado_bp, departamento_bp, facultad_bp, grado_bp, grupo_bp, home, plan_bp,
        tipo_especialidad_bp, tipodedicacion_bp, tipodocumento_bp, universidad_bp, materia_bp, cargo_bp, especialidad_bp, orientacion_bp
    )
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(universidad_bp, url_prefix='/api/v1')
    app.register_blueprint(area_bp, url_prefix='/api/v1')
    app.register_blueprint(tipodocumento_bp, url_prefix='/api/v1')
    app.register_blueprint(tipodedicacion_bp, url_prefix='/api/v1')
    app.register_blueprint(categoriacargo_bp, url_prefix='/api/v1')
    app.register_blueprint(grupo_bp, url_prefix='/api/v1')
    app.register_blueprint(grado_bp, url_prefix='/api/v1')
    app.register_blueprint(departamento_bp, url_prefix='/api/v1')
    app.register_blueprint(certificado_bp, url_prefix='/api/v1')
    app.register_blueprint(tipo_especialidad_bp, url_prefix='/api/v1')
    app.register_blueprint(plan_bp, url_prefix='/api/v1')
    app.register_blueprint(alumno_bp, url_prefix='/api/v1')
    app.register_blueprint(autoridad_bp, url_prefix='/api/v1')
    app.register_blueprint(facultad_bp, url_prefix='/api/v1')
    app.register_blueprint(materia_bp, url_prefix='/api/v1')
    app.register_blueprint(cargo_bp, url_prefix='/api/v1')
    app.register_blueprint(especialidad_bp, url_prefix='/api/v1')
    app.register_blueprint(orientacion_bp, url_prefix='/api/v1')

    # Endpoint principal /api/v1/
    from flask import jsonify
    from app.schemas import ResponseSchema
    @app.route('/api/v1/', methods=['GET'])
    def api_v1_index():
        response = {"message": "Bienvenido a la API v1", "data": None}
        return jsonify(ResponseSchema().dump(response)), 200

    from app.resources import home, certificado_bp
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
