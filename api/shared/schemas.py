from api import db, ma
from api.models import Jail, County, Charge, Inmate

class JailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jail
        load_instance = True
        sqla_session = db.session

class CountySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = County
        load_instance = True
        sqla_session = db.session

class InmateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inmate
        load_instance = True
        sqla_session = db.session

class ChargeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Charge
        load_instance = True
        sqla_session = db.session
