from django.shortcuts import render
from django.http import HttpResponse
from .models import JobHistory, Schedule
import random

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
    
    return render(request, 'dashboard/about.html')

