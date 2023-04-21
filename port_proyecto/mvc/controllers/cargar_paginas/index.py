import requests
import json
import web
import urllib.parse
import folium
import polyline
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from web import form


render = web.template.render('mvc/views')
cred = credentials.Certificate("./llave/key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


render = web.template.render('mvc/views')


class ver_pagina:
    def GET(self):
        return render.index.index()

class mostrar_sesion:
    def GET(self):
        return render.iniciar.sesion()

class inicio:
    def GET(self):
        collection_ref = db.collection('mensajes')

        # Obtener todos los documentos de la colección
        query_snapshot = collection_ref.stream()

        datos = {}

        for document in query_snapshot:
            datos[document.id] = document.to_dict()

        # Recorrer todos los documentos y agregar su contenido al diccionario
        for clave in datos.keys():
            # Acceder al valor de la clave en cada documento
            asunto = datos[clave]['asunto']
            fecha = datos[clave]['fecha']
            mensaje = datos[clave]['mensaje']
            print(asunto)
            print(fecha)
            print(mensaje)

        # Imprimir el diccionario con los datos
        print(datos)

        return render.iniciar.tablero(datos)
    def POST(self):
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        datos= dict(web.input())
        print(datos)
        print (datos["latitud"])
        print (datos["longitud"])
        latitud = datos["latitud"]
        longitud = datos["longitud"]
        # Crea un mapa de Folium centrado en el punto de inicio
        mapa = folium.Map(location=[latitud, longitud], zoom_start=16)
        folium.Marker(location= [latitud,longitud], tooltip='UNIDAD #').add_to(mapa)
        # Muestra el mapa
        mapa.save('mvc/views/mapa/mapa.html')


        
        raise web.seeother('/inicio')