from django.contrib import admin

from .models import Log

# Register your models here.

class LogAdmin(admin.ModelAdmin) :
    list_display = ('id', 'date', 'libelle', 'medecin')
    search_fields = ('date', 'libelle', 'medecin__nom')
    list_filter = ('date', 'medecin')
    
admin.site.register(Log, LogAdmin)
