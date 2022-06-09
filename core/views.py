from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home.html', datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_producto.html', datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(patente=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(patente=id)
    producto.delete()
    return redirect(to="home")