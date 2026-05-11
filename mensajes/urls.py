from django.urls import path

from .views import *

urlpatterns = [

    path('', inbox, name='inbox'),

    path('usuarios/', usuarios, name='usuarios'),

    path('enviar/<int:user_id>/',
         enviar_mensaje,
         name='enviar_mensaje'),
]