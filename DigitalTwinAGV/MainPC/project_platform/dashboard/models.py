from django.db import models

class JobHistory(models.Model):
    job_name = models.CharField(max_length=100)
    arrival = models.DateTimeField()
    due = models.DateTimeField()
    picked_at = models.CharField(max_length=10)
    placed_at = models.CharField(max_length=10)
    estimated_time = models.DurationField()
    actual_time = models.DurationField()
    delay = models.DurationField(null=True, blank=True)
    on_time = models.BooleanField(default=True)

    def __str__(self):
        return self.job_name
