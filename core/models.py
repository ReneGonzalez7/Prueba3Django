from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    isCliente = models.BooleanField(blank= True) #booleano que nos indica si es un cliente
    comentarios = models.CharField(max_length=255, blank=True)

    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()


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
    categoria = models.ForeignKey(Categoria,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku


# modelo para el descuent9
class Descuento (models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.id

# modelo para el despacho
class Despacho (models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.id

# modelo para la venta
class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.IntegerField()
    descuento = models.ForeignKey(Descuento,null=True, on_delete=models.CASCADE)
    despacho = models.ForeignKey(Despacho,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

# modelo para la venta
class DetalleVenta(models.Model):
    id = models.IntegerField(primary_key=True)
    producto = models.ForeignKey(Producto,null=True, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
