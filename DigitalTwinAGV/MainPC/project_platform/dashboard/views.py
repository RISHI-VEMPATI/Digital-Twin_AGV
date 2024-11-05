from django.shortcuts import render
from django.http import HttpResponse
from .models import JobHistory

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def history(request):
    jobs = JobHistory.objects.all()
    return render(request, 'dashboard/history.html', {'jobs': jobs})

def future(request):
    return render(request, 'dashboard/future.html')

