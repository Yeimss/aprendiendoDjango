from ast import Return
import http
import re
from django.shortcuts import render,HttpResponse, redirect

#mvc = Modelo Vista Controlador
#        ||     ||      ||
#mvt = Modelo Template Vista
def index(request):
    años=""
    year=2021
    for i in range (year, 2051):
        if year % 2 == 0:
            años+=f"<li>{str(year)}</li>"

    nombre='pedro pica piedra'
    lenguajes=['php', 'python', 'C', 'Java']
    return render(request,'index.html',{
        'nombre':nombre,
        'lenguajes':lenguajes
    })


def hola_mundo(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio')
    return render(request, 'hola_mundo.html')
