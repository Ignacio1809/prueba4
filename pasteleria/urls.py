from os import name
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
    path("actualizar", views.actualizar, name="actualizar"),
    path("editar", views.editar, name="editar"),
    path("agregar_producto", views.agregar_producto, name="agregar_producto"),
    path("registrar_producto", views.registrar_producto, name="registrar_producto"),
    path("buscar_producto", views.buscar_producto, name="buscar_producto"),
    path("mostrar_producto", views.mostrar_producto, name="mostrar_producto"),
    path("eliminar_producto", views.eliminar_producto, name="eliminar_producto"),
    path("borrar_producto", views.borrar_pro, name="borrar_producto"),
    path("actualizar_producto", views.actualizar_producto, name="actualizar_producto"),
    path("editar_producto", views.editar_producto, name="editar_producto"),
    path("frm_iniciar_sesion", views.frm_iniciar_sesion, name="frm_iniciar_sesion"),
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("producto_uno", views.producto_uno, name="producto_uno"),
    path("producto_dos", views.producto_dos, name="producto_dos"),
    path("producto_tres", views.producto_tres, name="producto_tres"),
    path("finalizar_pedido_uno", views.finalizar_pedido_uno, name="finalizar_pedido_uno"),
    path("finalizar_pedido_dos", views.finalizar_pedido_dos, name="finalizar_pedido_dos"),
    path("finalizar_pedido_tres", views.finalizar_pedido_tres, name="finalizar_pedido_tres"),
]