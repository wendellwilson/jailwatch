from flask_restx import Resource

from api.models import County
from api.shared.schemas import CountySchema
from api.shared.constants import State
from . import client_api

county_schema = CountySchema()

@client_api.route('/counties/<region>')
class CountiesRegion(Resource):
    def get(region):
        counties = County.query.all()
        return county_schema.dump(counties)