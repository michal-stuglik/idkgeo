from django.contrib.gis import admin
from geo.models import Point, Image, Film


class LocationAdmin(admin.GeoModelAdmin):
    # openlayers_url = (
    #     'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'
    # )
    # spherical_mercator_srid =     4326
    default_zoom = 13
    default_lon = 22.71  # 2532778  # 22.71
    default_lat = 49.15  # 6294764  # 49.15
    map_width = 800
    map_height = 600
    display_wkt = True


admin.site.register(Point, LocationAdmin)
admin.site.register(Image, admin.OSMGeoAdmin)
admin.site.register(Film, admin.OSMGeoAdmin)
