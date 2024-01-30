from datetime import datetime, timedelta
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from dossier.models import DossierMedical
from medecin.models import Medecin

# Create your views here.

def prochain_mercredi(date_rdv):
    input_date = datetime.strptime(date_rdv, '%Y-%m-%dT%H:%M')

    # Calculer les jours restants jusqu'au mercredi suivant
    jours_jusquau_mercredi = (2 - input_date.weekday() + 7) % 7

    # Ajouter la durée nécessaire pour atteindre le mercredi suivant
    prochain_mercredi = input_date + timedelta(days=jours_jusquau_mercredi)

    return input_date == prochain_mercredi



def addDossier (request) :
    ageDepart = 0
    day = datetime.now()
    medecin_actif = Medecin.objects.filter(is_active=True).first()

    
    if request.method == "POST" :
        if 'add' in request.POST :
            num = request.POST.get('num')
            identite = request.POST.get('identite')
            sexe = request.POST.get('sexe')
            dateNais = request.POST.get('nais')
            age = (int(day.year) - int(dateNais))
            adresse = request.POST.get('adresse')
            phone = request.POST.get('phone')
            diagnostic = request.POST.get('diagnostic')
            cure1 = request.POST.get('cure1')
            cure2 = request.POST.get('cure2')
            cure3 = request.POST.get('cure3')
            cure4 = request.POST.get('cure4')
            cure5 = request.POST.get('cure5')
            bilan1 = request.POST.get('bilan1')
            bilan2 = request.POST.get('bilan2')
            bilan3 = request.POST.get('bilan3')
            bilan4 = request.POST.get('bilan4')
            bilan5 = request.POST.get('bilan5')
            bilan6 = request.POST.get('bilan6')
            bilan7 = request.POST.get('bilan7')
            bilan8 = request.POST.get('bilan8')
            bilan9 = request.POST.get('bilan9')
            bilan10 = request.POST.get('bilan10')
            defrenation1 = request.POST.get('defrenation1')
            defrenation2 = request.POST.get('defrenation2')
            defrenation3 = request.POST.get('defrenation3')
            defrenation4 = request.POST.get('defrenation4')
            defrenation5 = request.POST.get('defrenation5')
            examComp1 = request.POST.get('examen1')
            examComp2 = request.POST.get('examen2')
            examComp3 = request.POST.get('examen3')
            examComp4 = request.POST.get('examen4')
            examComp5 = request.POST.get('examen5')
            examComp6 = request.POST.get('examen6')
            examComp7 = request.POST.get('examen7')
            examComp8 = request.POST.get('examen8')
            examComp9 = request.POST.get('examen9')
            examComp10 = request.POST.get('examen10')
            resume = request.POST.get('resume')
            dateRDV = request.POST.get('dateRDV')
            
            dossier = DossierMedical.objects.filter(numDossier=num).first()
            date_obj = datetime.strptime(dateRDV, '%Y-%m-%dT%H:%M')
            

            if dossier :
                messages.error(request, f"Le dossier avec le numéro matricule {num} existe déjà.")
                return render(request, 'messageDossier.html', context={'messages': messages.get_messages(request)})
            else :
                if day < date_obj :
                    
                    if prochain_mercredi(dateRDV) :
                        dossier = DossierMedical(
                            numDossier=num,
                            identite=identite,
                            sexe=sexe,
                            age=age,
                            adresse=adresse,
                            telephone=phone,
                            diagnostic=diagnostic,
                            cure1=cure1,
                            cure2=cure2,
                            cure3=cure3,
                            cure4=cure4,
                            cure5=cure5,
                            bilan1 =bilan1,
                            bilan2 = bilan2,
                            bilan3 = bilan3,
                            bilan4 = bilan4,
                            bilan5 = bilan5,
                            bilan6 = bilan6,
                            bilan7 = bilan7,
                            bilan8 = bilan8,
                            bilan9 = bilan9,
                            bilan10 = bilan10,
                            defrenation1 = defrenation1,
                            defrenation2 = defrenation2,
                            defrenation3 = defrenation3,
                            defrenation4 = defrenation4,
                            defrenation5 = defrenation5,
                            examComp1 = examComp1,
                            examComp2 = examComp2,
                            examComp3 = examComp3,
                            examComp4 = examComp4,
                            examComp5 = examComp5,
                            examComp6 = examComp6,
                            examComp7 = examComp7,
                            examComp8 = examComp8,
                            examComp9 = examComp9,
                            examComp10 = examComp10,
                            resume = resume,
                            dateRdv = dateRDV,
                            medecin = medecin_actif,
                        )
                        
                        dossier.save()
                        return redirect('liste')
                    else :
                        messages.error(request, 'La date du prochain rendez-vous doit être pour le prochain mercredi.')
                        return render(request, 'messageDossier.html', context={'messages': messages.get_messages(request)})
                else :
                    messages.error(request, 'Date incorrecte.')
                    return render(request, 'messageDossier.html', context={'messages': messages.get_messages(request)})
    
    return render(request, "addDossier.html", {'ageDepart': ageDepart})


def liste(request):
    medecin = get_object_or_404(Medecin, is_active=True)
    dossiers = DossierMedical.objects.filter(medecin=medecin.id)
    
    if not dossiers :
        message = "Aucun dossier médical enregistré"
    else :
        message = ""
        
    context = {
        'dossiers' : dossiers,
        'message'  : message,
        'medecin'  : medecin.username,
    }
    
    if request.method == "POST" :
        if "delete" in request.POST :
            num = request.POST.get("delete")
            dossier = get_object_or_404(DossierMedical, numDossier=num)
            dossier.delete()
            return redirect('liste')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    return render(request, "liste.html", context)


def detail(request, id) :
    dossier = get_object_or_404(DossierMedical, id=id)

    return render(request, 'details.html', {'dossier':dossier})


def date_naissance(age):
    date_actuelle = datetime.now()
    
    annee_naissance = date_actuelle.year - age
    
    date_naissance = datetime(annee_naissance, date_actuelle.month, date_actuelle.day)

    return date_naissance


def update(request, id) :
    dossier = get_object_or_404(DossierMedical, id=id)
    naissance = date_naissance(dossier.age).year
    day = datetime.now()
    
    if request.method == "POST" :
        ident = request.POST.get('id')
        num = request.POST.get('num')
        identite = request.POST.get('identite')
        sexe = request.POST.get('sexe')
        dateNais = request.POST.get('nais')
        age = (int(day.year) - int(dateNais))
        adresse = request.POST.get('adresse')
        phone = request.POST.get('phone')
        diagnostic = request.POST.get('diagnostic')
        cure1 = request.POST.get('cure1')
        cure2 = request.POST.get('cure2')
        cure3 = request.POST.get('cure3')
        cure4 = request.POST.get('cure4')
        cure5 = request.POST.get('cure5')
        bilan1 = request.POST.get('bilan1')
        bilan2 = request.POST.get('bilan2')
        bilan3 = request.POST.get('bilan3')
        bilan4 = request.POST.get('bilan4')
        bilan5 = request.POST.get('bilan5')
        bilan6 = request.POST.get('bilan6')
        bilan7 = request.POST.get('bilan7')
        bilan8 = request.POST.get('bilan8')
        bilan9 = request.POST.get('bilan9')
        bilan10 = request.POST.get('bilan10')
        defrenation1 = request.POST.get('defrenation1')
        defrenation2 = request.POST.get('defrenation2')
        defrenation3 = request.POST.get('defrenation3')
        defrenation4 = request.POST.get('defrenation4')
        defrenation5 = request.POST.get('defrenation5')
        examComp1 = request.POST.get('examen1')
        examComp2 = request.POST.get('examen2')
        examComp3 = request.POST.get('examen3')
        examComp4 = request.POST.get('examen4')
        examComp5 = request.POST.get('examen5')
        examComp6 = request.POST.get('examen6')
        examComp7 = request.POST.get('examen7')
        examComp8 = request.POST.get('examen8')
        examComp9 = request.POST.get('examen9')
        examComp10 = request.POST.get('examen10')
        resume = request.POST.get('resume')
        dateRDV = request.POST.get('dateRDV')
        
        dossier = get_object_or_404(DossierMedical, id=ident)
        
        dossier.numDossier=num
        dossier.identite=identite
        dossier.sexe=sexe
        dossier.age=age
        dossier.adresse=adresse
        dossier.telephone=phone
        dossier.diagnostic=diagnostic
        dossier.cure1=cure1
        dossier.cure2=cure2
        dossier.cure3=cure3
        dossier.cure4=cure4
        dossier.cure5=cure5
        dossier.bilan1 =bilan1
        dossier.bilan2 = bilan2
        dossier.bilan3 = bilan3
        dossier.bilan4 = bilan4
        dossier.bilan5 = bilan5
        dossier.bilan6 = bilan6
        dossier.bilan7 = bilan7
        dossier.bilan8 = bilan8
        dossier.bilan9 = bilan9
        dossier.bilan10 = bilan10
        dossier.defrenation1 = defrenation1
        dossier.defrenation2 = defrenation2
        dossier.defrenation3 = defrenation3
        dossier.defrenation4 = defrenation4
        dossier.defrenation5 = defrenation5
        dossier.examComp1 = examComp1
        dossier.examComp2 = examComp2
        dossier.examComp3 = examComp3
        dossier.examComp4 = examComp4
        dossier.examComp5 = examComp5
        dossier.examComp6 = examComp6
        dossier.examComp7 = examComp7
        dossier.examComp8 = examComp8
        dossier.examComp9 = examComp9
        dossier.examComp10 = examComp10
        dossier.resume = resume
        dossier.dateRdv = dateRDV
        
        dossier.save()
        return redirect('liste')
    
    return render(request, 'updateDossier.html', {'dossier': dossier, 'naissance' : naissance})


def listeVisite(request) :
    date_actuelle = datetime.now()
    jour_semaine_actuel = date_actuelle.weekday()
    jours_jusquau_mercredi = (2 - jour_semaine_actuel + 7) % 7
    date_mercredi_suivant = date_actuelle + timedelta(days=jours_jusquau_mercredi)
    date = date_mercredi_suivant.date()
    
    medecin = get_object_or_404(Medecin, is_active=True)
    visites = DossierMedical.objects.filter(dateRdv__date=date, medecin=medecin.id)

    if not visites :
        message = "Aucune visite enregistrée"
    else :
        message = ""
        
    context = {
        'visites' : visites,
        'message' : message,
        'date'    : date,
    }
    
    return render(request, 'listeVisite.html', context)



def visitesJour(request):
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)
    visites = DossierMedical.objects.filter(dateRdv__date=date, medecin=medecin.id)
    
    if not visites :
        message = "Aucune visite pour aujourd'hui"
    else :
        message = ""
        
    context = {
        'visites' : visites,
        'message' : message,
        'date'    : date,
    }
    
    return render (request, 'visitesJour.html', context)



def search (request) :
    if request.method == "POST" :
        recherche = request.POST.get("search", "")
        patients = DossierMedical.objects.filter(
            models.Q(numDossier__icontains=recherche) | 
            models.Q(identite__icontains=recherche)
        )
        
        return render(request, 'resultat_search.html', {'patients': patients})

        
    return render(request, "includes/header.html")