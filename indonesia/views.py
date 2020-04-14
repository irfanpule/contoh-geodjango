import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import IndoBorder


def index(request):
    return render(request, 'indonesia/index.html', {
        'indo_borders': IndoBorder.objects.all(),
        'title': 'Peta Indonesia'
    })


def provinsi(request, id):
    prov = get_object_or_404(IndoBorder, id=id)
    return JsonResponse({
        'geojson': json.loads(prov.geom.geojson),
        'name': prov.name_1
    })

