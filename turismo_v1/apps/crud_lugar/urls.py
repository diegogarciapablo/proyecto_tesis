
from django.urls import path
from .views import paso1,añadirlugar


urlpatterns = [
	path('add_lugar/',añadirlugar, name='alugar'),
	path('choice/',paso1, name='eleccion'),

]
