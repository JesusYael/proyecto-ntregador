import web
import sqlite3

render = web.template.render('mvc/views')


class operadores:
    def GET(self):
        return render.paneles.operadores()

    def POST(self):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        print(datos)
        with sqlite3.connect("/port_proyecto/db/admivo.sqlite3") as connection:
            cursor = connection.cursor()
            lista = (datos['nombre'],datos['apellido1'],datos['apellido2'],datos['curp'],datos['licencia'])
            print (lista)
            cursor.execute("insert into choferes (nombre,primer_ap,segundo_ap,curp,numero_licencia) values (?,?,?,?,?);",lista)
            connection.commit()
        raise web.seeother('/choferes')