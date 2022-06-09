from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def home(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'home.html', datos)