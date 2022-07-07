from django import forms
from .models import RegistroPersona, Producto, FormaDePago, Direccion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']
        help_texts = {k:"" for k in fields}


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
