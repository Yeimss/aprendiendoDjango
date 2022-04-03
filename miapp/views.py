from ast import Return
import http
import re
from django.shortcuts import render,HttpResponse, redirect

#mvc = Modelo Vista Controlador
#        ||     ||      ||
#mvt = Modelo Template Vista
def index(request):
    rango=range(2022, 2051)
    nombre='pedro pica piedra'
    lenguajes=['php', 'python', 'C', 'Java']
    return render(request,'index.html',{
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':rango
    })


def hola_mundo(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio')
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html',{
        'texto':"",
        'lista':['uno','dos','tres','siete','perro','manco']
    })