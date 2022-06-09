from django.urls import path
from rest_producto.views import home

urlpatterns =[
    path('', home, name="Tienda"),
]