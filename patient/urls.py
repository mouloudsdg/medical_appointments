from django.urls import path
from . import views

app_name = "patient"

urlpatterns = [
    path("", views.lst, name="list"),
    path("<int:id>/", views.detail, name="detail"),
    path("suppr/<int:id>", views.delt, name="delete"),
    path("ajout", views.add, name="add"),
    path("modif/<int:id>", views.put, name="put"),
]