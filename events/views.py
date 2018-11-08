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

class MyEventListView(ListView):
    model = Event
    template_name = "myevent_list.html"
    context_object_name = "myevent_list"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(creator = seld.request.user)

class EventCreateView(CreateView):
    model = Event
    template_name = "event_create.html"
    fields = ['name', 'description', 'max_slots', 'date_from', 'date_to', 
               'time_from', 'time_to', 'venue']

    def form_valid(self, form):
        form.instance.creator = self.request.user   
        return super().form_valid(form)   

class EventUpdateView(UpdateView):
    model = Event
    template_name = "event_update.html"
    fields = ['name', 'description', 'max_slots', 'date_from', 'date_to', 
               'time_from', 'time_to', 'venue']