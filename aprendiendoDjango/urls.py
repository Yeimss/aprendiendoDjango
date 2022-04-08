"""aprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
#importar app con las views
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('inicio/',views.index, name="inicio"),
    path('hola_mundo/', views.hola_mundo, name="hola_mundo"),
    path('hola_mundo/<int:redirigir>/', views.hola_mundo, name="hola_mundo"),
    path('pagina/', views.pagina, name='pagina'),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('create_article/', views.create_article, name="create_article"),
    path('save_article/', views.save_article, name="save"),
    path('article/', views.article, name="article"),
    path('edit_article/<str:id>', views.editar_article, name="edit_article"),
    path('articulos/', views.articulos, name="articulos"),
    path('eliminar_articulo/<str:id>', views.eliminar_articulo, name="borrar"),
    path('create-full-article/',views.create_full_article, name="create_full")
]   
