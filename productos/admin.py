from django.contrib import admin

from .models import Producto, Opinion, Carrito, Categoria

admin.site.register(Producto)

admin.site.register(Opinion)

admin.site.register(Carrito)

admin.site.register(Categoria)