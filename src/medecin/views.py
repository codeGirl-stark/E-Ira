from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from dossier.models import DossierMedical

from medecin.models import Medecin

# Create your views here.

def connect(request) :   
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        medecin = get_object_or_404(Medecin, username=username)
            
        if medecin.password == password :
            medecin.is_active = True
            medecin.save()
            return redirect('liste')
        else :
            return HttpResponse ("Mot de passe incorrect")

    return render(request, "connexion.html")


def stat (request) :
    
    age_ado = (0, 24)
    age_adultes = (25, 100)
    
    medecin = get_object_or_404(Medecin, is_active=True)
    patients = DossierMedical.objects.filter(medecin=medecin.id).count()
    homme = DossierMedical.objects.filter(medecin=medecin.id, sexe="M").count()
    femme = DossierMedical.objects.filter(medecin=medecin.id, sexe="F").count()
    ado = DossierMedical.objects.filter(age__range=age_ado).count()
    adulte = DossierMedical.objects.filter(age__range=age_adultes).count()



    if not patients :
        message = "Vous n'avez aucun patient pour le moment"
    else :
        message = ""
        
    context = {
        "message" : message,
        "patients" : patients,
        "homme" : homme,
        "femme" : femme,
        "ado": ado,
        "adulte": adulte,
    }

    return render(request, 'stat.html', context)


def deconnect(request) :
    medecin_actif = get_object_or_404(Medecin, is_active=True)
    medecin_actif.is_active = False
    medecin_actif.save()
    return redirect('connect')