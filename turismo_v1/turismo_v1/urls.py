"""turismo_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.mapa_main.views import Home,Mapa,Tour
from apps.crud_lugar.views import añadirlugar,paso1


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('users/',include(('apps.usuario.urls','usuario')))
    path('',Home,name='index'),
    path('mapa/',Mapa,name='mapa'),
    path('tour/',Tour,name='recorrido'),
    path('adminstrador/', include (('apps.crud_lugar.urls','crud'))),
]
