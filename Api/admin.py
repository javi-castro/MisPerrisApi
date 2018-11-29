from django.contrib import admin
from .models import Usuario
from .models import Mascota
# Register your models here.
#EL ADMINISTRADOR PODRA REALIZAR CAMBIOS EN LOS USUARIOS Y MASCOTAS
admin.site.register(Usuario)
admin.site.register(Mascota)