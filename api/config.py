import os
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
ma = Marshmallow()

class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class StageConfig(BaseConfig):
    CONFIG_NAME = "stage"
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(BaseConfig):
    CONFIG_NAME = "prod"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

EXPORT_CONFIGS = [
    DevConfig,
    StageConfig,
    ProdConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}