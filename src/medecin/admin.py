from django.contrib import admin
from .models import Medecin

# Register your models here.

class MedecinAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password', 'is_active')
    search_fields = ('username', 'password', 'is_active')
    list_filter = ('username', 'is_active')
    
admin.site.register(Medecin, MedecinAdmin)