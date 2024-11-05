from django.contrib import admin
from .models import JobHistory, Schedule
# Register your models here.

admin.site.register(JobHistory)
admin.site.register(Schedule)