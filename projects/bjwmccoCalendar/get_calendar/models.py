from django.db import models

class Appointment(models.Model):
    exchange_id = models.CharField(max_length=500, primary_key=True)
    subject = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    detail = models.TextField(default='N/A', blank=True)
    attendees = models.TextField(default='N/A', blank=True)
    def __str__(self):
        return self.subject

# Create your models here.
