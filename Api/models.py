from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #Agregamos datos
    codigoUsuario = models.AutoField(primary_key = True)
    rut = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 50)
    fecha = models.DateField()
    telefono = models.CharField(max_length= 9)
    region=models.CharField(max_length=30)
    ciudad=models.CharField(max_length=30)
    tipoVivienda = models.CharField(max_length = 20)

class Mascota(models.Model):
    codigoMascota = models.AutoField(primary_key = True)
    fotoMascota = models.ImageField(upload_to='FotosMascotas/')
    nombreMascota = models.CharField(max_length = 20)
    raza = models.CharField(max_length = 20)
    descripcion = models.TextField()
    estado = models.CharField(max_length = 15)

class Mensaje(models.Model):
    codigoMensaje = models.AutoField(primary_key = True)
    nombreMensaje = models.CharField(max_length = 30)
    correoMensaje = models.EmailField(max_length = 30)
    mensaje = models.TextField()