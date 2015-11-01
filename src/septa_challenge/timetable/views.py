from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import urllib
import json

from . import models

def home(request):
    query_params = request.GET

    context = {}
    context["stations"] = models.Station.objects.all()
    context["rows"] = False
    context["from_station"] = context["stations"][0].name # default values
    context["to_station"] = context["stations"][1].name

    if all (station in query_params for station in ("from_station","to_station")):
        try:
            schedule_json_arr = json_from_url(build_url_for_septa_call(query_params["from_station"],
                query_params["to_station"]))
            context["rows"] = build_rows(schedule_json_arr)
            context["column_names"] = ('Train Number',
                'Scheduled Departure time',
                'Scheduled Arrival time',
                'Train status/Delay',)
            context["from_station"] = query_params["from_station"]
            context["to_station"] = query_params["to_station"]
        except:
            context["error"] = "There was an error while processing your request. We apologize for the inconvenience."
            pass

    return render(request, 'main.html', context)

def json_from_url(url):
    return json.loads(urllib.urlopen(url).read())

def build_url_for_septa_call(from_station, to_station):
    base = 'http://www3.septa.org/hackathon/NextToArrive/'
    query_string = urllib.urlencode({ "req1" : format_station(from_station), "req2" : format_station(to_station)})
    return base + '?' + query_string

def format_station(station):
    return station.replace(' & ', '-').replace('Airport Terminals', 'Airport Terminal')

def build_rows(json_array):
    if not isinstance(json_array, list):
        # if 'error' in json_array:
        #     print json_array['error']
        raise TypeError('Expected a list!')

    return ((json_object['orig_train'],
        json_object['orig_departure_time'],
        json_object['orig_arrival_time'] if json_object['isdirect'] == 'true' else json_object['term_arrival_time'],
        json_object['orig_delay'])
        for json_object in json_array)
