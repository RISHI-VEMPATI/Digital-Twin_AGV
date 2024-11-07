from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.history, name='history'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),

]

