from django.shortcuts import render, redirect
from django.http import Http404
from datetime import datetime, date
from django.utils import timezone

from display.models import Location
from display.models import Contact
from display.models import CalendarException
from display.models import UsefulLink
from .forms import ReportFlagForm

def report_flag(request):
    if request.method == "POST":
        form = ReportFlagForm(request.POST)
        if form.is_valid():
            flagmod = form.save(commit=True)
            flagmod.save()
            return redirect('index')
    else:
        form = ReportFlagForm()
    return render(request, 'display/report_flag.html', {
        'form': form
    })

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
        links = UsefulLink.objects.filter(location_title=location)
        exceptions = CalendarException.objects.filter(location_title=location)
        today = date.today()
        exceptions_today = CalendarException.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day, location_title=location)
    except Location.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'display/location_detail.html', {
        'location': location,
        'contacts': contacts,
        'exceptions': exceptions,
        'exceptions_today': exceptions_today,
        'links': links,
    })