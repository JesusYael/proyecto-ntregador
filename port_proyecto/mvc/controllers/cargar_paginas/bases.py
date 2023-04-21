import web

render = web.template.render('mvc/views')


class bases:
    def GET(self):
        return render.paneles.base()