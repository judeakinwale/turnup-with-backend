from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    home_template = 'home/index.html'
    context = {'event_name': 'EVENT'}
    return render(request, home_template, context)

def all_events(request):
    events = Event.objects.all()
    context = {'events': events}
    event_template = 'home/events.html'
    return render(request, event_template, context)

def about(request):
    about_template = 'home/about.html'
    return render(request, about_template)