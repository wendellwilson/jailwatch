from flask import Blueprint
from flask_restx import Api

client_blueprint = Blueprint('client_api', __name__)
client_api = Api(client_blueprint)