import web
from web import form
urls = (
    
    '/', 'mvc.controllers.cargar_paginas.index.ver_pagina',
    '/ingresar', 'mvc.controllers.sesion.sesion.mostrar_inicio',
    '/registro', 'mvc.controllers.usuarios.registro_usuarios.registrar_usuario',
    '/inicio', 'mvc.controllers.cargar_paginas.index.inicio',
    '/unidades', 'mvc.controllers.cargar_paginas.unidades.unidades',
    '/operadores', 'mvc.controllers.cargar_paginas.operadores.operadores',
    '/rutas', 'mvc.controllers.cargar_paginas.rutas.rutas',
    '/bases', 'mvc.controllers.cargar_paginas.bases.bases',
    '/mantenimiento', 'mvc.controllers.cargar_paginas.mantenimiento.mantenimiento',
    '/mapa', 'mvc.controllers.cargar_paginas.mapa.mapa',
    
     
)
app = web.application(urls, globals()) #aplicacion web

if __name__ == "__main__":
    app.run()