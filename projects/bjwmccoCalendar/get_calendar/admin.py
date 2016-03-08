from django.contrib import admin
from .models import Appointment
from .sync_calendar import sync
import datetime
from pytz import timezone

StartTime = timezone("Asia/Shanghai").localize(datetime.datetime.now())
EndTime = timezone("Asia/Shanghai").localize(datetime.datetime.now()+datetime.timedelta(days=30))

sync(StartTime, EndTime)
class AppointmentAdmin(admin.ModelAdmin):
    fields = ['subject', 'start_time', 'end_time']
    
admin.site.register(Appointment, AppointmentAdmin)
# Register your models here.
