
from django.urls import path
from .views import paso1,AñadirLugar, CrearColegio, CrearIglesia, CrearAlojamiento


urlpatterns = [
	path('add_lugar/',AñadirLugar, name='alugar'),
	path('choice/',paso1, name='eleccion'),
	path('add_lugar/AColegio/', CrearColegio, name='AColegio'),
	path('add_lugar/church/',CrearIglesia, name='church'),
	path('add_lugar/lodgings/',CrearAlojamiento, name='lodgings')
]
