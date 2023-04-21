import web

render = web.template.render('mvc/views')


class unidades:
    def GET(self):
        return render.paneles.unidades()