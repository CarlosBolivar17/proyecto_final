from django.urls import path
from entrega_final.views import *
from App_CB.views import *
from entrega_final.settings import *
from App_CB.views import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



urlpatterns = [

    path('inicio', inicio, name="inicio"),
    path('carta/', carta, name="carta"),
    path('', inicio_sesion, name="Login"),
    path('register/', register, name="register"),
    path('reserva/', reserva, name="reserva"),
    path('about/', about, name="about"),
    path('logout', LogoutView.as_view(template_name="App_CB/logout.html"), name="logout"),
]