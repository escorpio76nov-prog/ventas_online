from django.contrib import admin

from .models import Producto, Opinion, Carrito

admin.site.register(Producto)

admin.site.register(Opinion)

admin.site.register(Carrito)