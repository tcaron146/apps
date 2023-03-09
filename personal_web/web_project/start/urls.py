from django.urls import path
from start import views

urlpatterns = [
    path("", views.home, name="home"),
]