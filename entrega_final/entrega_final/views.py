from django.http import HttpRequest, HttpResponse
from contextvars import Context
from django.template import Template, Context
from django.shortcuts import render

def test_inicio(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/entrega_final/templates/template_1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)