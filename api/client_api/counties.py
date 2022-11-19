from flask_restx import Resource, Namespace

from api.models import County
from api.shared.schemas import CountySchema
from api.shared.constants import State

county_schema = CountySchema()
counties_ns = Namespace('counties')

@counties_ns.route('/<region>')
class CountiesRegion(Resource):
    def get(region):
        counties = County.query.all()
        return county_schema.dump(counties)