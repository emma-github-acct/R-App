from django.contrib import admin

from .models import Location
from .models import Contact
from .models import NormalHours
from .models import ExceptionsCalendar
from .models import EventsCalendar

class LocationAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'map_id', 'monday_open', 'monday_close', 'tuesday_open', 'tuesday_close', 'wednesday_open', 'wednesday_close', 'thursday_open', 'thursday_close', 'friday_open', 'friday_close', 'saturday_open', 'saturday_close', 'sunday_open', 'sunday_close']

class ContactAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'desk_name', 'contact_name', 'phone_number', 'fax_number']

class NormalHoursAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'day_id', 'opening_time', 'closing_time']

class ExceptionsCalendarAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'event_title', 'date', 'opening_time', 'closing_time']

class EventsCalendarAdmin(admin.ModelAdmin):
	list_display = ['location_title', 'event_title', 'room_id','date', 'opening_time', 'closing_time', 'event_information']

admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(NormalHours, NormalHoursAdmin)
admin.site.register(ExceptionsCalendar, ExceptionsCalendarAdmin)
admin.site.register(EventsCalendar, EventsCalendarAdmin)
