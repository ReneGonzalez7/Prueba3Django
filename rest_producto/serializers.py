from rest_framework import serializers
from core.models import Descuento, Despacho, DetalleVenta, Producto, Venta


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock', 'categoria']

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['id', 'monto']

class DespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despacho
        fields = ['id', 'fecha']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id', 'total', 'descuento', 'despacho']

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id', 'cantidad', 'producto', 'venta']