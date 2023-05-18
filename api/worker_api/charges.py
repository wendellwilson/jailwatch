from flask_restx import Resource, Namespace

from api.models import Charge
from api.models.schemas import ChargeSchema

charge_schema = ChargeSchema()
charge_ns = Namespace('charge')

@charge_ns.route('/')
class Charge(Resource):
    def put():
        charge = None
        return charge_schema.dump(charge)