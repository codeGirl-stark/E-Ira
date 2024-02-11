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
    
    age_ado = (0, 59)
    age_adultes = (60, 150)
    age1 = (0, 40)
    age2 = (40, 50)
    age3 = (50, 60)
    age4 = (60, 70)
    age5 = (70, 300)
    
    
    medecin = get_object_or_404(Medecin, is_active=True)
    patients = DossierMedical.objects.filter(medecin=medecin.id).count()
    homme = DossierMedical.objects.filter(medecin=medecin.id, sexe="M").count()
    femme = DossierMedical.objects.filter(medecin=medecin.id, sexe="F").count()
    ado = DossierMedical.objects.filter(age__range=age_ado).count()
    adulte = DossierMedical.objects.filter(age__range=age_adultes).count()
    
    #compte par age de découverte
    agedec1 = DossierMedical.objects.filter(ageDecouverte__range=age1).count()
    agedec2 = DossierMedical.objects.filter(ageDecouverte__range=age2).count()
    agedec3 = DossierMedical.objects.filter(ageDecouverte__range=age3).count()
    agedec4 = DossierMedical.objects.filter(ageDecouverte__range=age4).count()
    agedec5 = DossierMedical.objects.filter(ageDecouverte__range=age5).count()
    
    #compte par circonstances
    circonstances1 = DossierMedical.objects.filter(medecin=medecin.id, circonstance="Module").count()
    circonstances2 = DossierMedical.objects.filter(medecin=medecin.id, circonstance="GMN").count()
    circonstances3 = DossierMedical.objects.filter(medecin=medecin.id, circonstance="ADP").count()
    circonstances4 = DossierMedical.objects.filter(medecin=medecin.id, circonstance="Metastase").count()
    circonstances5 = DossierMedical.objects.filter(medecin=medecin.id, circonstance="Autres").count()
    
    #compte par type hostoligique 
    type1 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Micro").count()
    type2 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Papillaire").count()
    type3 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Vesiculaire").count()
    type4 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="PapilloVesiculaire").count()
    type5 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Medullaire").count()
    type6 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Anaplasique").count()
    type7 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Autres").count()
    
    #compte par classifications T
    clasTx = DossierMedical.objects.filter(medecin=medecin.id, clasT="Tx").count()
    clasT0 = DossierMedical.objects.filter(medecin=medecin.id, clasT="T0").count()
    clasT1a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T1a").count()
    clasT1b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T1b").count()
    clasT2 = DossierMedical.objects.filter(medecin=medecin.id, clasT="T2").count()
    clasT3a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T3a").count()
    clasT3b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T3b").count()
    clasT4a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T4a").count()
    clasT4b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T4b").count()

    #compte par classifications N
    clasNx = DossierMedical.objects.filter(medecin=medecin.id, clasN="Nx").count()
    clasN0 = DossierMedical.objects.filter(medecin=medecin.id, clasN="N0").count()
    clasN1a = DossierMedical.objects.filter(medecin=medecin.id, clasN="N1a").count()
    clasN1b = DossierMedical.objects.filter(medecin=medecin.id, clasN="N1b").count()
    
    #compte par classifications M
    clasMx = DossierMedical.objects.filter(medecin=medecin.id, clasM="x").count()
    clasM0 = DossierMedical.objects.filter(medecin=medecin.id, clasM="M0").count()
    clasM1 = DossierMedical.objects.filter(medecin=medecin.id, clasM="M1").count()

    #compte par métastase
    meta1 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Aucune").count()
    meta2 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Ganglionaire").count()
    meta3 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Pulmonaire").count()
    meta4 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Oseuse").count()
    meta5 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Hepatique").count()
    meta6 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Cerebrale").count()
    meta7 = DossierMedical.objects.filter(medecin=medecin.id, metastase="Autres").count()
    
    #compte par stade
    stade1 = DossierMedical.objects.filter(medecin=medecin.id, stade="I").count()
    stade2 = DossierMedical.objects.filter(medecin=medecin.id, stade="II").count()
    stade3 = DossierMedical.objects.filter(medecin=medecin.id, stade="III").count()
    stade4 = DossierMedical.objects.filter(medecin=medecin.id, stade="IVA").count()
    stade5 = DossierMedical.objects.filter(medecin=medecin.id, stade="IVB").count()
    
    #compte par risque
    risque1 = DossierMedical.objects.filter(medecin=medecin.id, risque="Faible").count()
    risque2 = DossierMedical.objects.filter(medecin=medecin.id, risque="Intermediare").count()
    risque3 = DossierMedical.objects.filter(medecin=medecin.id, risque="Haut").count()

    #compte par totalisation chirugicale
    totalChir1 = DossierMedical.objects.filter(medecin=medecin.id, totalChir="1 temps").count()
    totalChir2 = DossierMedical.objects.filter(medecin=medecin.id, totalChir="2 temps").count()
    totalChir3 = DossierMedical.objects.filter(medecin=medecin.id, totalChir="curage").count()


    #compte par nombre de curage
    nbrCur1 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure="1-5").count()
    nbrCur2 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure="5-10").count()
    nbrCur3 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure=">10").count()
    
    #compte par activités cumulés
    activite1 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule="50-200").count()
    activite2 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule="200-300").count()
    activite3 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule="300-400").count()
    activite4 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule=">= 500").count()

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
        "agedec1" : agedec1,
        "agedec2" : agedec2,
        "agedec3" : agedec3,
        "agedec4" : agedec4,
        "agedec5" : agedec5,
        "circonstance1" : circonstances1,
        "circonstance2" : circonstances2,
        "circonstance3" : circonstances3,
        "circonstance4" : circonstances4,
        "circonstance5" : circonstances5,
        "type1" : type1,
        "type2" : type2,
        "type3" : type3,
        "type4" : type4,
        "type5" : type5,
        "type6" : type6,
        "type7" : type7,
        "clasTx" : clasTx,
        "clasT0" : clasT0,
        "clasT1a" : clasT1a,
        "clasT1b" : clasT1b,
        "clasT2" : clasT2,
        "clasT3a" : clasT3a,
        "clasT3b" : clasT3b,
        "clasT4a" : clasT4a,
        "clasT4b" : clasT4b,
        "clasNx" : clasNx,
        "clasN0" : clasN0,
        "clasN1a" : clasN1a,
        "clasN1b" : clasN1b,
        "clasMx" : clasMx,
        "clasM0" : clasM0,
        "clasM1" : clasM1,
        "meta1" : meta1,
        "meta2" : meta2,
        "meta3" : meta3,
        "meta4" : meta4,
        "meta5" : meta5,
        "meta6" : meta6,
        "meta7" : meta7,
        "stade1" : stade1,
        "stade2" : stade2,
        "stade3" : stade3,
        "stade4" : stade4,
        "stade5" : stade5,
        "risque1" : risque1,
        "risque2" : risque2,
        "risque3" : risque3,
        "totalChir1" : totalChir1,
        "totalChir2" : totalChir2,
        "totalChir3" : totalChir3,
        "nbrCur1" : nbrCur1,
        "nbrCur2" : nbrCur2,
        "nbrCur3" : nbrCur3,
        "activite1" : activite1,
        "activite2" : activite2,
        "activite2" : activite3,
        "activite3" : activite4,
    }

    return render(request, 'stat.html', context)


def deconnect(request) :
    medecin_actif = get_object_or_404(Medecin, is_active=True)
    medecin_actif.is_active = False
    medecin_actif.save()
    return redirect('connect')