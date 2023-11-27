from django import forms
from django.shortcuts import render,redirect
from .models import *
import os 
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def cargarInicio(request):
    juegos = Juegos.objects.all() 
    return render(request, "inicio.html",{"juegos":juegos})

def cargarCompras(request):
    productos = Producto.objects.all()
    return render(request, "compras.html",{"prod":productos})

def cargarStreams(request): 
    stream = Streamers.objects.all() 
    return render(request, "streams.html",{"stream":stream})

def transmitir_view(request):
  mensajes = Chat.objects.all()
  return render(request, 'transmitir.html',{"msj":mensajes})

def ver_stream(request):
    return render(request,'verstream.html')

def cargarPerfil(request):
    return render(request,'perfil.html')

def llamada(request): 
    return render(request, "llamada.html")

