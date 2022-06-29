from django.urls import path
from rest_producto.views import lista_productos, detalle_producto, login

urlpatterns = [
    path('lista_producto', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name="login")
]