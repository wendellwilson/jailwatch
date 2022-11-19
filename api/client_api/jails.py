from flask_restx import Resource, Namespace

from api.models import Jail
from api.shared.schemas import JailSchema
from api.shared.constants import State

jail_schema = JailSchema()
jails_ns = Namespace('jails')

@jails_ns.route('/<region>')
class JailsRegion(Resource):
    def get(region):
        jails = Jail.query.all()
        return jail_schema.dump(jails)