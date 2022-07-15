from django.urls import path
from rest_producto.viewsTienda import home, tienda
from django.urls import path
from rest_producto.views import lista_productos, detalle_producto
from rest_producto.viewsLogin import login
from rest_producto.views import detalle_venta, lista_categorias, lista_compras, lista_productos, detalle_producto, lista_ventas#, login

urlpatterns =[
    path('', home, name="Home"),
    path('tienda', tienda, name="Tienda"),
    path('tienda/<int:page>', tienda, name="Tienda"),
    path('api/lista_categorias', lista_categorias, name="lista_categorias"),
    path('api/lista_producto', lista_productos, name="lista_productos"),
    path('api/detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name="login"),
    path('api/lista_ventas/:id_usuario', lista_ventas, name=""),
    path('api/lista_compras/:id_cliente', lista_compras, name=""),
    path('api/detalle_venta/:id/<id>', detalle_venta, name=""),
    #path('login', login, name="login")
]