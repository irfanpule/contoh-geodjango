from django.contrib.gis import admin
from .models import WorldBorder


class WorldGeoAdmin(admin.OSMGeoAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(WorldBorder, WorldGeoAdmin)
