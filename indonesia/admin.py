from django.contrib.gis import admin
from .models import IndoBorder


class IndoGeoAdmin(admin.OSMGeoAdmin):
    list_display = ("name_1", "name_0")
    search_fields = ("name_1",)


admin.site.register(IndoBorder, IndoGeoAdmin)
