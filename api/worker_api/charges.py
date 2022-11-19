from flask_restx import Resource

from api.models import Charge
from api.shared.schemas import ChargeSchema
from . import worker_api

charge_schema = ChargeSchema()

@worker_api.route('/charge')
class Charge(Resource):
    def put():
        charge = None
        return charge_schema.dump(charge)