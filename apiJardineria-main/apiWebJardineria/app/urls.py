from django.urls import path, include
from .views import (
    agregar_carrito,
    clean_carrito,
    eliminar_carrito,
    index,
    procesar_compra,
    quienessomos,
    admin,
    carrito,
    categoria,
    compra,
    pedidos,
    perfil,
    producto,
    restar_carrito,
    seguimiento,
    sesion,
    sumar_producto,
    vender,
    modificarProducto,
    eliminar_producto,
    ProductoViewset,
    CategoriaViewSet,
    register,
    totalPrice,
    UsuarioViewSet
)
from rest_framework import routers
from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.register("producto", ProductoViewset)
router.register("categoria", CategoriaViewSet)
router.register("usuario", UsuarioViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("quienessomos/", quienessomos, name="quienessomos"),
    path("admin2/", admin, name="admin2"),
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
    path("carrito/", carrito, name="carrito"),
    path("addcart/<id>/", agregar_carrito, name="addcart"),
    path("delcart/<id>/", eliminar_carrito, name="delcart"),
    path("restcart/<id>/", restar_carrito, name="restcart"),
    path("cleancart/", clean_carrito, name="cleancart"),
    path("procesar_compra/", procesar_compra, name="procesar_compra"),
    path("sumar/<id>/", sumar_producto, name="sumar"),
    path("api/", include(router.urls)),
    path("total/", totalPrice, name="total"),
    
    path("login/", LoginView.as_view(template_name="app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="app/logout.html"), name="logout"),
]
