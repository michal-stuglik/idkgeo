from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from geo.models import Point, Image
from django.http import JsonResponse
from django.core.serializers import serialize

import os


# from idkgeo.settings import BASE_DIR, STATIC_IMG


def thumb(request):
    if request.method == 'GET':
        img_name = request.GET.get('name')

        # img_dir = os.path.join(BASE_DIR, STATIC_IMG)

        # img = Image.objects.filter(path_name=os.path.join(STATIC_IMG, img_name))
        # serializer = PhotoSerializer(img, many=True)
        # return HttpResponse(serializer, status="200")

        # return render_to_response('image.html',variables)


def point(request):
    print("I am here")

    if request.method == 'GET':
        points = Point.objects.all()

        # images = Image.objects.filter(point_id=p.id).all()
        # return render(request=request, template_name='pop.html', context={'images': images})

        return render(request=request, template_name='point.json', context={'points': points})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
