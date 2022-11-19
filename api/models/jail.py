from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from geoalchemy2 import Geometry

from .shared import counties_jails
from api import db
from api.shared.constants import State 


class Jail(db.Model):
    __tablename__ = 'jails'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    short_name = Column(String)
    state = Column(Enum(State))
    location = Column(Geometry('POINT'))
    county_id = Column(Integer, ForeignKey('counties.id'))
    located_county = db.relationship(
        'County', back_populates='located_jails'
    )
    associated_counties = db.relationship(
        'County', secondary=counties_jails, back_populates='associated_jails'
    )

    def __repr__(self) -> str:
        return f'Jail(id={self.id!r}, name={self.name!r}, short_name={self.short_name!r})'