from . import ma
from api.models import Jail, County

class JailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jail

class CountySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = County