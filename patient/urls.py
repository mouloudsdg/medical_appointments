from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:id>/", views.detail, name="detail"),
    path("suppr/<int:id>", views.delt, name="delete"),
    path("ajout", views.add, name="add"),
    #path("modif", views.put, name="put"),
]