import web

render = web.template.render('mvc/views')


class mantenimiento:
    def GET(self):
        return render.paneles.mantenimiento()