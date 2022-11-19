from flask import Blueprint
from flask_restx import Api

from .counties import counties_ns
from .jails import jails_ns

client_blueprint = Blueprint('client_api', __name__)
client_api = Api(client_blueprint)

client_api.add_namespace(counties_ns, '/counties')
client_api.add_namespace(jails_ns, '/jails')