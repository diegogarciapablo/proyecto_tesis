
from django.urls import path
from .views import paso1,AñadirLugar, CrearColegio, CrearIglesia, CrearAlojamiento, CrearPlaza, CrearRestaurante


urlpatterns = [
	path('add_lugar/',AñadirLugar, name='alugar'),
	path('choice/',paso1, name='eleccion'),
	path('add_lugar/AColegio/', CrearColegio, name='AColegio'),
	path('add_lugar/church/',CrearIglesia, name='church'),
	path('add_lugar/lodgings/',CrearAlojamiento, name='lodgings'),
	path('add_lugar/square/',CrearPlaza, name='square'),
	path('add_lugar/restaurant/',CrearRestaurante, name='restaurant')
]
