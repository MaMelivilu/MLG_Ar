from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarInicio),
    path('compras',views.cargarCompras),
    path('streams',views.cargarStreams),
    path('transmitir',views.transmitir_view),
    path('verstream',views.ver_stream),
    path('llamada',views.llamada),
    path('perfil', views.cargarPerfil)
    
]
from django.shortcuts import render

