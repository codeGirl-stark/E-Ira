from django.urls import path
from . import views

urlpatterns = [
    path('', views.connect, name="connect"),
    path("stat", views.stat, name="stat"),
    path('deconnect', views.deconnect, name="deconnect"),
]
