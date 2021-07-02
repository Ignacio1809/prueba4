from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from pasteleria.models import Cliente, Producto
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

def agregar_producto(request):
    productos = Producto.objects.all()
    carrito = {"producto": productos}
    return render(request, "pasteleria/agregar_producto.html", carrito)

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

def registrar_producto(request):
    nombre_producto = request.POST["nombre_producto"]
    precio = request.POST["precio"]
    descripcion= request.POST["descripcion"]
    agregar = Producto(nombre_producto=nombre_producto, precio=precio, descripcion= descripcion)
    agregar.save()
    return HttpResponseRedirect(reverse('pasteleria:inicio'))

def buscar_clientes(request):
    return render(request, "pasteleria/buscar.html")
    
def buscar_producto(request):
    return render(request, "pasteleria/buscar_producto.html")


def mostrar_clientes(request):
    mostrar = request.POST["rut"]
    listado = Cliente.objects.filter(rut__startswith=mostrar)
    lista = {"listado": listado}
    return render(request, "pasteleria/mostrar.html", lista)

def mostrar_producto(request):
    mostrar = request.POST["nombre_producto"]
    listado = Producto.objects.filter(nombre_producto__startswith=mostrar)
    lista = {"listado": listado}
    return render(request, "pasteleria/mostrar_producto.html", lista)
    
def eliminar_clientes(request):
    return render(request, "pasteleria/eliminar.html")

def eliminar_producto(request):
    return render(request, "pasteleria/eliminar_producto.html")

def eliminar(request):
    borrar = Cliente.objects.all(rut=request.POST["eliminar"])
    borrar.delete()
    return HttpResponse("Cliente eliminado")

def actualizar(request):
    actualizar = Cliente.objects.all()
    mostrar = {"actualizar": actualizar}
    return render(request, "pasteleria/actualizar.html", mostrar)

def editar(request):
    mostrar = Cliente.objects.get(rut= request.POST['rut'])
    nombre = request.POST['nombre']
    nombre = nombre.replace(' ','')
    apellido = request.POST['apellido'] 
    apellido = apellido.replace(' ','')
    fecha = request.POST['fecha']
    email= request.POST['correo']
    email = email.replace(' ','')
    dirrecion = request.POST['dirrecion']
    comuna = request.POST['comuna'] 

    mostrar.nombre = nombre
    mostrar.apellido = apellido
    mostrar.fecha = fecha
    mostrar.email = email
    mostrar.direccion = dirrecion
    mostrar.comuna = comuna

    mostrar.save()
    return render(request, 'pasteleria/editar.html',)

def borrar_pro(request):
    borrar_producto = Producto.objects.get(nombre_producto=request.POST["borrar_pro"])
    borrar_producto.delete()
    return HttpResponse("Producto eliminado")



    

