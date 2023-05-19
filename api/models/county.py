from sqlalchemy import Column, Integer, String, Enum
from geoalchemy2 import Geometry

from .shared import counties_jails
from api.shared.constants import State
from api import db

class County(db.Model):
    __tablename__ = 'counties'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    state = Column(Enum(State))
    geometry = Column(Geometry('MULTIPOLYGON'))
    located_jails = db.relationship('Jail', back_populates='located_county')
    # associated_jails = db.relationship(
    #     'Jail', secondary=counties_jails, back_populates='associated_counties'
    # )

    def __repr__(self) -> str:
        return f'County(id={self.id!r}, name={self.name!r}, abbreviation={self.abbreviation!r})'