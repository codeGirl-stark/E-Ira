from . import views
from django.urls import include, path

urlpatterns = [
    path('logListe/', views.logListe, name="logListe"),
]