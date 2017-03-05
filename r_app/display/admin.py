from django.contrib import admin

from .models import Location
from .models import Contact

class LocationAdmin(admin.ModelAdmin):
    list_display = ['location_title']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['desk_name']

admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)