from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def estado(request):
    return Response({"app": "Cafetería UTLA", "version": "1.0"})