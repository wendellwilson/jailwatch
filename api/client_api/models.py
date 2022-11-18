##Inmate

##Charge

import mongoengine as me

class Jail(me.Document):
    name = me.StringField(required=True)
    location = me.PointField(required=True)
    state = me.StringField()

class County(me.Document):
    name = me.StringField(required=True)
    geometry = me.MultiPolygonField(required=True)