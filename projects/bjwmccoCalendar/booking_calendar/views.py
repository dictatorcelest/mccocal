from django.shortcuts import render
from django.views import generic
from .models import Appointment
import datetime
from django.utils import timezone
from .sync_calendar import get_entry
from django.http import Http404


class HomeView(generic.ListView):
    template_name = 'booking_calendar/home.html'
    context_object_name = 'selected_period_items'
    def get_queryset(self):
        return Appointment.objects.filter(start_time__range=(timezone.now(), timezone.now()+ datetime.timedelta(days=15))).order_by('start_time')
    
def ItemDetailView(request, exchange_id):
    try:
        get_entry(exchange_id)
        selected_item = Appointment.objects.get(pk=exchange_id)
        template_name = 'booking_calendar/detail.html'
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist")
    return render(request, template_name, {'selected_item': selected_item})

# Create your views here.
