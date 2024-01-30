from . import views
from django.urls import path

urlpatterns = [
    path('addDossier', views.addDossier, name="addDossier"),
    path('liste/', views.liste, name="liste"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('visiteJour/', views.visitesJour, name="visitesJour"),
    path('listeVisite/', views.listeVisite, name="listeVisite"),
    path('search', views.search, name="search"),
]
