
from django.urls import path
from .views import paso1,AñadirLugar, CrearColegio, CrearIglesia, CrearAlojamiento, CrearPlaza,CrearRestaurante, ListarColegio, ListarPlaza, ListarRestaurante, ListarAlojamiento, ListarIglesia, EditarColegio, EditarIglesia, EditarAlojamiento, EditarPlaza, EditarRestaurante
from .views import EliminarColegio, EliminarIglesia, EliminarPlaza, EliminarRestaurante, EliminarAlojamiento,MostrarMapa
from .views import AñadirEvento, AgregarFoto, ListarEvento, ListarFoto, EditarEvento, EditarFoto, EliminarEvento, EliminarFoto
urlpatterns = [

	path('add_lugar/',AñadirLugar, name='alugar'),
	path('choice/',paso1, name='eleccion'),
	path('add_lugar/AColegio/', CrearColegio, name='AColegio'),
	path('add_lugar/church/',CrearIglesia, name='church'),
	path('add_lugar/lodgings/',CrearAlojamiento, name='lodgings'),
	path('add_lugar/square/',CrearPlaza, name='square'),
	path('add_lugar/restaurant/',CrearRestaurante, name='restaurant'),

	path('list_colegio/',ListarColegio, name='list_colegio'),
	path('list_plaza/',ListarPlaza, name='list_plaza'),
	path('list_iglesia/',ListarIglesia, name='list_iglesia'),
	path('list_alojamiento/',ListarAlojamiento, name='list_alojamiento'),
	path('list_restaurante/',ListarRestaurante, name='list_restaurante'),

	path('editar_colegio/<int:cod_colegio>',EditarColegio, name='editar_colegio'),
	path('editar_iglesia/<int:cod_iglesia>',EditarIglesia, name='editar_iglesia'),
	path('editar_alojamiento/<int:cod_alojamiento>',EditarAlojamiento, name='editar_alojamiento'),
	path('editar_plaza/<int:cod_plaza>',EditarPlaza, name='editar_plaza'),
	path('editar_restaurante/<int:cod_restaurante>',EditarRestaurante, name='editar_restaurante'),

	path('eliminar_colegio/<int:cod_colegio>',EliminarColegio, name='eliminar_colegio'),
	path('eliminar_iglesia/<int:cod_iglesia>',EliminarIglesia, name='eliminar_iglesia'),
	path('eliminar_plaza/<int:cod_plaza>',EliminarPlaza, name='eliminar_plaza'),
	path('eliminar_restaurante/<int:cod_restaurante>',EliminarRestaurante, name='eliminar_restaurante'),
	path('eliminar_alojamiento/<int:cod_alojamiento>',EliminarAlojamiento, name='eliminar_alojamiento'),


	path('add_lugar/evento/',AñadirEvento, name='evento'),
	path('add_lugar/img/',AgregarFoto, name='img'),

	path('list_evento/',ListarEvento, name='list_evento'),
	path('list_foto/',ListarFoto, name='list_foto'),

	path('editar_evento/<int:cod_evento>',EditarEvento, name='editar_evento'),
	path('editar_foto/<int:cod_foto>',EditarFoto, name='editar_foto'),

	path('eliminar_evento/<int:cod_evento>',EliminarEvento, name='eliminar_evento'),
	path('eliminar_foto/<int:cod_foto>',EliminarFoto, name='eliminar_foto'),

	path('mapa/',MostrarMapa,name='mapa'),

]
