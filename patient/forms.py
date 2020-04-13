from django import forms

class PatientForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100)
    prenom = forms.CharField(label='Prenom', max_length=100)
    adresse = forms.CharField(label="Adresse",max_length=100, required=False)
    telephone = forms.CharField(label="Telephone", max_length=100)
    mail = forms.EmailField(label='E-mail', max_length=100,required=False)
    