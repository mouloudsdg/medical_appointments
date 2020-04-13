from django.db import models

# Create your models here.
class Rdv(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.ForeignKey("patient.Patient",on_delete=models.CASCADE)

    
    class Meta:
        ordering = ["-date","heure"]
