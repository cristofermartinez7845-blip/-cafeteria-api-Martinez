from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .datos import platos


@api_view(["GET"])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})

@api_view(["GET", "POST"])
def lista_platos(request):
    return Response(platos)