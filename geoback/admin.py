from django.contrib.gis import admin
from .models import Point, Image, Film


class LocationAdmin(admin.GeoModelAdmin):
    openlayers_url = (
        'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'
    )
    # spherical_mercator_srid =     4326
    default_zoom = 13
    default_lon = 2532778  # 22.71
    default_lat = 6294764  # 49.15
    map_width = 800
    map_height = 600
    # map_srid = 4326
    display_wkt = True
    # map_template = 'gis/admin/osm.html'
    # map_template = 'gis/admin/openlayers_extralayers.html'


admin.site.register(Point, LocationAdmin)
admin.site.register(Image, admin.OSMGeoAdmin)
admin.site.register(Film, admin.OSMGeoAdmin)
