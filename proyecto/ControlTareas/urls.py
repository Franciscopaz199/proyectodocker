"""ControlTareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ControlTareas.Libreria.lib import Lib
from ControlTareas.Libreria.libPrograma import LibPrograma

Libreria = Lib()
Libreria2 = LibPrograma()

urlpatterns = [
    path('', Libreria.index, name = '/'),
    path('validar/', Libreria.validar,name = 'validar'),
    path('admin/', Libreria.admin, name = 'admin'),
    path('logout/', Libreria.logout, name = 'logout'),
    
    ####################################################################################
    path('agregar/', Libreria2.Agregar, name="agregar"),
    path('listar/', Libreria2.listar, name="listar"),
    path('eliminar/', Libreria2.eliminar, name="eliminar"),
    path('eliminartarea/', Libreria2.eliminartarea, name="eliminartarea"),

    path('actualizar/', Libreria2.actualizar, name="actualizar"),
    path('actualizartarea/', Libreria2.actualizartarea, name="actualizartarea"),
    path('fecha/', Libreria2.fecha, name="fecha"),
    path('contar/', Libreria2.contar, name="contar"),
    path('atrasadas/', Libreria2.atrasadas, name="atrasadas"),
    path('tareasMes/', Libreria2.tareasMes, name="tareasMes"),
]





