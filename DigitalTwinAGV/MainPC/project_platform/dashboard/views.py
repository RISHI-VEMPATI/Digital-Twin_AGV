from django.shortcuts import render
from django.http import HttpResponse
from .models import JobHistory, Schedule
import random
import os,json
from  django.conf import settings

# Create your views here.
def dashboard(request):
    agv_position = random.randint(0, 100)
    return render(request, 'dashboard/dashboard.html', {'agv_position': agv_position})

def history(request):
    jobs = JobHistory.objects.all()
    return render(request, 'dashboard/history.html', {'jobs': jobs})

def schedule(request):
    coming_jobs = Schedule.objects.all()
    return render(request, 'dashboard/schedule.html', {'coming_jobs': coming_jobs})

def about(request):
    file_path = os.path.join(settings.BASE_DIR,'dummy', 'static_data.json')
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    # Convert the JSON data to a formatted string
    json_string = json.dumps(json_data, indent=4)
    
    return render(request, 'dashboard/about.html', {'json_data': json_string})
    

