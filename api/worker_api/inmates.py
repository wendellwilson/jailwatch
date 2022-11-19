from flask_restx import Resource

from api.models import Inmate
from api.shared.schemas import InmateSchema
from . import worker_api

inmate_schema = InmateSchema()

@worker_api.route('/inmate')
class Inmate(Resource):
    def put():
        inmate = None
        return inmate_schema.dump(inmate)