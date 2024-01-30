from django.db import models

from medecin.models import Medecin

# Create your models here.

class DossierMedical(models.Model) :
    id = models.AutoField(primary_key=True)
    numDossier = models.CharField(max_length=20)
    identite = models.CharField(max_length=255)
    sexe = models.CharField(max_length=2)
    age = models.IntegerField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    diagnostic = models.TextField()
    cure1 = models.TextField(null=True)
    cure2 = models.TextField(null=True)
    cure3 = models.TextField(null=True)
    cure4 = models.TextField(null=True)
    cure5 = models.TextField(null=True)
    bilan1 = models.TextField(null=True)
    bilan2 = models.TextField(null=True)
    bilan3 = models.TextField(null=True)
    bilan4 = models.TextField(null=True)
    bilan5 = models.TextField(null=True)
    bilan6 = models.TextField(null=True)
    bilan7 = models.TextField(null=True)
    bilan8 = models.TextField(null=True)
    bilan9 = models.TextField(null=True)
    bilan10 = models.TextField(null=True)
    defrenation1 = models.TextField(null=True)
    defrenation2 = models.TextField(null=True)
    defrenation3 = models.TextField(null=True)
    defrenation4 = models.TextField(null=True)
    defrenation5 = models.TextField( null=True)
    examComp1 = models.TextField(null=True)
    examComp2 = models.TextField(null=True)
    examComp3 = models.TextField(null=True)
    examComp4 = models.TextField(null=True)
    examComp5 = models.TextField(null=True)
    examComp6 = models.TextField(null=True)
    examComp7 = models.TextField(null=True)
    examComp8 = models.TextField(null=True)
    examComp9 = models.TextField(null=True)
    examComp10 = models.TextField(null=True)
    resume = models.TextField(null=True)
    dateRdv = models.DateTimeField(verbose_name="Date du bilan")
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.numDossier
