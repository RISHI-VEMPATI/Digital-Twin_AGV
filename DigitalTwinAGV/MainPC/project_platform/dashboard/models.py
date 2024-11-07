from django.db import models
from datetime import timedelta
from django.utils import timezone

def default_due_time():
    return timezone.now() + timedelta(minutes=20)

def default_pick_time():
    return timezone.now() + timedelta(minutes=9)

class JobHistory(models.Model):
    job_name = models.CharField(max_length=100)
    arrival = models.DateTimeField()
    due = models.DateTimeField()
    picked_at = models.CharField(max_length=10, default='none')
    placed_at = models.CharField(max_length=10, default='none')
    estimated_time = models.DurationField()
    actual_time = models.DurationField()
    delay = models.DurationField(null=True, blank=True)
    on_time = models.BooleanField(default=True)

    def __str__(self):
        return self.job_name
    
class Schedule(models.Model):
    job_name = models.CharField(max_length=100)
    arrival = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(default=default_due_time)
    pick_at = models.CharField(max_length=10, default='none')
    place_at = models.CharField(max_length=10, default='none')
    estimated_pickup_time = models.DateTimeField(default=default_pick_time)

    def __str__(self):
        return self.job_name
