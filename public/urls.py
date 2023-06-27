from django.urls import path
from . import views
urlpatterns = [

    path('', views.index , name='Inicio'),
    path('bebidas', views.bebidas , name='bebidas'),
    path('carrusel', views.carrusel , name='carrusel'),
    path('contacto', views.contacto , name='contacto'),
    path('jamones', views.jamones , name='jamones'),
    path('opiniones', views.opiniones , name='opiniones'),
    path('quesos', views.quesos, name='quesos'),
    path('hi', views.hola_mundo, name='hola mundo'),
    path('saludar/<str:nombre>/', views.saludar, name='saludo'),
    path('ver_proyectos/<int:anio>/<int:mes>', views.ver_proyectos, name='proyectos'),
]