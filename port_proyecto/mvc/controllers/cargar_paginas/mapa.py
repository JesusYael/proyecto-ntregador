import web

render = web.template.render('mvc/views')


class mapa:
    def GET(self):
        return render.mapa.mapa()