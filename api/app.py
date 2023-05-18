from flask import Flask

from api.client_api import client_blueprint
from api.worker_api import worker_blueprint
from . import config_by_name, db, ma

def create_app(config_name='dev'):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    app.register_blueprint(client_blueprint, url_prefix="/api")
    app.register_blueprint(worker_blueprint, url_prefix="/worker/api")
    
    db.init_app(app)
    ma.init_app(app)

    return app