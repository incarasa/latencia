"""Defines URL patterns for manejador_usuarios."""

from django.urls import path

from . import views

app_name = 'manejador_usuarios'
urlpatterns = [
    #Pagina para añadir un nuevo pago
    path('nuevo_pago/', views.nuevo_pago, name='nuevo_pago'),
    #pagina vacia
    path('', views.home, name='home'),
]