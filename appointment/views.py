from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET,require_http_methods
from .models import Rdv
from .forms import RdvForm, SearchForm
from datetime import date
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@require_http_methods(["GET","POST"])
def lst(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.cleaned_data)
            if (form.cleaned_data["date"] and form.cleaned_data["patient"]):
                rdvs = Rdv.objects.filter(date=form.cleaned_data["date"] ,patient=form.cleaned_data["patient"])
            elif (form.cleaned_data["date"] and not form.cleaned_data["patient"]):
                rdvs = Rdv.objects.filter(date=form.cleaned_data["date"])
            elif (not form.cleaned_data["date"] and form.cleaned_data["patient"]):
                rdvs = Rdv.objects.filter(patient=form.cleaned_data["patient"])
            else: rdvs = Rdv.objects.all()
    else:
        if request.path == '/' :
            rdvs = Rdv.objects.filter(date=date.today())
            form = SearchForm({"date" : date.today()})
        else:    
            form = SearchForm()
            rdvs = Rdv.objects.all()
    return render(request,"appointment/list.html", {"rdvs" : rdvs, "form": form})

@login_required
@require_GET
def detail(request,id):
    try:
        rdv = Rdv.objects.get(pk=id)
    except Rdv.DoesNotExist:
        raise Http404("Appointment does not exist")
    return HttpResponse(rdv)

@login_required
@require_GET
def delt(request, id):
    try:
        Rdv.objects.get(pk=id).delete()
    except Rdv.DoesNotExist:
        raise Http404("Appointment does not exist")
    return HttpResponseRedirect("/rdv/")

@login_required
@require_http_methods(["GET","POST"])
def add(request):
    if request.method == "POST":
        form = RdvForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            heure = form.cleaned_data["heure"]
            patient = form.cleaned_data["patient"]
            objet = form.cleaned_data["objet"]
            r = Rdv(date=date, heure=heure, patient=patient, objet=objet)
            r.save()
            return HttpResponseRedirect("/rdv/")
    else:
        form = RdvForm()
    return render(request,"appointment/ajout.html", {"form": form})

@login_required
@require_http_methods(["GET","POST"])
def put(request, id):
    try:
        r = Rdv.objects.get(pk=id)
    except Rdv.DoesNotExist:
        raise Http404("Appointment does not exist")
    else:
        if request.method == "POST":
            form = RdvForm(request.POST)
            if form.is_valid():
                r.date = form.cleaned_data["date"]
                r.heure = form.cleaned_data["heure"]
                r.patient = form.cleaned_data["patient"]
                r.objet = form.cleaned_data["objet"]
                r.save()
                return HttpResponseRedirect("/rdv/")
        else:
            q = {
                "date": r.date,
                "heure": r.heure,
                "patient": r.patient,
                "objet": r.objet,
            }
            form = RdvForm(q)
    return render(request,"appointment/modif.html", {"form" : form, "id" : r.id})
