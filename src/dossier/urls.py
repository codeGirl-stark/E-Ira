from . import views
from django.urls import path

urlpatterns = [
    path('addDossier', views.addDossier, name="addDossier"),
    path('liste/', views.liste, name="liste"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('visiteJour/', views.visitesJour, name="visitesJour"),
    path('search', views.search, name="search"),
    path('rechercheVisite', views.rechercheVisite, name="rechercheVisite"),
    path('export', views.export, name="export"),
    path('export_to_csv', views.export_to_csv, name="export_to_csv"),
    path('export_to_sqlite', views.export_to_sqlite, name="export_to_sqlite"),
]
