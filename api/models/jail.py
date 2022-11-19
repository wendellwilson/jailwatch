from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from .shared import counties_jails,db
from api.shared.constants import State 


class Jail (db.Model):
    __tablename__ = "jails"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    short_name = Column(String)
    state = Column('value', Enum(State))
    location = Column(Geometry('POINT'))
    county_id = Column(Integer, ForeignKey("counties.id"))
    location_county = relationship(
        relationship("County", back_populates="location_jails")
    )
    associated_counties: relationship(
        "County", secondary=counties_jails, back_populates="jails"
    )

    def __repr__(self) -> str:
        return f"Jail(id={self.id!r}, name={self.name!r}, short_name={self.short_name!r})"