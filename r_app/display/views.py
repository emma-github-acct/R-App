from django.shortcuts import render
from django.http import Http404
from datetime import datetime, date

from display.models import Location
from display.models import Contact
from display.models import CalendarException

def index(request):
    locations = Location.objects.all()
    today = date.today()
    exceptions_today = CalendarException.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    return render(request, 'display/index.html', {
        'locations': locations,
        'exceptions_today': exceptions_today,
    })

def location_detail(request, id):
    try:
        location = Location.objects.get(id=id)
        contacts = Contact.objects.filter(location_title=location)
        exceptions = CalendarException.objects.filter(location_title=location)
        today = date.today()
        exceptions_today = CalendarException.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    except Location.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'display/location_detail.html', {
        'location': location,
        'contacts': contacts,
        'exceptions': exceptions,
        'exceptions_today': exceptions_today,
    })