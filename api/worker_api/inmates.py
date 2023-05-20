from flask_restx import Resource, Namespace

from api.models import Inmate
from api.models.schemas import InmateSchema
from api import db

inmate_schema = InmateSchema()
inmate_ns = Namespace('inmate')

@inmate_ns.route('/')
class Inmate(Resource):
    def put(self, inmateData):
        try:
            inmate = InmateSchema.load(partial=True)
            update = True
            #check if inmate exists
            matching_inmates = Inmate.query.filter(**inmate.get_unique_attrs()).all()
            if matching_inmates.length > 1:
                #TODO this should createa a dedup task
                return "multiple inmates matching found", 500
            elif matching_inmates.length == 1:
                #TODO do we need some kind of trusted source or data stamp to provide info preference
                update = matching_inmates[0].update(inmate)
                inmate = matching_inmates[0]
                
            if update:
                db.session.add(inmate)
                db.session.commit()
        except:
            return "Invalid inmate data", 400
        return inmate_schema.dump(inmate), 200