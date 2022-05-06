from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca-de', views.acerca_de, name='acerca-de'),
    path('clientes', views.clientes, name='clientes'),
    path('cliente/<str:nombre_cliente>', views.cliente, name='cliente'),
    path('peliculas/<str:nombre_peli>/comentarios/<int:comentario_numero>', views.comentarios, name='comentarios'),
    path('cotizacion-dollar', views.cotizacion_dollar, name='cotizacion-dollar')
]