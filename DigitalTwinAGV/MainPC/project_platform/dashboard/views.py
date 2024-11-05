from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def history(request):
    return render(request, 'dashboard/history.html')

def future(request):
    return render(request, 'dashboard/future.html')

