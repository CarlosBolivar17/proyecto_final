from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    Fecha_nacimiento = models.DateField()

class administrador(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    Fecha_nacimiento = models.DateField()


class varios(models.Model):
    Importe_nom = models.CharField(max_length=60)
    Importe_num = models.IntegerField()
    Fecha_importe = models.DateField()


