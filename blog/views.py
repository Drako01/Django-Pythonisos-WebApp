from django.http import HttpResponse
from django.shortcuts import render
import sqlite3, requests


# Create your views here.
def index(request):
    dato = {
        "nombre": "Alejandro",
        "edad": 45,
        "direccion": {"calle": "Catamarca 2112", "localidad": "Quilmes Oeste"}
    }
    return render(request, "blog/index.html", dato)

def acerca_de(request):
    return render(request, "blog/acerca-de.html")

def clientes(request):
    conn = sqlite3.connect('contabilidad.sqlite')
    cliente = conn.cursor()
    cliente.execute("select nombre, edad from personas")
    html = """
            <html>
            <title> Lista de Clientes </title>
            <table style="border: 2px solid; background: yellow">
            <thead>
                <tr>
                <th> Nombre </th>
                <th> Edad </th>
                </thead>
            """
    for (nombre, edad) in cliente.fetchall():
        html += "<tr><td>" + nombre + "</td><td>" + str(edad) + "</td></tr>"
    html += '</table></html>'
    conn.close()
    return HttpResponse(html)

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

