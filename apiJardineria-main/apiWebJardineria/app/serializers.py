from asyncore import read
from .models import Producto, Categoria
from rest_framework import serializers
from django.contrib.auth.models import User

class CategorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source='categoria.nombre')
    categoria = CategorioSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')
    nombre = serializers.CharField(required=True, min_length=3, max_length=50)
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'