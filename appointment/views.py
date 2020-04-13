from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET,require_POST
from django.shortcuts import render 
from .models import Rdv
from datetime import date
from django.http import Http404

# Create your views here.

@require_GET
def index(request):
    rdv_jour = Rdv.objects.filter(date=date.today())
    return HttpResponse(rdv_jour)


@require_GET
def show_rdv(request,id):
    try:
        rdv = Rdv.objects.get(pk=id)
    except Rdv.DoesNotExist:
        raise Http404("Rdv does not exist")
    return HttpResponse(rdv)



