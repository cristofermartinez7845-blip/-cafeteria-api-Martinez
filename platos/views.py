from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .datos import platos
from rest_framework import status


@api_view(["GET"])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})

@api_view(["GET", "POST"])
def lista_platos(request):
    if request.method == "GET":
        return Response(platos)

    nombre = request.data.get("nombre")
    precio = request.data.get("precio")

    if not nombre or precio is None:
        return Response(
            {"error": "nombre y precio son obligatorios"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    nuevo_id = max(p["id"] for p in platos) + 1
    nuevo = {"id": nuevo_id, "nombre": nombre, "precio": precio}
    platos.append(nuevo)
    return Response(nuevo, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def plato_detalle(request, id):
    for plato in platos:
        if plato["id"] == id:
            return Response(plato)
    return Response({"error": "Plato no encontrado"}, status=status.HTTP_404_NOT_FOUND)