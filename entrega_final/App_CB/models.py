from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    Fecha_nacimiento = models.DateField()

class administrador(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    Fecha_nacimiento = models.DateField()


class reserva(models.Model):
    nombre_asociado = models.CharField(max_length=60)
    cantidad_pax = models.IntegerField()
    Fecha_ingreso = models.DateField()