from flask import Flask

from client_api import client_blueprint
from worker_api import worker_blueprint
from . import config_by_name, db, ma

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name or 'dev'])

    app.register_blueprint(client_blueprint)
    app.register_blueprint(worker_blueprint)
    
    db.init_app(app)
    ma.init_app(app)