from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape, from_shape
from marshmallow_sqlalchemy.convert import ModelConverter, fields
from shapely.geometry import mapping

from api import db, ma
from api.models import Jail, County, Charge, Inmate

class GeometryField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return mapping(to_shape(value))

    def _deserialize(self, value, attr, data, **kwargs):
        return from_shape(value)

class GeometryModelConverter(ModelConverter):
    SQLA_TYPE_MAPPING = {
        **ModelConverter.SQLA_TYPE_MAPPING,
        **{Geometry: GeometryField},
    }

class JailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jail
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
