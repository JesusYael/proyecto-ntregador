import web
import sqlite3
import hashlib

render = web.template.render('mvc/views')


class registrar_usuario:
    def GET(self):
        return render.iniciar.registro()

    def POST(self):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        print(datos)
        with sqlite3.connect("/port_proyecto/db/admivo.sqlite3") as connection:
            cursor = connection.cursor()
            productos_lista = (datos['nombre'],datos['AP'],datos['AM'],datos['email'],hashlib.md5(datos['contra'].encode()).hexdigest())
            print (productos_lista)
            cursor.execute("insert into consesionario (nombre,primer_ap,segundo_ap,email,password) values (?,?,?,?,?);",productos_lista)
            connection.commit()
        raise web.seeother('/ingresar')