from django.shortcuts import render
from .models import Sensor, State, Probability
from django.utils import timezone
import requests
# Create your views here.

def home(request):
    sensors = Sensor.objects.all().order_by('-id')[:5]
    states = State.objects.all().order_by('-state_num')[:1]
    probs = Probability.objects.all().order_by('-prob_id')[:1]
    context = {'sensors': sensors, 'states' : states, 'probs' : probs}
    return render(request, 'testapp/main.html', context=context)

def safety(request):
    return render(request, 'testapp/sobanganjeon.html', {})

def statistics(request):
    return render(request, 'testapp/statistics.html', {})

def location(request):
    r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBGE4LjBk3a2Lsqi1CzGHAYInoWWZTOsSo', params=request.POST)
    
    if r.status_code == 200:
        context = {'location': r.text}
        return render(request, 'testapp/location.html', context=context)
    else:
        return render(request, 'testapp/location.html', {'location' : 'fail'})

def setting(request):
    return render(request, 'testapp/setting.html', {})

def popup(request):
    return render(request, 'testapp/popup.html', {})