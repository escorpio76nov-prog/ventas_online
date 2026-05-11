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

    nombre = models.CharField(max_length=100)

    marca = models.CharField(max_length=100, default=25)

    descripcion = RichTextField(default='Descripción por defecto')

    imagen = models.ImageField(upload_to='productos', default='media/default.png', blank=True)

    fecha = models.DateField(default=timezone.now)

    precio = models.FloatField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre