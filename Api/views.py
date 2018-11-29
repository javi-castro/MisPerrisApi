from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario, Mascota, Mensaje
from .serializers import MascotaSerializer
# CREAMOS LA API QUE MOSTRARA TODOS LOS DATOS DE LAS MASCOTAS.
class MascotaApiShow(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)