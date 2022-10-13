from django.shortcuts import render
from contextvars import Context
from django.http import HttpResponse, request
from datetime import datetime
from django.template import Template, Context
from App_CB.views import *
from App_CB.models import *
from App_CB.templates import *

# Create your views here.



def inicio(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def nosotros(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/about_us.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

