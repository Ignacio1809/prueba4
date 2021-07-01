from django.urls import path
from . import views

app_name = "pasteleria"
urlpatterns = [
    path("", views.index, name="inicio"),
    path("agregar", views.agregar_clientes, name="agregar"),
    path("registrar", views.registrar_clientes, name="registrar"),
    path("buscar", views.buscar_clientes, name="buscar"),
    path("mostrar", views.mostrar_clientes, name="mostrar"),
    path("eliminar", views.eliminar_clientes, name="eliminar"),
    path("borrar", views.eliminar, name="borrar"),
]