import os
from uuid import uuid4

from django.contrib.gis.db import models
from django.utils.deconstruct import deconstructible
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from idkgeo.settings import SITE_URL


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

    @property
    def film_in_list(self):
        return [image_link(im) for im in Film.objects.filter(point_id=self.id).all()]

    @property
    def images_in_list(self):
        return [image_link(im) for im in Image.objects.filter(point_id=self.id).all()]

    @property
    def film_content(self):
        return """<div class='divVid'>{}</div>""".format("".join(self.film_in_list))

    @property
    def images_content(self):
        return """<div class='divImg'>{}</div>""".format("".join(self.images_in_list))

    @property
    def coordinates(self):
        return self.geo.x, self.geo.y

    @property
    def pop_content(self):
        return """<div><h3>{}</h3>{}{}{}</div>""".format(self.name,
                                                         self.images_content,
                                                         self.film_content,
                                                         self.description)


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


def make_url(site_url, image_str):
    return str(site_url).rstrip("/") + "/" + str(image_str).lstrip("/")


def image_link(img: Image):
    options = {'size': (100, 100), 'crop': True}
    thumb_url = get_thumbnailer(img.url).get_thumbnail(options).url

    full_image, thumb_image = make_url(SITE_URL, str(img.url)), make_url(SITE_URL, thumb_url)
    return "<a target='_blank' href='{}'><img class='aImg' src='{}'/></a>".format(full_image, thumb_image)
