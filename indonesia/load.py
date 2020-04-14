import os
from django.contrib.gis.utils import LayerMapping
from .models import IndoBorder


# Auto-generated `LayerMapping` dictionary for IndoBorder model
indoborder_mapping = {
    'name_0': 'NAME_0',
    'name_1': 'NAME_1',
    'kode': 'KODE',
    'geom': 'MULTIPOLYGON',
}

indo_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'prov.shp')
)

def run(verbose=True):
    lm = LayerMapping(IndoBorder, indo_shp, indoborder_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)