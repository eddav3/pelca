from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HolaMundo(APIView):
    def get (self, requeste , format = None):
        return Response({'mensaje': 'Hola Mundo Prueba de Vista'})


hola_mundo = HolaMundo.as_view()