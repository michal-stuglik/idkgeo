import os
from uuid import uuid4

from django.contrib.gis.db import models
from django.utils.deconstruct import deconstructible
from easy_thumbnails.fields import ThumbnailerImageField


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)

        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class Point(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=2500)
    geo = models.PointField(srid=4326)  # wgs84
    created = models.DateTimeField(auto_now_add=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    url = ThumbnailerImageField(upload_to=UploadToPathAndRename(""), null=False)

    point = models.ForeignKey(to=Point, on_delete=models.SET_NULL, null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    point = models.ForeignKey(to=Point, on_delete=models.SET_NULL, null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name
