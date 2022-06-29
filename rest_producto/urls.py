from django.urls import path
from rest_producto.viewsTienda import home, tienda
from django.urls import path
from rest_producto.views import lista_productos, detalle_producto#, login

urlpatterns =[
    path('', home, name="Home"),
    path('tienda', tienda, name="Tienda"),
    path('tienda/<int:page>', tienda, name="Tienda"),
    path('api/lista_producto', lista_productos, name="lista_productos"),
    path('api/detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    #path('login', login, name="login")
]