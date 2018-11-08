from django.urls import path

from .views import MyEventListView, HomePageView, EventListView, EventDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("events/", EventListView.as_view(), name="event_list")
    path("events/my/", MyEventListView.as_view(), name="myevent_list")
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail")

]