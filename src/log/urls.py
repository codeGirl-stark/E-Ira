from . import views
from django.urls import include, path

urlpatterns = [
    path('logListe/', views.logListe, name="logListe"),
    path('deleteLog/<int:id>/', views.deleteLog, name="deleteLog"),
    path('supprimer/', views.supprimer, name="supprimer"),
]