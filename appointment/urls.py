from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rdv/<int:id>/",views.show_rdv, name="show_rdv"),
]