from django.contrib import admin
from .models import DossierMedical, Medecin

class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'numDossier', 'identite', 'sexe', 'age', 'adresse', 'telephone',
        'antecedent', 'carcinome', 'anteFamiliaux', 'ageDecouverte', 'Nodule', 'DecouverteFortuite', 
        'gnm','adp','Metastase','AutresCir', 'typeHisto','clasT', 'clasN', 'clasM', 
        'multifoc', 'effraCapsulaire', 'embonVasculaire','Aucune','Ganglionaire','Pulmonaire','Oseuse',
        'Hepatique','Cerebrale','AutresMeta','stade', 'risque', 'temps1','temps2','curage', 'nbrCure', 'activiteCumule',
        'thera', 'cure1', 'cure2', 'cure3', 'cure4', 'cure5', 'cure6', 'cure7',
        'cure8', 'cure9', 'cure10', 'defrenation1', 'defrenation2', 'defrenation3',
        'bilan1', 'bilan2', 'bilan3', 'bilan4', 'bilan5', 'bilan6', 'bilan7', 'bilan8',
        'bilan9', 'bilan10', 'examComp1', 'examComp2', 'examComp3', 'examComp4', 'examComp5',
        'examComp6', 'examComp7', 'examComp8', 'examComp9', 'examComp10', 'resume', 'consigne',
        'refrac', 'dateRdv', 'medecin'
    )
    
    search_fields = ('numDossier', 'identite', 'medecin__nom')  # Adjust based on your Medecin model
    list_filter = ('numDossier', 'medecin')

    fieldsets = (
        ('Informations Générales', {
            'fields': ('numDossier', 'identite', 'sexe', 'age', 'adresse', 'telephone')
        }),
        ('Antécédents et Diagnostics', {
            'fields': ('antecedent', 'carcinome', 'anteFamiliaux', 'ageDecouverte',
                       'Nodule','DecouverteFortuite','gnm','adp','Metastase','AutresCir', 'typeHisto')
        }),
        ('Classification et Stade', {
            'fields': ('clasT', 'clasN', 'clasM', 'multifoc', 'effraCapsulaire', 'embonVasculaire',
                       'Aucune','Ganglionaire','Pulmonaire','Oseuse','Hepatique','Cerebrale','AutresMeta',
                       'stade', 'risque', 'temps1','temps2','curage')
        }),
        ('Traitements', {
            'fields': (
                'nbrCure', 'activiteCumule', 'thera',
                'cure1', 'cure2', 'cure3', 'cure4', 'cure5',
                'cure6', 'cure7', 'cure8', 'cure9', 'cure10',
                'defrenation1', 'defrenation2', 'defrenation3',
                'bilan1', 'bilan2', 'bilan3', 'bilan4', 'bilan5',
                'bilan6', 'bilan7', 'bilan8', 'bilan9', 'bilan10',
                'examComp1', 'examComp2', 'examComp3', 'examComp4', 'examComp5',
                'examComp6', 'examComp7', 'examComp8', 'examComp9', 'examComp10'
            )
        }),
        ('Résumé et Consignes', {
            'fields': ('resume', 'consigne', 'refrac')
        }),
        ('Date et Médecin', {
            'fields': ('dateRdv', 'medecin')
        }),
    )

admin.site.register(DossierMedical, DossierMedicalAdmin)
