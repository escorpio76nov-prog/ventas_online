from django.urls import path

from .views import *

urlpatterns = [

    path('', home, name='home'),

    path('about/', about, name='about'),

    path('pages/', ProductoListView.as_view(), name='pages'),

    path('pages/<int:pk>/', ProductoDetailView.as_view(), name='detalle'),

    path('pages/create/', ProductoCreateView.as_view(), name='crear'),

    path('pages/update/<int:pk>/', ProductoUpdateView.as_view(), name='editar'),

    path('pages/delete/<int:pk>/', ProductoDeleteView.as_view(), name='borrar'),

]