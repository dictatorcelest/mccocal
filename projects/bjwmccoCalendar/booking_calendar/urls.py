'''
Created on Mar 8, 2016

@author: chcu
'''
from django.conf.urls import url
from booking_calendar import views

app_name = 'booking_calendar'
urlpatterns = [
               url(r'^$', views.HomeView.as_view(), name='home'),
               url(r'^(?P<exchange_id>[A-Za-z0-9+/=]+)/$', views.ItemDetailView, name='detail'),
               ]