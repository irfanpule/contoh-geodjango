import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WorldBorder


def index(request):
    return render(request, 'world/index.html', {
        'worlds': WorldBorder.objects.all(),
        'title': 'Peta Dunia'
    })


def country(request, id):
    world = get_object_or_404(WorldBorder, id=id)
    return JsonResponse({
        'geojson': json.loads(world.mpoly.geojson),
        'name': world.name
    })
