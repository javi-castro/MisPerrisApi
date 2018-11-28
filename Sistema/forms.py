from django import forms
from Api.models import Mascota
#ESTADO DE LAS MASCOTAS
ESTADO = (
    ("rescatado","Rescatado"),
    ("disponible","Disponible"),
    ("adoptado","Adoptado")
)

#VIVIENDA PARA QUE LOS CLIENTES PUEDAN SELECCIONAR EL TIPO DE CASA O DEPTO TIENEN
VIVIENDA = (
    ("casa-patio-grande", "Casa con patio grande"),
    ("casa-patio-chico", "Casa con patio pequeño"),
    ("casa-sin-patio", "Casa sin patio"),
    ("dpto", "Departamento")
)

regiones=(
    ('1','Región Metropolitana'),
    ('2','IV Región'),
)

ciudades=(
    ('1', 'Santiago'),
    ('2', 'Vicuña'),
)

#CREAMOS EL LOGIN PARA QUE EL USUARIO PUEDA INGRESAR
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario:")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

#CREAMOS EL FORMULARIO PARA QUE LOS CLIENTES PUEDAN INGRESAR SUS DATOS
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario:")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña:")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo:")
    rut=forms.CharField(widget=forms.TextInput(attrs={'pattern':'[0-9]{1,2}.[0-9]{3}.[0-9]{3}-[0-9Kk]{1}'}), label= "Run:")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre")
    fecha=forms.DateField(widget=forms.SelectDateWidget(years=range(2018, 1939,-1)), label="Fecha Nacimiento:")
    telefono=forms.CharField(widget=forms.TextInput(),label="Telefono:")
    region=forms.ChoiceField(choices=regiones,label="Region:")
    ciudad=forms.ChoiceField(choices=ciudades,label="Ciudad:")
    tipoVivienda=forms.ChoiceField(choices=VIVIENDA,label="Tipo vivienda:")

#CREAMOS EL FORMULARIO PARA QUE EL ADMINISTRADOR PUEDA AGREGAR MASCOTAS
class AgregarMascotas(forms.Form):
    fotoMascota=forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota")
    raza=forms.CharField(widget=forms.TextInput(),label="Raza Mascota")
    descripcion=forms.CharField(widget = forms.Textarea(attrs = { "placeholder": "Ingrese descripción" }), label = "Descripción")
    estado=forms.ChoiceField(choices=ESTADO, initial='Rescatado')

#CREAMOS UN FORMULARIO DE CONTACTO
class Contacto(forms.Form):
    nombreMensaje = forms.CharField(widget = forms.TextInput(attrs = { "placeholder": "Ingrese nombre" }), label = "Nombre")
    correoMensaje = forms.EmailField(widget = forms.EmailInput(attrs = { "placeholder": "Ingrese correo" }), label = "Correo electrónico")
    mensaje = forms.CharField(widget = forms.Textarea(attrs = { "placeholder": "Ingrese mensaje" }), label = "Mensaje")