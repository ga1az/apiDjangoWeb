from django import forms
from .models import RegistroPersona, Producto, FormaDePago, Direccion


class Registro(forms.ModelForm):
    class Meta:
        model = RegistroPersona
        # fields = ["nombre", "correo", "password", "date_nacimiento"]
        fields = "__all__"


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"


class FormaPagoForm(forms.ModelForm):
    class Meta:
        model = FormaDePago
        fields = "__all__"


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = "__all__"
