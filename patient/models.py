from django.db import models


# Create your models here.

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255,blank=True)
    telephone = models.CharField(max_length=255)
    mail = models.EmailField(blank=True)
    info = models.TextField(blank=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return "%s %s" % (self.nom,self.prenom)
