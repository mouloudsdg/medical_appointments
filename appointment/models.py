from django.db import models
from patient.models import Patient
# Create your models here.
class Rdv(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    objet = models.CharField(max_length=255, blank=True)
    class Meta:
        ordering = ["-date","heure"]
