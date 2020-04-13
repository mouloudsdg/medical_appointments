from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.http import require_GET,require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from .forms import PatientForm
from django.http import Http404

# Create your views here.

@require_GET
def list(request):
    patients = Patient.objects.all()
    return HttpResponse(patients)


@require_GET
def detail(request,id):
    try:
        patient = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return HttpResponse(patient)

@require_GET
def delt(request,id):
    try:
        Patient.objects.get(pk=id).delete()
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return HttpResponse(status=205)

@csrf_exempt
@require_http_methods(["GET","POST"])
def add(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            adresse = form.cleaned_data["adresse"]
            telephone = form.cleaned_data["telephone"]
            mail = form.cleaned_data["mail"]
            p = Patient(nom=nom,prenom=prenom,adresse=adresse,telephone=telephone,mail=mail)
            p.save()
            return HttpResponseRedirect("/patient/")
    else:
        form = PatientForm()
    
    return HttpResponse(form)