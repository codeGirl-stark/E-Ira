from datetime import datetime, timedelta
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from dossier.models import DossierMedical
from log.models import Log
from medecin.models import Medecin
import csv
from django.apps import apps
import shutil
import os
from django.conf import settings

# Create your views here.

"""def prochain_mercredi(date_rdv):
    input_date = datetime.strptime(date_rdv, '%Y-%m-%d')

    # Calculer les jours restants jusqu'au mercredi suivant
    jours_jusquau_mercredi = (2 - input_date.weekday() + 7) % 7

    # Ajouter la durée nécessaire pour atteindre le mercredi suivant
    prochain_mercredi = input_date + timedelta(days=jours_jusquau_mercredi)

    return input_date == prochain_mercredi"""



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
            antecedent = request.POST.get('antecedent')
            carcinome = request.POST.get('carcinome')
            ageDecouverte = request.POST.get('ageDecouverte')
            Nodule = request.POST.get('Nodule')
            DecouverteFortuite = request.POST.get('DecouverteFortuite')
            gnm = request.POST.get('gnm')
            adp = request.POST.get('adp')
            Metastase = request.POST.get('Metastase')
            AutresCir = request.POST.get('AutresCir')
            anteFamiliaux = request.POST.get('anteFamiliaux')
            typeHisto = request.POST.get('typeHisto')
            clasT = request.POST.get('clasT')
            clasN = request.POST.get('clasN')
            clasM = request.POST.get('clasM')
            multifoc = request.POST.get('multifoc')
            effraCapsulaire = request.POST.get('effraCapsulaire')
            embonVasculaire = request.POST.get('embonVasculaire')
            Aucune = request.POST.get('Aucune')
            Ganglionaire = request.POST.get('Ganglionaire')
            Pulmonaire = request.POST.get('Pulmonaire')
            Oseuse = request.POST.get('Oseuse')
            Hepatique = request.POST.get('Hepatique')
            Cerebrale = request.POST.get('Cerebrale')
            AutresMeta = request.POST.get('AutresMeta')
            stade = request.POST.get('stade')
            risque = request.POST.get('risque')
            temps1 = request.POST.get('temps1')
            temps2 = request.POST.get('temps2')
            curage = request.POST.get('curage')
            nbrCure = request.POST.get('nbrCure')
            activiteCumule = request.POST.get('activiteCumule')
            thera = request.POST.get('thera')
            cure1 = request.POST.get('cure1')
            cure2 = request.POST.get('cure2')
            cure3 = request.POST.get('cure3')
            cure4 = request.POST.get('cure4')
            cure5 = request.POST.get('cure5')
            cure6 = request.POST.get('cure6')
            cure7 = request.POST.get('cure7')
            cure8 = request.POST.get('cure8')
            cure9 = request.POST.get('cure9')
            cure10 = request.POST.get('cure10')
            defrenation1 = request.POST.get('defrenation1')
            defrenation2 = request.POST.get('defrenation2')
            defrenation3 = request.POST.get('defrenation3')
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
            consigne = request.POST.get('consigne')
            refrac = request.POST.get('refrac')
            dateRDV = request.POST.get('dateRDV')
            
            dossier = DossierMedical.objects.filter(numDossier=num).first()
            date_obj = datetime.strptime(dateRDV, '%Y-%m-%d')
            

            if dossier :
                return HttpResponse(f'Un dossier avec le {num} existe déjà')
            else :
                if day < date_obj :
                    
                    dossier = DossierMedical(
                        numDossier=num,
                        identite=identite,
                        sexe=sexe,
                        age=age,
                        adresse=adresse,
                        telephone=phone,
                        antecedent = antecedent,
                        carcinome = carcinome,
                        anteFamiliaux = anteFamiliaux,
                        ageDecouverte = ageDecouverte,
                        Nodule = Nodule,
                        DecouverteFortuite = DecouverteFortuite,
                        gnm = gnm,
                        adp = adp,
                        Metastase = Metastase,
                        AutresCir = AutresCir,
                        typeHisto = typeHisto,
                        clasT = clasT,
                        clasN = clasN,
                        clasM = clasM,
                        multifoc = multifoc,
                        effraCapsulaire= effraCapsulaire,
                        embonVasculaire = embonVasculaire,
                        Aucune = Aucune, 
                        Ganglionaire = Ganglionaire,
                        Pulmonaire = Pulmonaire,
                        Oseuse = Oseuse,
                        Hepatique = Hepatique,
                        Cerebrale = Cerebrale,
                        AutresMeta = AutresMeta,
                        stade = stade,
                        risque = risque,
                        temps1 = temps1,
                        temps2 = temps2,
                        curage = curage,
                        nbrCure = nbrCure, 
                        activiteCumule = activiteCumule,
                        thera =thera,
                        cure1 = cure1,
                        cure2 = cure2,
                        cure3 = cure3,
                        cure4 = cure4,
                        cure5 = cure5,
                        cure6 = cure6,
                        cure7 = cure7,
                        cure8 = cure8,
                        cure9 = cure9,
                        cure10 = cure10,
                        defrenation1 = defrenation1,
                        defrenation2 = defrenation2,
                        defrenation3 = defrenation3,
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
                        consigne = consigne,
                        refrac = refrac,
                        dateRdv = dateRDV,
                        medecin = medecin_actif,
                    )
                    dossier.save()
                    
                    log = Log(
                        date = day,
                        libelle = f"{medecin_actif.username} a enregistré le dossier du patient {identite}",
                        medecin = medecin_actif,
                    )
                    log.save()
                    
                    return redirect('liste')
                else :
                    return HttpResponse('Date incorrecte.')
    
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
            return render(request, "confirm.html", {'dossier': dossier})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    return render(request, "liste.html", context)


def delete(request,id) :
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)

    
    dossier = get_object_or_404(DossierMedical, id=id)
    dossier.delete()
    log = Log(
        date = date,
        libelle = f"{medecin.username} a supprimé le dossier du patient {dossier.identite}",
        medecin = medecin,
    )
    log.save()
    
    return redirect('liste')

    return render(request, "confirm.html")


def detail(request, id) :
    dossier = get_object_or_404(DossierMedical, id=id)

    return render(request, 'details.html', {'dossier':dossier})


def date_naissance(age):
    date_actuelle = datetime.now()
    
    annee_naissance = date_actuelle.year - age
    
    date_naissance = datetime(annee_naissance, date_actuelle.month, date_actuelle.day)

    return date_naissance


def update(request, id) :
    medecin = get_object_or_404(Medecin, is_active=True)
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
        antecedent = request.POST.get('antecedent')
        carcinome = request.POST.get('carcinome')
        ageDecouverte = request.POST.get('ageDecouverte')
        Nodule = request.POST.get('Nodule')
        DecouverteFortuite = request.POST.get('DecouverteFortuite')
        gnm = request.POST.get('gnm')
        adp = request.POST.get('adp')
        Metastase = request.POST.get('Metastase')
        AutresCir = request.POST.get('AutresCir')
        anteFamiliaux = request.POST.get('anteFamiliaux')
        typeHisto = request.POST.get('typeHisto')
        clasT = request.POST.get('clasT')
        clasN = request.POST.get('clasN')
        clasM = request.POST.get('clasM')
        multifoc = request.POST.get('multifoc')
        effraCapsulaire = request.POST.get('effraCapsulaire')
        embonVasculaire = request.POST.get('embonVasculaire')
        Aucune = request.POST.get('Aucune')
        Ganglionaire = request.POST.get('Ganglionaire')
        Pulmonaire = request.POST.get('Pulmonaire')
        Oseuse = request.POST.get('Oseuse')
        Hepatique = request.POST.get('Hepatique')
        Cerebrale = request.POST.get('Cerebrale')
        AutresMeta = request.POST.get('AutresMeta')
        stade = request.POST.get('stade')
        risque = request.POST.get('risque')
        temps1 = request.POST.get('temps1')
        temps2 = request.POST.get('temps2')
        curage = request.POST.get('curage')
        nbrCure = request.POST.get('nbrCure')
        activiteCumule = request.POST.get('activiteCumule')
        cure1 = request.POST.get('cure1')
        cure2 = request.POST.get('cure2')
        cure3 = request.POST.get('cure3')
        cure4 = request.POST.get('cure4')
        cure5 = request.POST.get('cure5')
        cure6 = request.POST.get('cure6')
        cure7 = request.POST.get('cure7')
        cure8 = request.POST.get('cure8')
        cure9 = request.POST.get('cure9')
        cure10 = request.POST.get('cure10')
        defrenation1 = request.POST.get('defrenation1')
        defrenation2 = request.POST.get('defrenation2')
        defrenation3 = request.POST.get('defrenation3')
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
        consigne = request.POST.get('consigne')
        dateRDV = request.POST.get('dateRDV')
        
        dossier = get_object_or_404(DossierMedical, id=ident)
        
        dossier.numDossier=num
        dossier.identite=identite
        dossier.sexe=sexe
        dossier.age=age
        dossier.adresse=adresse
        dossier.telephone=phone
        dossier.antecedent = antecedent
        dossier.carcinome = carcinome
        dossier.ageDecouverte = ageDecouverte
        dossier.Nodule = Nodule
        dossier.DecouverteFortuite = DecouverteFortuite
        dossier.gnm = gnm
        dossier.adp = adp
        dossier.Metastase = Metastase
        dossier.AutresCir = AutresCir
        dossier.typeHisto = typeHisto
        dossier.clasT = clasT
        dossier.clasN = clasN
        dossier.clasM = clasM
        dossier.Aucune = Aucune
        dossier.Ganglionaire = Ganglionaire
        dossier.Pulmonaire =Oseuse
        dossier.Hepatique = Hepatique
        dossier.Cerebrale = Cerebrale
        dossier.AutresMeta = AutresMeta
        dossier.risque = risque
        dossier.temps1 = temps1
        dossier.temps2 = temps2
        dossier.curage = curage
        dossier.nbrCure = nbrCure
        dossier.activiteCumule = activiteCumule
        dossier.cure1 = cure1
        dossier.cure2 = cure2
        dossier.cure3 = cure3
        dossier.cure4 = cure4
        dossier.cure5 = cure5
        dossier.cure6 = cure6
        dossier.cure7 = cure7
        dossier.cure8 = cure8
        dossier.cure9 = cure9
        dossier.cure10 = cure10
        dossier.defrenation1 = defrenation1
        dossier.defrenation2 = defrenation2
        dossier.defrenation3 = defrenation3
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
        dossier.consigne = consigne
        dossier.dateRdv = dateRDV
        
        dossier.save()
        
        log = Log(
            date = day,
            libelle = f"{medecin.username} a modifé le dossier du patient {identite}",
            medecin = medecin,
        )
        log.save()
    
        return redirect('liste')
    
    return render(request, 'updateDossier.html', {'dossier': dossier, 'naissance' : naissance})



def visitesJour(request):
    
    date = datetime.now().strftime('%Y-%m-%d')
    medecin = get_object_or_404(Medecin, is_active=True)
    visites = DossierMedical.objects.filter(dateRdv=date, medecin=medecin.id)
    
    if not visites :
        message = "Aucune consultation pour aujourd'hui"
    else :
        message = ""
        
    context = {
        'visites' : visites,
        'message' : message,
        'date'    : date,
    }
    
    return render (request, 'visitesJour.html', context)



def search (request) :
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)

    if request.method == "POST" :
        recherche = request.POST.get("search", "")
        patients = DossierMedical.objects.filter(
            models.Q(numDossier__icontains=recherche) | 
            models.Q(identite__icontains=recherche)
        )
        
        log = Log(
            date = date,
            libelle = f"{medecin.username} a éffectué une recherche sur {recherche}",
            medecin = medecin,
        )
        log.save()
        
        return render(request, 'resultat_search.html', {'patients': patients})

    return render(request, "includes/header.html")


def rechercheVisite (request) :
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)

    if request.method == "POST" :
        date_recherchee = request.POST.get("search")
        
        if date_recherchee:
            visites = DossierMedical.objects.filter(dateRdv=date_recherchee, medecin=medecin.id)
            if not visites :
                message = f"Aucune consultation pour le {date_recherchee}"
            else :
                message = ""
                
            context = {
                'visites' : visites,
                'message' : message,
                'date'    : date_recherchee,
            }
            
            log = Log(
            date = date,
            libelle = f"{medecin.username} a recherché les visites du {date_recherchee}",
            medecin = medecin,
            )
            log.save()
            
            return render(request, "listeVisite.html", context)
        

    return render (request, "listeVisite.html")


def export (request) :
    
    return render(request, "export.html")

def export_to_csv (request) :
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)

    csv_filename = "base.csv"

    # Liste de tous les modèles dans l'application
    all_models = apps.get_models()

    # Ouverture du fichier en mode écriture
    with open(csv_filename, 'w', newline='') as csv_file:
        # Création de l'objet writer
        csv_writer = csv.writer(csv_file)

        for model in all_models:
            # Obtention de toutes les instances du modèle
            all_data = model.objects.all()

            # Écriture de l'en-tête du CSV (noms de colonnes)
            header = [field.name for field in model._meta.fields]
            csv_writer.writerow([f"{model.__name__} - {col}" for col in header])

            # Écriture des données dans le CSV
            for row in all_data:
                csv_writer.writerow([getattr(row, field) for field in header])

    # Réponse HTTP pour télécharger le fichier CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="base.csv"'
    
    log = Log(
        date = date,
        libelle = f"{medecin.username} a téléchargé la base de données sous format CSV",
        medecin = medecin,
        )
    log.save()

    # Copie du contenu du fichier CSV dans la réponse HTTP
    with open(csv_filename, 'r') as csv_file:
        response.write(csv_file.read())

    return response
    
    
def export_to_sqlite(request):
    date = datetime.now()
    medecin = get_object_or_404(Medecin, is_active=True)
    
    # Chemin du fichier SQLite actuel
    db_path = settings.DATABASES['default']['NAME']

    # Chemin de destination pour le fichier exporté
    exported_db_path = os.path.join(settings.BASE_DIR, 'base.sqlite3')

    # Copie du fichier SQLite vers l'emplacement de destination
    shutil.copy2(db_path, exported_db_path)

    # Réponse HTTP pour télécharger le fichier SQLite
    response = HttpResponse(content_type='application/x-sqlite3')
    response['Content-Disposition'] = 'attachment; filename="base.sqlite3"'
    
    log = Log(
        date = date,
        libelle = f"{medecin.username} a téléchargé la base de données sous format Sqlite",
        medecin = medecin,
        )
    log.save()

    # Copie du contenu du fichier SQLite dans la réponse HTTP
    with open(exported_db_path, 'rb') as db_file:
        response.write(db_file.read())

    # Suppression du fichier exporté 
    os.remove(exported_db_path)

    return response