from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    features = []
    places = Place.objects.all()
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat],
            },
            "properties": {
                "title": place.short_title,
                "placeId": place.place_id,
                "detailsUrl": reverse('place-detail', kwargs={'id': place.id})
            }
        })
    data = {
        "type": "FeatureCollection",
        "features": features,
    }
    return render(request, 'index.html', {
        'places_geojson': data
    })


def place_detail(request, id):
    place = get_object_or_404(Place, pk=id)
    imgs = [img.image.url for img in place.images.all()]
    data = {
        'title': place.title,
        'imgs': imgs,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }
    return JsonResponse(data)
