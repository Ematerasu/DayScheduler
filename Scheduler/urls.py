from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("home/", views.home, name="home"),
    path("<str:id>", views.schedule, name="index"),
    path("contact/", views.contact, name="contact"),
]