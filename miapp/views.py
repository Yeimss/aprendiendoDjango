from ast import Return
import http
import re
from django.shortcuts import render,HttpResponse, redirect

#mvc = Modelo Vista Controlador
#        ||     ||      ||
#mvt = Modelo Template Vista

layout="""
<h1>Sitio web con Django | James Herrera</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola_mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""
def index(request):
    html=("""
    <h1>Inicio</h1>
    <p>Años pares hasta el 2050</p>
    <ul>
    """)
    year=2021
    for i in range (year, 2051):
        if i %2==0:
            html+=f"<li>{str(i)}</li>"
    html+="</ul>"
    return HttpResponse(layout+html)


def hola_mundo(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio')
    return HttpResponse (layout+"Hola mundo con Django!!")


def contacto(request, nombre="", edad=""):
    html=""
    if nombre and edad:
        html+="<p>Los datos de contacto son: </p>"
        html+=f"<h3>nombre: {nombre}</h3>"
        html+=f"<h3>edad: {edad}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)