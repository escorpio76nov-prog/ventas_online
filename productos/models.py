from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.pais}"


class Producto(models.Model):

    categoria = models.ForeignKey(
    Categoria,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    ) 

    nombre = models.CharField(max_length=100)

    marca = models.CharField(max_length=100)

    descripcion = RichTextField(default='Descripción por defecto')

    imagen = models.ImageField(upload_to='productos', default='default.png', blank=True)

    fecha = models.DateField(default=timezone.now)

    precio = models.FloatField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.nombre
    

class Opinion(models.Model):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='opiniones'
        )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    comentario = models.TextField()

    puntuacion = models.IntegerField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{self.usuario} - {self.producto}'
    

class Carrito(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.IntegerField(default=1)

    creado = models.DateTimeField(auto_now_add=True)

    def subtotal(self):

        return self.producto.precio * self.cantidad

    def __str__(self):

        return f'{self.usuario} - {self.producto}'
    
