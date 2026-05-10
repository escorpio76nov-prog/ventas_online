from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

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

    marca = models.CharField(max_length=100)

    descripcion = RichTextField()

    imagen = models.ImageField(upload_to='productos')

    fecha = models.DateField(auto_now_add=True)

    precio = models.FloatField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre