from django.contrib import messages
from django.shortcuts import render,HttpResponse, redirect
from miapp.models import Article
from miapp.forms import FormArticle
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

def crear_articulo(request, title, content, public):
    article = Article(
        title=title,
        content=content,
        public=public
    )
    article.save()
    return HttpResponse(f"Articulo Creado: {article.title} - {article.content}")

def save_article(request):
    #-----------guardar con metodo GET------------------------
    """ 
    if request.method=='GET':

        title=request.GET['title']
        content=request.GET['content']
        public=request.GET['public']

        article = Article(
            title=title,
            content=content,
            public=public
        )
        article.save()
        return HttpResponse(f"Articulo Creado: {article.title} - {article.content}")
    else:
        return HttpResponse(f"No se ha podido crear el articulo")
    """
    #-----------guardar con metodo POST------------------------
    if request.method=='POST':

        titulo=request.POST['title']
        contenido=request.POST['content']
        publico=request.POST['public']

        article = Article(
            title=titulo,
            content=contenido,
            public=publico
        )
        article.save()
        return HttpResponse(f"Articulo Creado: {article.title} - {article.content}")
    else:
        return HttpResponse(f"No se ha podido crear el articulo")
    
def create_full_article(request):

    if request.method=='POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form= formulario.cleaned_data
            title=data_form.get('title')
            content=data_form['content']
            public=data_form['public']
            article = Article(
            title=title,
            content=content,
            public=public
            )
            article.save()
            #crear mensaje flash(sesion que solo se muestra una vez)
            messages.success(request, f'Has creado un articulo {article.id}. {article.title} correctamente ')
            return redirect('articulos')
            #return HttpResponse(f"{title} - {content} - {public}")
    else:
        formulario=FormArticle()
    return render(request, 'create_full_article.html',
    {
        'form':formulario
    })


def create_article(request):
    return render(request, 'create_article.html')
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
    articulos=Article.objects.order_by('-id')#[:3]
    #se pueden poner corchetes al final que sería limite o el top que deseamos en la consulta
    #o se puede poner un rango con [n1:n2] donde n1 es el limite inferior y n2 es el limite superior
    """ 
    #articulos=Article.objects.filter(title="batman", public=True)-> sive para filtrar por columna y un valor en dicha columna
    #articulos=Article.objects.filter(title__contains="batman")-> __contains es como un like en sql
    #articulos=Article.objects.filter(title__exacts="articulo")
    #articulos=Article.objects.filter(title="vacio").exclude(public=False)
    #articulos=Article.objects.exclude(public=False)
    #articulos=Article.objects.raw("SELECT * FROM miapp_article WHERE id>7")
    """
    return render(r, 'articulos.html', {
        'articulos':articulos
    })

def eliminar_articulo(request,id):
    articulos=Article.objects.get(pk=id)
    articulos.delete()
   
    return redirect('articulos')