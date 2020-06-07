from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def point(request):
    # make geojson file and send

    return HttpResponse("geojson will be here")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
