from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplatelateView, ListView, DetailView
from .models import Event

class HomePageView(TemplateView):
    template_name = "home.html"

class EventListVIew(LIstView):
    model = Event
    template_name = "event_list.html"
    
class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"
    