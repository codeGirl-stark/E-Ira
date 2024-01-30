from django.db import models

# Create your models here.
class Medecin (models.Model) :
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

def __str__(self):
    return self.username
