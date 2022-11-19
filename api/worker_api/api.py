from flask import Blueprint
from flask_restx import Api

worker_blueprint = Blueprint('worker_api', __name__)
worker_api = Api(worker_blueprint)