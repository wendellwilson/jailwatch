from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import *
from django.core.serializers import serialize
from html import unescape
from djgeojson.views import GeoJSONLayerView

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['county_map'] = serialize('geojson', NcCounty.objects.only('name', 'border'),
                                          geometry_field='border', fields=['name',])
        context['jail_loc'] = serialize('geojson', NcJail.objects.all(),
                                          geometry_field='location')

        return context