from sqlalchemy import Column, ForeignKey, Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

counties_jails = Table(
    "countis_jails",
    db.metadata,
    Column("county_id", ForeignKey("counties.id"), primary_key=True),
    Column("jail_id", ForeignKey("jails.id"), primary_key=True),
)