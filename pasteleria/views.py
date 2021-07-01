from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from pasteleria.models import Cliente
from django.utils import timezone
from django.urls import reverse


# Create your views here.
def index(request):
    listado_clientes = Cliente.objects.all()
    context = {"listado_clientes": listado_clientes}
    return render(request, "pasteleria/inicio.html", context)

def agregar_clientes(request):
    clientes = Cliente.objects.all()
    carrito = {"clientes": clientes}
    return render(request, "pasteleria/agregar.html", carrito)

def registrar_clientes(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    fecha_nacimiento = request.POST["fecha"]
    direccion = request.POST["direccion"]
    comuna = request.POST["comuna"]
    email = request.POST["correo"]
    agregar = Cliente(rut=rut, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, direccion=direccion, comuna=comuna, email=email)
    agregar.save()
    return HttpResponseRedirect(reverse('pasteleria:inicio'))

def buscar_clientes(request):
    return render(request, "pasteleria/buscar.html")

def mostrar_clientes(request):
    mostrar = request.POST["rut"]
    listado = Cliente.objects.filter(rut__startswith=mostrar)
    lista = {"listado": listado}
    return render(request, "pasteleria/mostrar.html", lista)
    
def eliminar_clientes(request):
    return render(request, "pasteleria/eliminar.html")

def eliminar(request):
    borrar = Cliente.objects.get(rut=request.POST["eliminar"])
    borrar.delete()
    return HttpResponse("Cliente eliminado")



    

