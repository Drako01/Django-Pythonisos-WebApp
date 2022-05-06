from certifi import contents
from django.http import HttpResponse, Http404
from django.shortcuts import render
import sqlite3, requests


# Create your views here.
def index(request):
    dato = {
        "nombre": "Marcelo Mansilla",
        "edad": 50,
        "direccion": {"calle": "36", "numero": "400" ,"localidad": "La Plata", "provincia": "Buenos Aires", "pais": "Argentina"},
        "cant_hijos": 2,
        "familia":["Alejandro", "Barbara", "Fede", "Lola", "Daisy"],
    }
    return render(request, "blog/index.html", dato)


def acerca_de(request):
    return render(request, "blog/acerca-de.html")


def clientes(request, template_name="blog/clientes.html"):
    conn = sqlite3.connect('contabilidad.sqlite')
    cliente = conn.cursor()
    cliente.execute("select nombre, edad from personas")  
    cliente_list = cliente.fetchall()  
    conn.close()
    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)


def cliente(request, nombre_cliente, template_name='blog/cliente.html'):
    conn = sqlite3.connect('contabilidad.sqlite')
    cursor = conn.cursor()
    cursor.execute("select nombre, edad from personas where nombre=?", [nombre_cliente])    
    cliente_s = cursor.fetchone()
    if cliente_s is None:
        raise Http404
    conn.close()
    dato = {"cliente": cliente_s}
    return render(request, template_name, dato)


def comentarios(request, nombre_peli, comentario_numero):
    if (isinstance(comentario_numero, int)):
        content = {
            "nombre_peli": nombre_peli,
            "comentario_numero": comentario_numero
        }
        return render(request, 'blog/comentarios.html', content)
    return Http404

def cotizacion_dollar(request):
    r = requests.get('https://api.recursospython.com/dollar')
    dollar = r.json()    
    html = """
            <html>
                <head>
                <title> Valor del Dolar </title>
                </head>
                <body>
                    <strong>Compra: </strong> ${compra} </br>
                    <strong>Venta: </strong> ${venta}
                </body>
            """.format(compra=dollar["buy_price"], venta=dollar["sale_price"])    
    return HttpResponse(html)

