from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import AgregarUsuario ,Login, AgregarMascotas, Contacto
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from Api.models import Usuario, Mascota, Mensaje
from django.core import serializers
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.
acciones=[
   {'Mostrar':'Home','url':'inicio'}
]

#DEFINIMOS INICIO
def index(request):
    return render(request, "index.html")
#DEFINIMOS SALIR
def salir(request):
    logout(request)
    return redirect('indice')
#CREAMOS LA VISTA NOSOTROS PARA QUE SE PUEDAN INFORMAR ACERCA DE LA FUNDACIÓN
def nosotros(request):
	return render(request, "nosotros.html")

#CREAMOS LA VISTA PARA QUE LOS CLIENTES PUEDAN CONTACTARSE CON LA LA FUNDACIÓN
def contacto(request):
    if request.method=='POST':
        form=Contacto(request.POST)
        if form.is_valid():
            titulo="Titulo del mensaje o asunto"
            contenido=form.cleaned_data['mensaje']+"\n"
            contenido+="comunicarse a "+form.cleaned_data['correo']
            correo=EmailMessage(titulo,contenido,to=['contacto.misperris.javiera@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        form=Contacto()
    return render_to_response('contacto.html',{'form':form,})

#DEFINIMOS EL REGISTRATE PARA QUE LOS CLIENTES PUEDAN LLENAR EL FORMULARIO DE REGISTRO CON SUS DATOS
def registrate(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo"), data.get("password"))
        usuario=Usuario(user=regDB,rut=data.get("rut"),nombre=data.get("nombre"),fecha=data.get("fecha"),telefono=data.get("telefono"),region=data.get("region"),ciudad=data.get("ciudad"),tipoVivienda=data.get("tipoVivienda"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    contexto={
        'actual':actual, 
        'form':form, 
        'usuarios':usuarios,
        }
    return render(request, "registrate.html", contexto)

#DEFINIMOS EL LOGIN PARA QUE EL USUARIO PUEDA LOGUEARSE AL SISTEMA
def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('mascota')
    return render(request,"login.html",{'form':form,})

#HACEMOS UN LOGIN_REQUIRED PARA PODER AGREGAR MASCOTAS 
@login_required(login_url='login')
def registrarmascota(request):
    actual=request.user
    form=AgregarMascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        mascota=Mascota(fotoMascota=request.FILES["fotoMascota"],nombreMascota=data.get("nombreMascota"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"))
        mascota.save()
    #mascotas=Mascota.objects.all()
    form=AgregarMascotas()

    contexto = {
        'actual':actual, 
        'form':form, 
    }
    return render(request,"listarMascota.html",contexto)
#VISTAS PARA VER LAS MASCOTAS REGISTRADAS
@login_required(login_url='login')
def listar(request):
    actual=request.user
    form=AgregarMascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        mascota=Mascota(fotoMascota=data.get("fotoMascota"),nombreMascota=data.get("nombreMascota"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"))
        mascota.save()
    mascota=Mascota.objects.all()
    paginator = Paginator(mascota, 4)
    page = request.GET.get('page')
    mascota = paginator.get_page(page)
    return render(request,"listar.html",{'paginator':paginator,'actual':actual,'form':form,'mascota':mascota,'acciones':acciones,})

#VISTA PARA CAMBIAR CONTRASEÑA
@login_required(login_url='login')
#View para cambiar la password 
def cambiarcontraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('La Contraseña ha sido cambiada correctamente'))
            return redirect('cambiarcontraseña')
        else:
            messages.error(request, ('Por favor verificar que los datos ingresados esten correctos.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "cambiarcontraseña.html", {
        'form': form
    })
