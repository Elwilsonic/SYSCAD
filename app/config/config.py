from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
env_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path=env_path)

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    HASHIDS_MIN_LENGTH: str = os.environ.get('HASHIDS_MIN_LENGTH') or '8'
    HASHIDS_ALPHABET: str = os.environ.get('HASHIDS_ALPHABET') or os.environ.get('ALFABETO') or 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    HASHIDS_SALT: str = os.environ.get('HASHIDS_SALT') or 'default_salt'
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'default_secret_key'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app: str) -> Config:
    configuration = {
        'testing': TestConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }

    return configuration[app]
