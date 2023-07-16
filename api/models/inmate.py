from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import class_mapper, ColumnProperty
from api.shared.constants import Gender, Race
from api import db
from .shared import AuditableModel

class Inmate(AuditableModel):
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

    def get_unique_attrs(self):
        # pull out attibutes that define a unique inmate
        unique_attrs = {}
        for attr in self.UNIQUE_ATTR:
            attr_value = getattr(self, attr)
            if attr_value and attr_value not in self.AMBIGUOUS_VALUES:
                unique_attrs[attr] = attr_value
        return unique_attrs
        
    def update(self, new_data):
        #TODO create a tag to check correctness when we mismatch values here
        updated = False
        #TODO always update last scraped if more recent
        for attr in self.__table__.columns.keys():
            if attr in new_data and not getattr(self, attr):
                setattr(self, attr, new_data[attr])
                updated = True
        #TODO check charges
        return updated

    def __repr__(self) -> str:
        return f'Inmate(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, middle_name={self.middle_name!r})'

class Charge(db.Model):
    __tablename__ = 'charges'

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

    def __repr__(self) -> str:
        return f'Charge(id={self.id!r})'
