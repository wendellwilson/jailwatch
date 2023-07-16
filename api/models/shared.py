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

# Defines a list off attributes used to determine if two objects are the same
# and allows the pulling of a dict of those attributes used for queries
class UniqueAttributesMixin():
    def _unique_attrs(self):
        # If this is empty all attributes will be returned
        return []
        
    def _ambiguous_values(self):
        # Values to ignore for uniqueness comparison such as 'other' or 'all'
        return []

    def get_unique_attrs(self):
        # pull out attibutes that define a unique inmate
        if self._unique_attrs is []:
            return self.__dict__
        unique_attrs = {}
        for attr in self._unique_attrs():
            attr_value = getattr(self, attr)
            if attr_value and attr_value not in self._ambiguous_values():
                unique_attrs[attr] = attr_value
        return unique_attrs
    
    # This falls apart if we don't have enough populated fields
    def unique_equals(self, other, match_min = 2):
        # Only equal if we have match_min value matches
        match = 0
        if not (hasattr(other, 'get_unique_attrs') and callable(other.get_unique_attrs)):
            return False
        other_attr = self.get_unique_attrs()
        for key, value in self.get_unique_attrs():
            if key in other_attr.keys():
                if value == other_attr[key]:
                 match += 1
                else:
                    return False
        return match >= match_min
    
class UpdatableMixin():
    def _update_ignore():
        return []
    
    def _update_most_recent():
        return ['last_seen']
    
    def update(self, new_data):
        #TODO create a tag to check correctness when we mismatch values here
        updated = False
        ignore = self._update_ignore()
        most_recent = self._update_most_recent()
        #Update blank field or some dates if they are more recent
        for attr in self.__table__.columns.keys():
            if attr not in ignore and attr in new_data:
                if not getattr(self, attr) or (attr in most_recent and new_data[attr] > getattr(self, attr)):
                    setattr(self, attr, new_data[attr])
                    updated = True
        return updated