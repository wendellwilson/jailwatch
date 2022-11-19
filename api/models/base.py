from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Table

Base = declarative_base()

counties_jails = Table(
    "countis_jails",
    Base.metadata,
    Column("county_id", ForeignKey("counties.id"), primary_key=True),
    Column("jail_id", ForeignKey("jails.id"), primary_key=True),
)