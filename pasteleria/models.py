from django.db import models
import datetime
from django.db.models.base import Model
from django.utils.translation import ugettext as _


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

    class Meta:
        permissions = (
            ('Admin', _('Es el Admin')),
            ('Usuario', _('Eres un simple usuario')),
            ('Agregar', _('Puedes agregar clientes')),
            ('Eliminar', _('Puedes eliminar clientes')),
            ('Actualizar', _('Puedes actualizar clientes')),
            ('Buscar', _('Puedes buscar productos')),
        )

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, default="")
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre_producto

    class Meta:
        permissions = (
            ('Admin', _('Es el Admin')),
            ('Usuario', _('Eres un simple usuario')),
            ('Agregar', _('Puedes agregar productos')),
            ('Eliminar', _('Puedes eliminar productos')),
            ('Actualizar', _('Puedes actualizar productos')),
            ('Buscar', _('Puedes buscar productos')),
        )

