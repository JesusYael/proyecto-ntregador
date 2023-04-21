import web
import hashlib
import sqlite3

render = web.template.render('mvc/views')


class mostrar_inicio:
    def GET(self):
        return render.iniciar.sesion()
    def POST(self):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        print(datos)
        with sqlite3.connect("/port_proyecto/db/admivo.sqlite3") as connection:
            # Obtener los valores del formulario de inicio de sesión
            cursor = connection.cursor()
            username = datos["user"]
            password = hashlib.md5(datos['contra'].encode()).hexdigest()
            # Validar los valores en la base de datos utilizando una consulta SQL SELECT
            
            cursor.execute("SELECT * FROM consesionario WHERE email=? AND password=?;", (username, password))
            user = cursor.fetchone()
            numero = user[0]
            if user:
                # Si el usuario y la contraseña existen, permitir que el usuario inicie sesión
                web.setcookie('username', username)
                raise web.seeother('/inicio')
            else:
                # Si no existen, mostrar un mensaje de error
                self.error_message = "Correo electrónico o contraseña incorrectos."
                return self.GET()