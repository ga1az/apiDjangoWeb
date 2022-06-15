from django.urls import path
from .views import (
    index,
    quienessomos,
    admin,
    carrito,
    categoria,
    compra,
    pedidos,
    perfil,
    producto,
    seguimiento,
    sesion,
    vender,
    modificarProducto,
    eliminar_producto,
)

urlpatterns = [
    path("", index, name="index"),
    path("quienessomos/", quienessomos, name="quienessomos"),
    path("admin2/", admin, name="admin2"),
    path("carrito/", carrito, name="carrito"),
    path("categoria/", categoria, name="categoria"),
    path("compra/", compra, name="compra"),
    path("pedidos/", pedidos, name="pedidos"),
    path("perfil/", perfil, name="perfil"),
    path("producto/", producto, name="producto"),
    path("seguimiento/", seguimiento, name="seguimiento"),
    path("sesion/", sesion, name="sesion"),
    path("vender/", vender, name="vender"),
    path("modificar/<id>/", modificarProducto, name="modificar"),
    path("eliminar/<id>/", eliminar_producto, name="eliminar_producto"),
]
