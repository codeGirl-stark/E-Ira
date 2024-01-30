from django.contrib import admin
from .models import DossierMedical

# Register your models here.

class DossierMedicalAdmin(admin.ModelAdmin) :
    list_display = ('id', 'numDossier', 'identite', 'sexe', 'age', 'adresse', 'telephone', 'diagnostic', 'dateRdv', 'medecin')
    search_fields = ('numDossier', 'identite','diagnostic', 'medecin')
    list_filter = ('numDossier', 'medecin')
    
admin.site.register(DossierMedical, DossierMedicalAdmin)
