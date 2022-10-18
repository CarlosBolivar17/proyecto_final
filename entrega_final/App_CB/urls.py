from django.urls import path
from entrega_final.views import *
from App_CB.views import *
from entrega_final.settings import *
from App_CB.views import login

urlpatterns = [

    path('', inicio, name="inicio"),
    path('carta/', carta, name="carta"),
    path('iniciarsesion/', inicio_sesion, name="Login"),
    path('reg_user/', reg_user, name="reg_user"),
    path('reserva/', reserva, name="reserva"),
    path('about/', about, name="about"),
]