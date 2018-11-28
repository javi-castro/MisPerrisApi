from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mascota/$', views.MascotaApiShow.as_view()),
]