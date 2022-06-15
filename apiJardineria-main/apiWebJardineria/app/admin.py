from django.contrib import admin
from .models import Categoria, Producto, Usuario, Pedido, DetallePedido, RegistroPersona


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio", "categoria"]
    list_editable = ["precio"]
    search_fields = ["nombre", "precio"]
    list_filter = ["categoria"]


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(RegistroPersona)
