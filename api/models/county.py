from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from base import Base, counties_jails
from api.constants import State

class County (Base):
    __tablename__ = 'counties'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    short_name = Column(String)
    state = Column('value', Enum(State))
    geometry = Column(Geometry('POLYGON'))
    location_jails = relationship('Jail', back_populates='location_county')
    jails: relationship(
        'Jail', secondary=counties_jails, back_populates='counties'
    )

    def __repr__(self) -> str:
        return f'County(id={self.id!r}, name={self.name!r}, short_name={self.short_name!r})'