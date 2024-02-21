from datetime import datetime
import os
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from dossier.models import DossierMedical
from log.models import Log

from medecin.models import Medecin

# Create your views here.

def connect(request) :
    date = datetime.now()   
    if request.method == "POST" :
        medecin_en_ligne = Medecin.objects.filter(is_active=True).first()
        if medecin_en_ligne :
            medecin_en_ligne.is_active = False
            medecin_en_ligne.save()
        username = request.POST.get('username')
        password = request.POST.get('password')
        medecin = get_object_or_404(Medecin, username=username)
            
        if medecin.password == password :
            medecin.is_active = True
            medecin.save()
            log = Log(
                date = date,
                libelle = f"{username} s'est connectée",
                medecin = medecin,
            )
            log.save()
            return redirect('liste')
        else :
            return HttpResponse ("Mot de passe incorrect")

    return render(request, "connexion.html")


def stat (request) :
    
    age_ado = (0, 39)
    age_perso = (40,59)
    age_adultes = (60, 150)
    
    age1 = (0, 24)
    age2 = (25, 39)
    age3 = (40, 49)
    age4 = (50, 59)
    age5 = (60, 69)
    age6 = (70, 300)
    
    cure1 = (0, 4)
    cure2 = (5, 10)
    cure3 = (11, 100)
    
    cumul1 = (0, 199)
    cumul2 = (200, 299)
    cumul3 = (300, 499)
    cumul4 = (500, 1000)
    cumul5 = (1001, 5000)
    
    
    medecin = get_object_or_404(Medecin, is_active=True)
    patients = DossierMedical.objects.filter(medecin=medecin.id).count()
    
    homme = DossierMedical.objects.filter(medecin=medecin.id, sexe="M").count()
    stathomme = int((homme / patients) * 100)
    femme = DossierMedical.objects.filter(medecin=medecin.id, sexe="F").count()
    statfemme = int((femme / patients) * 100)
    
    ado = DossierMedical.objects.filter(age__range=age_ado).count()
    statAdo = int((ado / patients) * 100)
    perso = DossierMedical.objects.filter(age__range=age_perso).count()
    statPerso = int((perso / patients) * 100)
    adulte = DossierMedical.objects.filter(age__range=age_adultes).count()
    statAdulte = int((adulte / patients) * 100)
    
    #compte par age de découverte
    agedec1 = DossierMedical.objects.filter(ageDecouverte__range=age1).count()
    statAgedec1 = int((agedec1 / patients) * 100)
    agedec2 = DossierMedical.objects.filter(ageDecouverte__range=age2).count()
    statAgedec2 = int((agedec2 / patients) * 100)
    agedec3 = DossierMedical.objects.filter(ageDecouverte__range=age3).count()
    statAgedec3 = int((agedec3 / patients) * 100)
    agedec4 = DossierMedical.objects.filter(ageDecouverte__range=age4).count()
    statAgedec4 = int((agedec4 / patients) * 100)
    agedec5 = DossierMedical.objects.filter(ageDecouverte__range=age5).count()
    statAgedec5 = int((agedec5 / patients) * 100)
    agedec6 = DossierMedical.objects.filter(ageDecouverte__range=age6).count()
    statAgedec6 = int((agedec6 / patients) * 100)
    
    #compte par circonstances
    circonstances1 = DossierMedical.objects.filter(medecin=medecin.id, Nodule="on").count()
    statci1 = int((circonstances1 / patients) * 100)
    circonstances2 = DossierMedical.objects.filter(medecin=medecin.id, DecouverteFortuite="on").count()
    statci2 = int((circonstances2 / patients) * 100)
    circonstances3 = DossierMedical.objects.filter(medecin=medecin.id, gnm="on").count()
    statci3 = int((circonstances3 / patients) * 100)
    circonstances4 = DossierMedical.objects.filter(medecin=medecin.id, adp="on").count()
    statci4 = int((circonstances4 / patients) * 100)
    circonstances5 = DossierMedical.objects.filter(medecin=medecin.id, Metastase="on").count()
    statci5 = int((circonstances5 / patients) * 100)
    circonstances6 = DossierMedical.objects.filter(medecin=medecin.id, AutresCir="on").count()
    statci6 = int((circonstances6 / patients) * 100)
    
    #compte par type hostoligique 
    type1 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Papillaire").count()
    statType1 = int((type1 / patients) * 100)
    type2 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Vesiculaire").count()
    statType2 = int((type2 / patients) * 100)
    type3 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="PapilloVesiculaire").count()
    statType3 = int((type3 / patients) * 100)
    type4 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Medullaire").count()
    statType4 = int((type4 / patients) * 100)
    type5 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Anaplasique").count()
    statType5 = int((type5 / patients) * 100)
    type6 = DossierMedical.objects.filter(medecin=medecin.id, typeHisto="Autres").count()
    statType6 = int((type6 / patients) * 100)
    
    #compte par classifications T
    clasTx = DossierMedical.objects.filter(medecin=medecin.id, clasT="Tx").count()
    statTx = int((clasTx / patients) * 100)
    clasT0 = DossierMedical.objects.filter(medecin=medecin.id, clasT="T0").count()
    statT0 = int((clasT0 / patients) * 100)
    clasT1a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T1a").count()
    statT1a = int((clasT1a / patients) * 100)
    clasT1b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T1b").count()
    statT1b = int((clasT1b / patients) * 100)
    clasT2 = DossierMedical.objects.filter(medecin=medecin.id, clasT="T2").count()
    statT2 = int((clasT2 / patients) * 100)
    clasT3a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T3a").count()
    statT3a = int((clasT3a / patients) * 100)
    clasT3b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T3b").count()
    statT3b = int((clasT3b / patients) * 100)
    clasT4a = DossierMedical.objects.filter(medecin=medecin.id, clasT="T4a").count()
    statT4a = int((clasT3a / patients) * 100)
    clasT4b = DossierMedical.objects.filter(medecin=medecin.id, clasT="T4b").count()
    statT4b = int((clasT4b / patients) * 100)

    #compte par classifications N
    clasNx = DossierMedical.objects.filter(medecin=medecin.id, clasN="Nx").count()
    statNx = int((clasNx / patients) * 100)
    clasN0 = DossierMedical.objects.filter(medecin=medecin.id, clasN="N0").count()
    statN0 = int((clasN0 / patients) * 100)
    clasN1a = DossierMedical.objects.filter(medecin=medecin.id, clasN="N1a").count()
    statN1a = int((clasN1a / patients) * 100)
    clasN1b = DossierMedical.objects.filter(medecin=medecin.id, clasN="N1b").count()
    statN1b = int((clasN1b / patients) * 100)
    
    #compte par classifications M
    clasMx = DossierMedical.objects.filter(medecin=medecin.id, clasM="Mx").count()
    statMx = int((clasMx / patients) * 100)
    clasM0 = DossierMedical.objects.filter(medecin=medecin.id, clasM="M0").count()
    statM0 = int((clasM0 / patients) * 100)
    clasM1 = DossierMedical.objects.filter(medecin=medecin.id, clasM="M1").count()
    statM1 = int((clasM1 / patients) * 100)

    #compte par métastase
    meta1 = DossierMedical.objects.filter(medecin=medecin.id, Aucune="on").count()
    statmeta1 = int((meta1 / patients) * 100)
    meta2 = DossierMedical.objects.filter(medecin=medecin.id, Ganglionaire="on").count()
    statmeta2 = int((meta2 / patients) * 100)
    meta3 = DossierMedical.objects.filter(medecin=medecin.id, Pulmonaire="on").count()
    statmeta3 = int((meta3 / patients) * 100)
    meta4 = DossierMedical.objects.filter(medecin=medecin.id, Oseuse="on").count()
    statmeta4 = int((meta4 / patients) * 100)
    meta5 = DossierMedical.objects.filter(medecin=medecin.id, Hepatique="on").count()
    statmeta5 = int((meta5 / patients) * 100)
    meta6 = DossierMedical.objects.filter(medecin=medecin.id, Cerebrale="on").count()
    statmeta6 = int((meta6 / patients) * 100)
    meta7 = DossierMedical.objects.filter(medecin=medecin.id, AutresMeta="on").count()
    statmeta7 = int((meta7 / patients) * 100)
    
    #compte par stade
    stade1 = DossierMedical.objects.filter(medecin=medecin.id, stade="I").count()
    statStade1 = int((stade1 / patients) * 100)
    stade2 = DossierMedical.objects.filter(medecin=medecin.id, stade="II").count()
    statStade2 = int((stade2 / patients) * 100)
    stade3 = DossierMedical.objects.filter(medecin=medecin.id, stade="III").count()
    statStade3 = int((stade3 / patients) * 100)
    stade4 = DossierMedical.objects.filter(medecin=medecin.id, stade="IVA").count()
    statStade4 = int((stade4 / patients) * 100)
    stade5 = DossierMedical.objects.filter(medecin=medecin.id, stade="IVB").count()
    statStade5 = int((stade5 / patients) * 100)
    
    #compte par risque
    risque1 = DossierMedical.objects.filter(medecin=medecin.id, risque="Faible").count()
    statRisque1 = int((risque1 / patients) * 100)
    risque2 = DossierMedical.objects.filter(medecin=medecin.id, risque="Intermediare").count()
    statRisque2 = int((risque2 / patients) * 100)
    risque3 = DossierMedical.objects.filter(medecin=medecin.id, risque="Haut").count()
    statRisque3 = int((risque3 / patients) * 100)

    #compte par totalisation chirugicale
    totalChir1 = DossierMedical.objects.filter(medecin=medecin.id, temps1="on").count()
    statChir1 = int((totalChir1 / patients) * 100)
    totalChir2 = DossierMedical.objects.filter(medecin=medecin.id, temps2="on").count()
    statChir2 = int((totalChir2 / patients) * 100)
    totalChir3 = DossierMedical.objects.filter(medecin=medecin.id, curage="on").count()
    statChir3 = int((totalChir3 / patients) * 100)


    #compte par nombre de curage
    nbrCur1 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure__range=cure1).count()
    statCur1 = int((nbrCur1 / patients) * 100)
    nbrCur2 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure__range=cure2).count()
    statCur2 = int((nbrCur2 / patients) * 100)
    nbrCur3 = DossierMedical.objects.filter(medecin=medecin.id, nbrCure__range=cure3).count()
    statCur3 = int((nbrCur3 / patients) * 100)
    
    
    #compte par activités cumulés
    activite1 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule__range=cumul1).count()
    statActivite1 = int((activite1 / patients) * 100)
    activite2 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule__range=cumul2).count()
    statActivite2 = int((activite2 / patients) * 100)
    activite3 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule__range=cumul3).count()
    statActivite3 = int((activite3 / patients) * 100)
    activite4 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule__range=cumul4).count()
    statActivite4 = int((activite4 / patients) * 100)
    activite5 = DossierMedical.objects.filter(medecin=medecin.id, activiteCumule__range=cumul5).count()
    statActivite5 = int((activite5 / patients) * 100)
    
    
    carcinome = DossierMedical.objects.filter(medecin=medecin.id, carcinome="oui").count()
    statCarcinome = int((carcinome / patients) * 100)
    
    effra = DossierMedical.objects.filter(medecin=medecin.id, effraCapsulaire="oui").count()
    statEffra = int((effra / patients) * 100)
    
    embon = DossierMedical.objects.filter(medecin=medecin.id, embonVasculaire="oui").count()
    statEmbon = int((embon / patients) * 100)
    
    refrac = DossierMedical.objects.filter(medecin=medecin.id, refrac="oui").count()
    statRefrac = int((refrac / patients) * 100)


    if not patients :
        message = "Vous n'avez aucun patient pour le moment"
    else :
        message = ""
        
    context = {
        "message" : message,
        "patients" : patients,
        
        "carcinome" : carcinome,
        "statCarcinome" : statCarcinome,
        "effra" : effra,
        "statEffra" : statEffra,
        "embon" : embon,
        "statEmbon" : statEmbon,
        "refrac" : refrac,
        "statRefrac" : statRefrac,
        
        "homme" : homme,
        "stathomme" : stathomme,
        "femme" : femme,
        "statfemme" : statfemme,
        
        "ado": ado,
        "statAdo" : statAdo,
        "perso" : perso,
        "statPerso" : statPerso,
        "adulte": adulte,
        "statAdulte" : statAdulte,
        
        "agedec1" : agedec1,
        "statAgedec1" : statAgedec1,
        "agedec2" : agedec2,
        "statAgedec2" : statAgedec2,
        "agedec3" : agedec3,
        "statAgedec3" : statAgedec3,
        "agedec4" : agedec4,
        "statAgedec4" : statAgedec4,
        "agedec5" : agedec5,
        "statAgedec5" : statAgedec5,
        "agedec6" : agedec6,
        "statAgedec6" : statAgedec6,
        
        "circonstance1" : circonstances1,
        "statci1" : statci1,
        "circonstance2" : circonstances2,
        "statci2" : statci2,
        "circonstance3" : circonstances3,
        "statci3" : statci3,
        "circonstance4" : circonstances4,
        "statci4" : statci4,
        "circonstance5" : circonstances5,
        "statci5" : statci5,
        "circonstance6" : circonstances6,
        "statci6" : statci6,
        
        "type1" : type1,
        "statType1" : statType1,
        "type2" : type2,
        "statType2" : statType2,
        "type3" : type3,
        "statType3" : statType3,
        "type4" : type4,
        "statType4" : statType4,
        "type5" : type5,
        "statType5" : statType5,
        "type6" : type6,
        "statType6" : statType6,
        
        "clasTx" : clasTx,
        "statTx" : statTx,
        "clasT0" : clasT0,
        "statT0" : statT0,
        "clasT1a" : clasT1a,
        "statT1a" : statT1a,
        "clasT1b" : clasT1b,
        "statT1b" : statT1b,
        "clasT2" : clasT2,
        "statT2" : statT2,
        "clasT3a" : clasT3a,
        "statT3a" : statT3a,
        "clasT3b" : clasT3b,
        "statT3b" : statT3b,
        "clasT4a" : clasT4a,
        "statT4a" : statT4a,
        "clasT4b" : clasT4b,
        "statT4b" : statT4b,
        
        "clasNx" : clasNx,
        "statNx" : statNx,
        "clasN0" : clasN0,
        "statN0" : statN0,
        "clasN1a" : clasN1a,
        "statN1a" : statN1a,
        "clasN1b" : clasN1b,
        "statN1b" : statN1b,
        
        "clasMx" : clasMx,
        "statMx" : statMx,
        "clasM0" : clasM0,
        "statM0" : statM0,
        "clasM1" : clasM1,
        "statM1" : statM1,
        
        "meta1" : meta1,
        "statmeta1" : statmeta1,
        "meta2" : meta2,
        "statmeta2" : statmeta2,
        "meta3" : meta3,
        "statmeta3" : statmeta3,
        "meta4" : meta4,
        "statmeta4" : statmeta4,
        "meta5" : meta5,
        "statmeta5" : statmeta5,
        "meta6" : meta6,
        "statmeta6" : statmeta6,
        "meta7" : meta7,
        "statmeta7" : statmeta7,
        
        "stade1" : stade1,
        "statStade1" : statStade1,
        "stade2" : stade2,
        "statStade2" : statStade2,
        "stade3" : stade3,
        "statStade3" : statStade3,
        "stade4" : stade4,
        "statStade4" : statStade4,
        "stade5" : stade5,
        "statStade5" : statStade5,
        
        "risque1" : risque1,
        "statRisque1" : statRisque1,
        "risque2" : risque2,
        "statRisque2" : statRisque2,
        "risque3" : risque3,
        "statRisque3" : statRisque3,
        
        "totalChir1" : totalChir1,
        "statChir1" : statChir1,
        "totalChir2" : totalChir2,
        "statChir2" : statChir2,
        "totalChir3" : totalChir3,
        "statChir3" : statChir3,
        
        "nbrCur1" : nbrCur1,
        "statCur1" : statCur1,
        "nbrCur2" : nbrCur2,
        "statCur2" : statCur2,
        "nbrCur3" : nbrCur3,
        "statCur3" : statCur3,
        
        "activite1" : activite1,
        "activite2" : activite2,
        "activite3" : activite3,
        "activite4" : activite4,
        "activite5" : activite5,
    }

    return render(request, 'stat.html', context)



def deconnect(request) :
    date = datetime.now()
    
    medecin_actif = get_object_or_404(Medecin, is_active=True)
    medecin_actif.is_active = False
    medecin_actif.save()
    
    log = Log(
        date = date,
        libelle = "Déconnexion",
        medecin = medecin_actif,
    )
    log.save()
    
    return redirect('connect')