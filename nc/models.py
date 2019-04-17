from django.db import models
from jailwatch.base_models import *


class NcPIO(PIO):  # Public Information Officer
    pass


class NcSheriff(Sheriff):
    pass


class NcJail(Jail):
    pio = models.OneToOneField(NcPIO, on_delete=models.SET_NULL, null=True)


class NcCounty(County):
    jails = models.ManyToManyField(NcJail)
    sheriff = models.OneToOneField(NcSheriff, on_delete=models.SET_NULL, null=True)
