from django.shortcuts import render
from .models import Sensor, State, Probability, Sensitivity
from django.utils import timezone
import requests
from .bicubicinterpolatearr import do_color
import json

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
    sense_db = Sensitivity.objects.all().order_by('-sense_id')[0]
    sen_gas = sense_db.sense_gas
    sen_temp = sense_db.sense_temp
    context = {'sense_gas':sen_gas, 'sense_temp' : sen_temp}
    if request.method == 'POST':
        new_sense = Sensitivity()
        new_sense.sense_gas = request.POST['sense_gas']
        new_sense.sense_temp = request.POST['sense_temp']
        new_sense.save()
        context = {'sense_gas':new_sense.sense_gas, 'sense_temp' : new_sense.sense_temp}          
    return render(request, 'testapp/setting.html', context=context)

def popup(request):
    return render(request, 'testapp/popup.html', {})

def ifcam(request):
    ifcamlist = Sensor.objects.only('ifcam').order_by('-id')[0].ifcam
    pixel64list = do_color(ifcamlist)
    context = {'pixels':json.dumps(pixel64list)}
    return render(request, 'testapp/ifcam.html', context=context)