from flask import Flask
from client_api.jails import jails_blueprint
from client_api.map import map_blueprint
from config import config_by_name

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name or 'dev'])

    app.register_blueprint(jails_blueprint)
    app.register_blueprint(map_blueprint)

    from api.models.shared import db
    db.init_app(app)
    from api.shared import ma
    ma.init_app(app)