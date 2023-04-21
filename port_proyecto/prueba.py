import geocoder

def obtener_latitud_longitud():
    g= geocoder.ip('me')
    latitud, longitud = g.latlng
    print(f'Latitud:{latitud}, longitud:{longitud}')

obtener_latitud_longitud()
