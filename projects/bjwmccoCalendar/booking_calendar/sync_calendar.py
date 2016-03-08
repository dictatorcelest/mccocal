'''
Created on Mar 8, 2016

@author: chcu
'''
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
#from _datetime import datetime, date
import datetime
from pytz import timezone
from .models import Appointment
#from django.utils.html import escape

#from datetime import timedelta


URL = u'https://apj.064d.cloudmail.microsoft.com/EWS/Exchange.asmx'
USERNAME = u'FAREAST\\bjwmcco'
PASSWORD = u'FEB.2016-02'

def sync(StartTime, EndTime):#Use timezone("Asia/Shanghai").localize(datetime.datetime(2016,2,1,0,0,0)) to set the event start time and end time value.
    connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)

    service = Exchange2010Service(connection)
    #print(service.calendar())

    eventsList = service.calendar().list_events(
                                                start=StartTime,
                                                end=EndTime,
                                                details=True
                                                )
    count = 0
    for event in eventsList.events:
        appointment = Appointment (
                                   exchange_id = event.id,
                                   subject = event.subject,
                                   start_time = event.start,
                                   end_time = event.end,
                                   #detail = event.html_body,
                                   #attendees = models.TextField(blank=True)
                                   )
        appointment.save()
        count += 1
    return count

def get_entry(ExchangeID):#ExchangeID should be the key from exchange server to identify a calendar item.
    connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)

    service = Exchange2010Service(connection)
    event = service.calendar().get_event(ExchangeID)
    appointment = Appointment (
                                   exchange_id = event.id,
                                   subject = event.subject,
                                   start_time = event.start,
                                   end_time = event.end,
                                   detail = event.html_body,
                                   #attendees = event.attendees
                                   )
    appointment.save()
    return event.subject
    
'''
    print ("{start} {stop} - {subject}".format(
                                             start=event.start,
                                             stop=event.end,
                                             subject=event.subject
                                             ))


event = service.calendar().new_event(
                                     subject=u"Python test",
                                     attendees=[u'chcu@microsoft.com'],
                                     location=u"My house",
                                     )
event.start = timezone("Asia/Shanghai").localize(datetime.datetime(2016,3,5,15,30,0))
event.end = timezone("Asia/Shanghai").localize(datetime.datetime(2016,3,5,16,30,0))

event.create()

print(event.id)
'''
'''
event = service.calendar().get_event('AAAVAGJqd21jY29AbWljcm9zb2Z0LmNvbQBGAAAAAACaI3n7aDKWSqTPifl3gWLVBwAzAX97lqHaRo+2sFckqKT+AAAADQdmAAC39ha9qM5vQIYrtMvuQOK9AADm2xWYAAA=')
event.cancel()
'''