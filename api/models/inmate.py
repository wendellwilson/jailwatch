from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import class_mapper, ColumnProperty
from api.shared.constants import Gender, Race
from api import db
from .shared import AuditableModel, UpdatableMixin, UniqueAttributesMixin

class Inmate(AuditableModel, UpdatableMixin, UniqueAttributesMixin):
    __tablename__ = 'inmates'

    UNIQUE_ATTR = [
        'first_name',
        'last_name',
        'race',
        'gender',
        'date_of_birth']
    
    AMBIGUOUS_VALUES = [Gender.OTHER.value, Race.OTHER.value]

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    book_id = Column(String)
    charges = db.relationship(
        'Charge', back_populates='inmate'
    )
    race = Column(Enum(Race))
    gender = Column(Enum(Gender))
    date_of_birth = Column(Date)
    #Last time a scraper saw a record for this inmate
    last_seen = Column(Date)
    #TODO Maybe we need a duplicate prevention flag of some sort
    #TODO We should have a duplicates reference

    def _unique_attrs(self):
        return self.UNIQUE_ATTR
        
    def _ambiguous_values(self):
        return self.AMBIGUOUS_VALUES

    def __repr__(self) -> str:
        return f'Inmate(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, middle_name={self.middle_name!r})'

class Charge(AuditableModel, UpdatableMixin, UniqueAttributesMixin):
    __tablename__ = 'charges'

    UNIQUE_ATTR = [
        'date_charged',
        'agency',
        'inmate_id',
        'statute'
    ]

    id = Column(Integer, primary_key=True)
    date_confined = Column(Date)
    date_charged = Column(Date)
    date_released = Column(Date)
    statute = Column(String)
    bond_type = Column(String)
    bond_amount = Column(Integer)
    court_docket = Column(String)
    days_charge = Column(Integer)
    agency = Column(String)
    description = Column(String)
    inmate_id = Column(Integer, ForeignKey('inmates.id'))
    #Last time a scraper saw a record for this charge
    last_seen = Column(Date)
    inmate = db.relationship('Inmate', back_populates='charges')

    def _unique_attrs(self):
        return self.UNIQUE_ATTR

    def __repr__(self) -> str:
        return f'Charge(id={self.id!r})'
