from django.shortcuts import render
from contextvars import Context
from django.http import HttpResponse, request
from datetime import datetime
from django.template import Template, Context
from App_CB.views import *
from App_CB.models import *
from App_CB.templates import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.



def inicio(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def log_in(self):

    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/log_in.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def carta(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/menu.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def reg_user(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/reg_user.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def reserva(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/reserva.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)





def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)