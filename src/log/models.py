from django.db import models
from medecin.models import Medecin


# Create your models here.

class Log (models.Model) :
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name= "Date")
    libelle = models.CharField(max_length=255)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)

    
    def __str__(self):
         return f"{self.date} - {self.libelle}"