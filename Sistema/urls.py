from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns=[
    url(r'^index/$', views.index,name="indice"),
    url(r'^nosotros/$', views.nosotros,name="nosotros"),
    url(r"^contacto/$", views.contacto, name = "contacto"),
    url(r'^login/$', views.ingresar, name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^registrate/$',views.registrate,name="registrate"),
    url(r'^registromascota/$',views.registrarmascota,name="registrarmascota"),
    url(r'^mascota/$',views.listar,name="mascota"),
    url(r'^contraseña/$', views.cambiarcontraseña, name='cambiarcontraseña'),
    url(r'^password_reset/$',PasswordResetView.as_view(),{'template_name':'recuperarcontraseña/password_reset_form.html',
    'email_template':'recuperarcontraseña/password_reset_email.html'}, name="password_reset"),
    url(r'^password_reset_done/$',PasswordResetDoneView.as_view(),{'template_name':'recuperarcontraseña/password_reset_done.html'},
    name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',PasswordResetConfirmView.as_view(),{'template_name':'recuperarcontraseña/password_reset_confirm.html'},
    name="password_reset_confirm"),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'recuperarcontraseña/password_reset_complete.html'},
    name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)