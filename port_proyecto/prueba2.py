from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_app")

def obtener_ubicacion(latitud,longitud):
    location = geolocator.reverse(f'{latitud},{longitud}')
    return location.address

obtener_ubicacion(latitud,longitud)