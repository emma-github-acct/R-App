from django.db import models
from django.utils import timezone
time_help_text = "Military time only"

class UsefulLink(models.Model):
    link_title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    location_title = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE
    )

class ReportFlag(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __unicode__(self):
        return self.location
    
    def __str__(self):
        return self.location

class CalendarException(models.Model):
    title = models.CharField(max_length=30)
    location_title = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE
    )
    event_title = models.ForeignKey(
        "EventsCalendar",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    date = models.DateField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
class EventsCalendar(models.Model):
    #'location_title', 'event_title', 'room_id','date', 'opening_time', 'closing_time', 'event_information'
    location_title = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE
    )
    event_title = models.CharField(max_length=50)
    event_information = models.CharField(max_length=1000)
    date = models.DateField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    room_id = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.event_title
    
    def __str__(self):
        return self.event_title
    
class Contact(models.Model):
    desk_name = models.CharField(max_length=40)
    location_title = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE
    )
    contact_name = models.CharField(max_length=30)
    phone_number=models.CharField(max_length=10, help_text='Only input numbers, No Dash Marks')

    def __unicode__(self):
        return self.desk_name
    
    def __str__(self):
        return self.desk_name

class Location(models.Model):
    # Location - Fields
    location_title = models.CharField(max_length=20)
    map_id = models.IntegerField(default=0, unique=True)
    open_24_hours_for_students = models.BooleanField(default=False)
    monday_open = models.TimeField(help_text=time_help_text)
    monday_close = models.TimeField(help_text=time_help_text)
    tuesday_open = models.TimeField(help_text=time_help_text)
    tuesday_close = models.TimeField(help_text=time_help_text)
    wednesday_open = models.TimeField(help_text=time_help_text)
    wednesday_close = models.TimeField(help_text=time_help_text)
    thursday_open = models.TimeField(help_text=time_help_text)
    thursday_close = models.TimeField(help_text=time_help_text)
    friday_open = models.TimeField(help_text=time_help_text)
    friday_close = models.TimeField(help_text=time_help_text)
    saturday_open = models.TimeField(help_text=time_help_text)
    saturday_close = models.TimeField(help_text=time_help_text)
    sunday_open = models.TimeField(help_text=time_help_text)
    sunday_close = models.TimeField(help_text=time_help_text)
    
    def __unicode__(self):
        return self.location_title
    
    def __str__(self):
        return self.location_title