from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import relationship
from base import Base
from api.constants import Gender, Race

class Inmate (Base):
    __tablename__ = 'inmates'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(Date)
    last_name = Column(String)
    book_id = Column(String)
    charges = relationship(
        "Charge", back_populates="inmate", cascade="all, delete-orphan"
    )
    race = Column('value', Enum(Race))
    gender = Column('value', Enum(Gender))
    date_of_birth = Column(Date)

    def __repr__(self) -> str:
        return f'Inmate(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, middle_name={self.middle_name!r})'

class Charge (Base):
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
    inmate = relationship("Inmate", back_populates="charges")

    def __repr__(self) -> str:
        return f'Charge(id={self.id!r})'
