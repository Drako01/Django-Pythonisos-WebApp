from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca-de', views.acerca_de, name='acerca-de'),
    path('clientes', views.clientes, name='clientes'),
    path('cotizacion-dollar', views.cotizacion_dollar, name='cotizacion-dollar')
]