from flask_restx import Resource, Namespace

from api.models import Inmate
from api.models.schemas import InmateSchema

inmate_schema = InmateSchema()
inmate_ns = Namespace('inmate')

@inmate_ns.route('/')
class Inmate(Resource):
    def put():
        inmate = None
        return inmate_schema.dump(inmate)