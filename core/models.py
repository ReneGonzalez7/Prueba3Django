from django.db import models

# Create your models here.
# Modelo para la categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

# modelo para el producto
class Producto(models.Model):
    sku = models.CharField(max_length=15, primary_key=True, verbose_name='SKU')
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
