from models import Jail, County
import logging
from flask import Flask, request, Response
from flask_mongoengine import MongoEngine

logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "jailwatch",
}
db = MongoEngine(app)

@app.route('/jails/<state>')
def get_state_jails(state):
    jails = Jail.objects.to_json()
    return Response(jails, mimetype="application/json", status=200)

@app.route('/map/<state>')
def get_state_map(state):
    counties = County.objects().to_json()
    return Response(counties, mimetype="application/json", status=200)
