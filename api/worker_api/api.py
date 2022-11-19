from flask import Blueprint
from flask_restx import Api

from .charges import charge_ns
from .inmates import inmate_ns

worker_blueprint = Blueprint('worker_api', __name__)
worker_api = Api(worker_blueprint)

worker_api.add_namespace(charge_ns, path='/charge')
worker_api.add_namespace(inmate_ns, path='/inmate')