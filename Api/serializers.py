from rest_framework import serializers
from .models import Mascota, Usuario
#CREAMOS UN SERIALIZER QUE MUESTRE LAS MASCOTAS CON TODOS SUS DATOS
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = Mascota