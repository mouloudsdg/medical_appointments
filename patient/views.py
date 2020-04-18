from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, QueryDict
from django.views.decorators.http import require_GET,require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from .forms import PatientForm
from django.http import Http404

# Create your views here.


@require_GET
def lst(request):
    patients = Patient.objects.all()
    return render(request,"patient/list.html", {"patients" : patients})


@require_GET
def detail(request, id):
    try:
        patient = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return HttpResponse(patient)

@require_GET
def delt(request, id):
    try:
        Patient.objects.get(pk=id).delete()
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return HttpResponseRedirect("/patient/")

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
            info = form.cleaned_data["info"]
            p = Patient(nom=nom, prenom=prenom, adresse=adresse, telephone=telephone, mail=mail, info=info)
            p.save()
            return HttpResponseRedirect("/patient/")
    else:
        form = PatientForm()
    return render(request,"patient/ajout.html", {"form": form})


@require_http_methods(["GET","POST"])
def put(request, id):
    try:
        p = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    else:
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                p.nom = form.cleaned_data["nom"]
                p.prenom = form.cleaned_data["prenom"]
                p.adresse = form.cleaned_data["adresse"]
                p.telephone = form.cleaned_data["telephone"]
                p.mail = form.cleaned_data["mail"]
                p.info = form.cleaned_data["info"]
                p.save()
                return HttpResponseRedirect("/patient/")
        else:
            q = {
                "nom": p.nom,
                "prenom": p.prenom,
                "adresse": p.adresse,
                "telephone": p.telephone,
                "mail": p.mail,
                "info": p.info,
            }
            form = PatientForm(q)
    return render(request,"patient/modif.html", {"form" : form, "id" : p.id})
