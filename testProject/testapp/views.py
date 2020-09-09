from django.shortcuts import render
from .models import Sensor, State, Probability
from django.utils import timezone
# Create your views here.

def home(request):
    sensors = Sensor.objects.all().order_by('-id')[:5]
    states = State.objects.all().order_by('-state_num')[:1]
    probs = Probability.objects.all().order_by('-prob_id')[:1]
    context = {'sensors': sensors, 'states' : states, 'probs' : probs}
    return render(request, 'testapp/메인화면.html', context=context)

def safety(request):
    return render(request, 'testapp/sobanganjeon.html', {})

def statics(request):
    return render(request, 'testapp/post_list.html', {})

def location(request):
    return render(request, 'testapp/location.html', {})

def setting(request):
    return render(request, 'testapp/setting.html', {})

def popup(request):
    return render(request, 'testapp/popup.html', {})