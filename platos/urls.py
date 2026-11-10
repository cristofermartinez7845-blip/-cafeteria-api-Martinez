from django.urls import path
from . import views

urlpatterns = [
    path("estado/", views.estado),
    path("platos/", views.lista_platos),
    path("platos/<int:id>/", views.plato_detalle),
]