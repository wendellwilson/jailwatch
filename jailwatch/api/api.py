from models import Jail
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
    jails = Jail.objects().to_json()
    return jails
