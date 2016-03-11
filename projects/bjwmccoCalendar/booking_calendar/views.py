from django.shortcuts import render
from django.views import generic
from .models import Appointment
import datetime
from django.utils import timezone
from .sync_calendar import get_entry
from django.http import Http404
from pytz import timezone
from django.core import serializers


def CurrentMonthView(request):
    try:
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        next_month = month+1
        current_month_appointment = Appointment.objects.filter(start_time__range = (timezone('Asia/Shanghai').localize(datetime.datetime(year, month, 1, 0,0,0)), timezone('Asia/Shanghai').localize(datetime.datetime(year, next_month, 1, 0,0,0))))
        template_name ='booking_calendar/home.html'
        selected_period_items = serializers.serialize("json", current_month_appointment)
    except Appointment.DoesNotExist:
        raise Http404 ("Appointment does not exist")
    return render(request, template_name, {'selected_period_items': selected_period_items})

class HomeView(generic.ListView):
    template_name = 'booking_calendar/home.html'
    context_object_name = 'selected_period_items'
    def get_queryset(self):
        return Appointment.objects.filter(start_time__range=(timezone.now(), timezone.now()+ datetime.timedelta(days=15))).order_by('start_time')

class CalendarView(generic.ListView):
    template_name = 'booking_calendar/calendar.html'
    #context_object_name = 'selected_period_items'
    #def get_queryset(self):
        #return Appointment.objects.filter(start_time__range=(timezone.now(), timezone.now()+ datetime.timedelta(days=15))).order_by('start_time')
       
def ItemDetailView(request, exchange_id):
    try:
        get_entry(exchange_id)
        selected_item = Appointment.objects.get(pk=exchange_id)
        template_name = 'booking_calendar/detail.html'
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist")
    return render(request, template_name, {'selected_item': selected_item})


    # Create your views here.
