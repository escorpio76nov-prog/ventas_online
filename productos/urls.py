from django.urls import path

from .views import *

urlpatterns = [

    path('', home, name='home'),

    path('about/', about, name='about'),

    path('pages/', ProductoListView.as_view(), name='pages'),

    path('pages/<int:pk>/', ProductoDetailView.as_view(), name='detalle'),

    path('crear/', ProductoCreateView.as_view(), name='crear'),

    path('pages/update/<int:pk>/', ProductoUpdateView.as_view(), name='editar'),

    path('pages/delete/<int:pk>/', ProductoDeleteView.as_view(), name='borrar'),

    path('buscar/', buscar_producto, name='buscar'),

    path(
    'opinion/<int:producto_id>/',
    crear_opinion,
    name='opinion'
    ),

    path(
    'carrito/',
    carrito,
    name='carrito'
    ),

    path(
    'agregar-carrito/<int:producto_id>/',
    agregar_carrito,
    name='agregar_carrito'
    ),

    path(
    'eliminar-carrito/<int:item_id>/',
    eliminar_carrito,
    name='eliminar_carrito'
    ),

    path(
    'pagar/',
    pagar,
    name='pagar'
    ),

    path('pago-exitoso/', pago_exitoso, name='pago_exitoso'),

    path(
    'crear-categoria/',
    crear_categoria,
    name='crear_categoria'
    ),

]

