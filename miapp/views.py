from ast import Return
import http
import re
from django.shortcuts import render,HttpResponse, redirect

#mvc = Modelo Vista Controlador
#        ||     ||      ||
#mvt = Modelo Template Vista
def index(request):
    return render(request,'index.html')


def hola_mundo(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio')
    return render(request, 'hola_mundo.html')
