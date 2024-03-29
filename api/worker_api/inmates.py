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
            #check if inmate exists
            matching_inmates = Inmate.query.filter(**inmate.get_unique_attrs()).all()
            #check for duplicate
            if matching_inmates.length > 1:
                #TODO this should create a dedup task
                return "multiple inmates matching found", 500
            elif matching_inmates.length == 1:
                #TODO do we need some kind of trusted source or data stamp to provide info preference
                updated_inamate = matching_inmates[0]
                if updated_inamate.update(inmate):
                    db.session.add(updated_inamate)
                # now check all the charges
                for charge in inmate.charges:
                    charge.last_seen = inmate.last_seen
                    charge_updated = False
                    for updated_charge in updated_inamate.charges:
                        if updated_charge.unique_equals(charge):
                            updated_charge.update(charge)
                            charge_updated = True
                    if not charge_updated:
                        updated_charge.append(charge)
                    db.session.add(updated_charge)
            db.session.commit()
        except:
            return "Invalid inmate data", 400
        return inmate_schema.dump(inmate), 200