from email import message
from .cart import Carro
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import Registro, ProductoForm, DireccionForm, FormaPagoForm, UserRegisterForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategorioSerializer, UsuarioSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategorioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productos = productos.filter(nombre = nombre)
        
        return productos 


# from app.cart import Cart

def register(request):
        data = {
            'form': UserRegisterForm()
        }

        if request.method == 'POST':
            formulario = UserRegisterForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect(to="index")
            data["form"] = formulario
        return render(request, 'app/register.html', data)

# Create your views here.
def index(request):
    Productos = Producto.objects.all()
    data = {"Productos": Productos}
    return render(request, "app/index.html", data)


def quienessomos(request):
    return render(request, "app/quienessomos.html")


def admin(request):
    productos = Producto.objects.all()
    data = {"Productos": productos}
    return render(request, "app/admin.html", data)


def categoria(request):
    return render(request, "app/categoria.html")


def compra(request):
    return render(request, "app/compra.html")

@login_required(login_url='/login')
def pedidos(request):
    return render(request, "app/pedidos.html")


@login_required(login_url='/login')
def perfil(request):
    user = get_object_or_404(User, id=request.user.id)
    data = {"user": user}
    return render(request, "app/perfil.html", data)


def producto(request):
    return render(request, "app/producto.html")


def seguimiento(request):
    return render(request, "app/seguimiento.html")


def sesion(request):
    data = {"form": Registro(), "form2": FormaPagoForm()}
    return render(request, "app/sesion.html", data)


def vender(request):
    data = {"form": ProductoForm()}
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
            data["mensaje"] = "Producto guardado"
        else:
            data["form"] = formulario
    return render(request, "app/vender.html", data)


def modificarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {"form": ProductoForm(instance=producto)}
    if request.method == "POST":
        formulario = ProductoForm(
            data=request.POST, instance=producto, files=request.FILES
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="admin2")
        data["form"] = formulario
    return render(request, "app/modificar.html", data)

def verProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {"producto": producto}
    return render(request, "app/modificar.html", data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="admin2")


def carrito(request):
    data = {
        "carro": request.session["carro"]
    }
    return render(request, "app/carrito.html", data)


def agregar_carrito(request, id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=id)
    carro.agregar(producto=producto)
    return redirect(to="index")


def eliminar_carrito(request, id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=id)
    carro.eliminar(producto=producto)
    return redirect(to="carrito")


def restar_carrito(request, id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=id)
    carro.restar(producto=producto)
    return redirect(to="carrito")


def clean_carrito(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect(to="carrito")


def procesar_compra(request):
    messages.success(request, "Gracias por su Compra!!")
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("index")


def sumar_producto(request, producto_id):
    carrito = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.sumar(producto)
    return redirect("carro")


def totalPrice(request):
    carrito = Carro(request)
    return carrito.totalPrice()

