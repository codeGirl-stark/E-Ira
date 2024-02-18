from django.shortcuts import get_object_or_404, render
from medecin.models import Medecin
from .models import Log

# Create your views here.

def logListe (request) :
    medecin = get_object_or_404(Medecin, is_active=True)
    logs = Log.objects.filter(medecin=medecin.id)
    
    return render(request, "listelog.html", {"logs" : logs})

