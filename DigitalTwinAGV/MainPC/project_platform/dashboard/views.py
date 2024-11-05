from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def dashboard(request):
    agv_position = random.randint(0, 100)
    return render(request, 'dashboard/dashboard.html', {'agv_position': agv_position})

def history(request):
    return render(request, 'dashboard/history.html')

def future(request):
    return render(request, 'dashboard/future.html')

