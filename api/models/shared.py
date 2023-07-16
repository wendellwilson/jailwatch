from sqlalchemy import Column, ForeignKey, Table
from api import db

counties_jails = Table(
    'counties_jails',
    db.metadata,
    Column('county_id', ForeignKey('counties.id'), primary_key=True),
    Column('jail_id', ForeignKey('jails.id'), primary_key=True),
)


class AuditableModel(db.Model):
    _absract_ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
