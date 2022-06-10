from django.urls import path
from rest_producto.views import home, tienda

urlpatterns =[
    path('', home, name="Home"),
    path('tienda', tienda, name="Tienda"),
    path('tienda/<int:page>', tienda, name="Tienda"),
]