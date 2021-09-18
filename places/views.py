from django.shortcuts import render

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
                "title": place.title_short,
                "placeId": place.place_id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        })
    data = {
        "type": "FeatureCollection",
        "features": features,
    }
    return render(request, 'index.html', {
        'places_geojson': data
    })
