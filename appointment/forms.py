from django import forms
from patient.models import Patient

class RdvForm(forms.Form):
    date = forms.DateField(label="Date")
    heure = forms.TimeField(label='Heure')
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    objet = forms.CharField(label="Objet",max_length=255 ,min_length=1, required=False)

class SearchForm(forms.Form):
    date = forms.DateField(label="Date",required=False)
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(),required=False)