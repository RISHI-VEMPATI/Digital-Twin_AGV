from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login_page(request):
    return render(request, 'users/login.html')

def register_page(request):
    return render(request, 'users/register.html')

