from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

from django.contrib.auth import login

from django.views.generic import CreateView

from .models import Perfil

from .forms import UsuarioForm


class SignUpView(CreateView):
    model = Perfil
    form_class = UsuarioForm

    def form_valid(self, form):
        form.save()
        return redirect('/')


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home.html', datos)

def create(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/create.html', datos)

def update(request, id):
    producto = Producto.objects.get(sku=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/update.html', datos)

def delete(request, id):
    producto = Producto.objects.get(sku=id)
    producto.delete()
    return redirect(to="home")