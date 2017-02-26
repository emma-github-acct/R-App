from django.contrib import admin

from .models import Location
from .models import Calendar

class LocationAdmin(admin.ModelAdmin):
    list_display = ['location_title']
      

admin.site.register(Location, LocationAdmin)
admin.site.register(Calendar)