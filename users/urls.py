from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("signu/", SignUpView.as_view(),name = "signup")
]
  