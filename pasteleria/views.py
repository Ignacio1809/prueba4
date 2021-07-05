from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from pasteleria.models import Cliente, Producto
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    if request.user.has_perm('pasteleria.Admin') or ('pasteleria.view_cliente'):
        listado_clientes = Cliente.objects.all()
        context = {"listado_clientes": listado_clientes}
        return render(request, "pasteleria/inicio.html", context)
    else:
        return ('No cuentas con los permisos')

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

def actualizar_producto(request):
    actualizar = Producto.objects.all()
    mostrar = {"actualizar": actualizar}
    return render(request, "pasteleria/actualizar_producto.html", mostrar)

def editar_producto(request):
    mostrar = Producto.objects.get(nombre_producto= request.POST['nombre_producto'])
    nombre_producto = request.POST['nombre_producto']
    nombre_producto = nombre_producto.replace(' ','')
    precio = request.POST['precio'] 
    precio = precio.replace(' ','')
    descripcion = request.POST['descripcion'] 
    descripcion = descripcion.replace(' ','')

    mostrar.nombre_producto = nombre_producto
    mostrar.precio = precio
    mostrar.descripcion = descripcion

    mostrar.save()
    carrito = {"mostrar": mostrar}
    return render (request, "pasteleria/editar_producto.html", carrito)

def frm_iniciar_sesion(request):
    return render(request, 'pasteleria/frm_iniciar_sesion.html')

def iniciar_sesion(request):
    usuario = request.POST["usuario"]
    clave = request.POST["clave"]

    user = authenticate(request, username = usuario, password = clave)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pasteleria:inicio'))
    else:
        return HttpResponse ("No se pudo autenticar las credenciales")

def producto_uno(request):
    return render(request, "pasteleria/producto_uno.html")

def producto_dos(request):
    return render(request, "pasteleria/producto_dos.html")


def producto_tres(request):
    return render(request, "pasteleria/producto_tres.html")

def finalizar_pedido_uno(request):
    return render(request, "pasteleria/finalizar_pedido_uno.html")

def finalizar_pedido_dos(request):
    return render(request, "pasteleria/finalizar_pedido_dos.html")

def finalizar_pedido_tres(request):
    return render(request, "pasteleria/finalizar_pedido_tres.html")