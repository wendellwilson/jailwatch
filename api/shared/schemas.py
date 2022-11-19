from geoalchemy2.types import Geometry
from marshmallow_sqlalchemy.convert import ModelConverter, fields

from api import db, ma
from api.models import Jail, County, Charge, Inmate




class GeometryModelConverter(ModelConverter):
    SQLA_TYPE_MAPPING = {
        **ModelConverter.SQLA_TYPE_MAPPING,
        **{Geometry: fields.Str},
    }


class JailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jail
        sqla_session = db.session
        model_converter = GeometryModelConverter

class CountySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = County
        sqla_session = db.session
        model_converter = GeometryModelConverter

class InmateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inmate
        sqla_session = db.session

class ChargeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Charge
        sqla_session = db.session
