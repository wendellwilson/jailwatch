from flask_restx import Resource, Namespace

from api.models import County
from api.models.schemas import CountySchema
from api.shared.constants import State

county_schema = CountySchema(many=True)
counties_ns = Namespace('counties')

@counties_ns.route('/<region>')
class CountiesRegion(Resource):
    def get(self, region):
        region = region.upper()
        try:
            counties = County.query.filter(County.state == State(region))
        except:
            return f'{region} is not a valid state', 400
        return county_schema.dump(counties), 200