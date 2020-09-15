from django.shortcuts import render
from .models import Sensor, State, Probability
from django.utils import timezone
import requests
from .bicubicinterpolatearr import do_color

# Create your views here.

def home(request):
    sensors = Sensor.objects.all().order_by('-id')[:5]
    states = State.objects.all().order_by('-state_num')[:5]
    probs = Probability.objects.all().order_by('-prob_id')[:1]
    context = {'sensors': sensors, 'states' : states, 'probs' : probs}
    return render(request, 'testapp/main.html', context=context)

def safety(request):
    return render(request, 'testapp/sobanganjeon.html', {})

def statistics(request):
    return render(request, 'testapp/statistics.html', {})

def location(request):
    return render(request, 'testapp/location.html', {})
    
def setting(request):
    return render(request, 'testapp/setting.html', {})

def popup(request):
    return render(request, 'testapp/popup.html', {})

def ifcam(request):
    ifcamlist = Sensor.objects.only('ifcam').order_by('-id')[0].ifcam
    pixel64list = do_color(ifcamlist)
    context = {'pixels':pixel64list}
    return render(request, 'testapp/ifcam.html', context=context)