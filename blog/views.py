from django.http import HttpResponse
from django.shortcuts import render
import sqlite3, requests


# Create your views here.
def index(request):
    dato = {
        "nombre": "Alejandro",
        "edad": 46,
        "direccion": {"calle": "Cuchuflito 2112", "localidad": "Quilmes Oeste", "provincia": "Buenos Aires", "pais": "Argentina"},
        "cant_hijos": 2,
        "hijos":["Alejandro", "Barbara", "Fede", "Lola", "Daisy"],
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

