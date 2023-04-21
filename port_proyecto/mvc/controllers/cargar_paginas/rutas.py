import web

render = web.template.render('mvc/views')


class rutas:
    def GET(self):
        return render.paneles.ruta()