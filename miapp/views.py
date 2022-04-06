from urllib import response
from django.shortcuts import render,HttpResponse, redirect
from miapp.models import Article

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

def create_article(request, title, content, public):
    article = Article(
        title=title,
        content=content,
        public=public
    )
    article.save()
    return HttpResponse(f"Articulo Creado: {article.title} - {article.content}")


def article(request):
    try:
        articulo = Article.objects.get(title="aguacates", public=not 1)
        response=f"<h1>Article: {articulo.title} - {articulo.content} <br/> ^-^</h1>"
    except:
        response=f"<h1>Articulo no encontrado >.<</h1>"
    return HttpResponse(response)

def editar_article(r,id):
    articulo=Article.objects.get(pk=id)

    articulo.title="Batman"
    articulo.content="Nananananananananan Batmaaaaaan"
    articulo.public="True"

    articulo.save()

    return HttpResponse(f"Articulo Editado: {articulo.title} - {articulo.content}")

def articulos(r):
    articulos=Article.objects.order_by("-id")#[:3]
    #se pueden poner corchetes al final que sería limite o el top que deseamos en la consulta
    #o se puede poner un rango con [n1:n2] donde n1 es el limite inferior y n2 es el limite superior
    return render(r, 'articulos.html', {
        'articulos':articulos
    })

def eliminar_articulo(request,id):
    articulos=Article.objects.get(pk=id)
    articulos.delete()
   
    return redirect('articulos')