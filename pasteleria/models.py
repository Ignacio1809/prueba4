from django.db import models
import datetime
from django.db.models.base import Model


# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=100, default="")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField("Fecha de nacimiento")
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):  
        return self.rut

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, default="")
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre_producto

