from django import forms

class PatientForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100, min_length=2)
    prenom = forms.CharField(label='Prenom', max_length=100, min_length=2)
    adresse = forms.CharField(label="Adresse",max_length=100, min_length=5, required=False)
    telephone = forms.CharField(label="Telephone", max_length=100, min_length=5)
    mail = forms.EmailField(label='E-mail', max_length=100, min_length=5, required=False)
    info = forms.CharField(widget=forms.Textarea,required=False)