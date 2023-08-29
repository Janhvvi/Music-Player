from django.urls import path
from . import views

urlpatterns = [
    path("", views.genre, name="home"),
    path("<str:name>", views.genre, name="home"),
]