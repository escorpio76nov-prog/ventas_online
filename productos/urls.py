from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.crear_producto, name='crear_producto'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('resultados/', views.resultados, name='resultados'),
]