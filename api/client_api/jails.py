from api.models import Jail
from flask import Response, Blueprint
from api.shared.constants import State

jails_blueprint = Blueprint('jails', __name__)

@jails_blueprint.route('/<state>')
def get_state_jails(state):
    jails = Jail.objects.to_json()
    return Response(jails, mimetype="application/json", status=200)