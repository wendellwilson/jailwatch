from api.models import County
from flask import Response, Blueprint
from api.shared.constants import State

map_blueprint = Blueprint('map', __name__)

@map_blueprint.route('/<state>')
def get_state_map(state):
    counties = County.objects().to_json()
    return Response(counties, mimetype="application/json", status=200)
