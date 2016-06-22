from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

from . import models

def home(request):
    return render(request, 'main.html', {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})

def render_json(request):
    response = requests.get("http://www3.septa.org/hackathon/TransitViewAll")
    raw_data = response.json()

    # The data looks like:
    # {
    #   timestamp: [
    #       {
    #           routeName: [
    #               {infoForASingleVehicle},
    #               ...
    #           ],
    #       },
    #       ...,
    #   ]
    # }
    #
    # Transform it to a flat list of dicts

    data = []
    for list_elem in raw_data.values()[0]:
        route_name, vehicles = list_elem.items()[0]
        for vehicle in vehicles:
            data.append({
                'id': vehicle.get('VehicleID'),
                'lat': vehicle.get('lat'),
                'lng': vehicle.get('lng'),
                'dir': vehicle.get('Direction'),
                'dest': vehicle.get('destination')
            })

    return JsonResponse({'data': data})
