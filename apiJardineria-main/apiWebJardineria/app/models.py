from cProfile import run
from django.db import models

# Create your models here.
# Modelo categoria de producto
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class RegistroPersona(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=51)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to="productos/", null=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.usuario.nombre


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.pedido.usuario.nombre


class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return self.usuario.nombre


class FormaDePago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)
    mes = models.CharField(max_length=2)
    anio = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.usuario.nombre
