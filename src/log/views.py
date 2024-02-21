from django.shortcuts import get_object_or_404, redirect, render
from medecin.models import Medecin
from .models import Log

# Create your views here.

def logListe (request) :
    medecin = get_object_or_404(Medecin, is_active=True)
    logs = Log.objects.filter(medecin=medecin.id)
    
    if request.method == "POST" :
        if "delete" in request.POST :
            ident = request.POST.get("delete")
            log = get_object_or_404(Log, id=ident)
            return render(request, "deleteLog.html", {'log': log})
        elif "supprimer" in request.POST :
            return render(request, "confirmation.html")
        
    return render(request, "listelog.html", {"logs" : logs})


def deleteLog (request, id):
    log = get_object_or_404(Log, id=id)
    log.delete()
    
    return redirect('logListe')


def supprimer (request):
    logs = Log.objects.all()
    logs.delete()
    
    return redirect('logListe')
