# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Well

# Create your views here.


def charts(request):
    wellsList = Well.objects.all()
    names = []
    pressureValues = []
    temperatureValues = []
    for well in wellsList:
        names.append(well.name)
        pressureValues.append(well.pressureValue)
        temperatureValues.append(well.temperatureValue)
    context = {"wellsList": wellsList, 'names': names,
               'pressureValue': pressureValues, 'temperatureValue': temperatureValues}
    return render(request, "charts.html", context)


def wellDetails(request, well_id):
    well = get_object_or_404(Well, pk=well_id)
    context = {"well": well}
    return render(request, "details.html", context)
