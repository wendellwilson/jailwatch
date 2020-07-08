##Inmate

##Charge

import mongoengine as me

class Jail(me.Document):
    name = me.StringField(required=True)
    location = me.PointField(required=True)
    state = me.StringField()