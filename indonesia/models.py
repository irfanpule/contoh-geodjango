from django.contrib.gis.db import models


class IndoBorder(models.Model):
    name_0 = models.CharField(max_length=80)
    name_1 = models.CharField(max_length=80)
    kode = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_1
