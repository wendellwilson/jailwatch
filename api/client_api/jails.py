from flask_restx import Resource, Namespace
from api.models import Jail
from api.models.schemas import JailSchema
from api.shared.constants import State

jail_schema = JailSchema(many=True)
jails_ns = Namespace('jails')

@jails_ns.route('/<region>')
class JailsRegion(Resource):
    def get(self, region):
        region = region.upper()
        try:
            jails = Jail.query.filter(Jail.state == State(region))
        except:
            return f'{region} is not a valid state', 400
        return jail_schema.dump(jails), 200