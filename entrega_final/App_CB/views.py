from django.shortcuts import render
from contextvars import Context
from django.http import HttpResponse, request, response
from datetime import datetime
from django.template import Template, Context
from App_CB.views import *
from App_CB.forms import *
from App_CB.models import *
from App_CB.templates import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def inicio(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def reservas(self):

    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/reservas.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

@login_required
def edit_perfil(request):
    usuario= request.user
    if request.method == 'POST':
        if formulario.is_valid:

            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2'] 
            usuario.save()

            return render(request, "App_CB/inicio.html")

    else:
        formulario = user_editform(Initial={'email':usuario.mail})
    return render(request, "App_CB/profile.html", {"formulario": formulario, "usuario":usuario})



@csrf_exempt
def reserva(request):
    if request.method=="POST":
        
        varios_ = varios(Importe_nom=request.POST["Importe_nom"],Importe_num=request.POST["Importe_num"],Fecha_importe=request.POST["Fecha_importe"])

        varios_.save()

        return render(request, "App_CB/inicio.html")

    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/reserva.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento) 

def log_in(self):

    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/registration/log_in.html")
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



def about(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/entrega_final/entrega_final/App_CB/templates/App_CB/About.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def inicio_sesion(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            
            if user:
                login(request,user)
                return render(request, "App_CB/inicio.html", {"mensaje":f"bienvenido {user}"})
            
        else:

            return render(request, "App_CB/inicio.html", {"mensaje":"Datos incorrectos."})
        
    else:
    
        form = AuthenticationForm()
    
    return render(request, "App_CB/log_in.html", {"formulario":form})


def register(request):

      if request.method == "POST":

            form = create_user(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App_CB/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:    
            form = create_user()     

      return render(request,"App_CB/register.html" ,  {"formulario":form})

def buscador_reservas(request):

    if request.GET["Fecha_importe"] != "":
        modeloResultados = varios.objects.filter(Fecha_importe=request.GET["Fecha_importe"])

    return render(request,'App_CB/buscador_reservas.html', {"modelo":modeloResultados, "valorFechaImporte":request.GET["Fecha_importe"]})