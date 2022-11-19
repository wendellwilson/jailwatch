from flask_restx import Resource

from api.models import Jail
from api.shared.schemas import JailSchema
from api.shared.constants import State
from . import client_api

jail_schema = JailSchema()

@client_api.route('/jails/<region>')
class JailsRegion(Resource):
    def get(region):
        jails = Jail.query.all()
        return jail_schema.dump(jails)