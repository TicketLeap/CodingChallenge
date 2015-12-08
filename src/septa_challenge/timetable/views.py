from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models

def home(request):
    return render(request, 'main.html', {})

def render_json(request):	
	return JsonResponse({'key' : 'value'})
