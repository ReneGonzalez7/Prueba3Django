from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock']

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            #'comentarios'
        )