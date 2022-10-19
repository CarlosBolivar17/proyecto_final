from django.urls import path
from entrega_final.views import *
from App_CB.views import *
from entrega_final.settings import *
from App_CB.views import login

urlpatterns = [

    path('', inicio, name="inicio"),
    path('carta/', carta, name="carta"),
    path('iniciarsesion/', inicio_sesion, name="Login"),
    path('register/', register, name="register"),
    path('reserva/', reserva, name="reserva"),
    path('about/', about, name="about"),
]