from django.contrib import admin

from .models import Location
from .models import Contact
from .models import CalendarException
from .models import EventsCalendar

class LocationAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'map_id', 'monday_open', 'monday_close', 'tuesday_open', 'tuesday_close', 'wednesday_open', 'wednesday_close', 'thursday_open', 'thursday_close', 'friday_open', 'friday_close', 'saturday_open', 'saturday_close', 'sunday_open', 'sunday_close']

class ContactAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'desk_name', 'contact_name', 'phone_number']

class EventsCalendarAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'event_title', 'room_id','date', 'opening_time', 'closing_time', 'event_information']
    
class CalendarExceptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'location_title', 'date', 'opening_time', 'closing_time']

admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(EventsCalendar, EventsCalendarAdmin)
admin.site.register(CalendarException, CalendarExceptionAdmin)
