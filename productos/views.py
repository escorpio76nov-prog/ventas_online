from django.shortcuts import render

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Producto


# HOME

def home(request):

    return render(request, 'productos/home.html')


# ABOUT

def about(request):

    return render(request, 'productos/about.html')


# LISTAR PRODUCTOS

class ProductoListView(ListView):

    model = Producto

    template_name = 'productos/pages.html'


# DETALLE

class ProductoDetailView(DetailView):

    model = Producto

    template_name = 'productos/detalle.html'


# CREAR

class ProductoCreateView(LoginRequiredMixin, CreateView):

    model = Producto

    fields = [
        'nombre',
        'marca',
        'descripcion',
        'imagen',
        'precio',
    ]

    template_name = 'productos/crear.html'

    success_url = reverse_lazy('pages')

    def form_valid(self, form):

        form.instance.autor = self.request.user

        return super().form_valid(form)


# EDITAR

class ProductoUpdateView(LoginRequiredMixin, UpdateView):

    model = Producto

    fields = [
        'nombre',
        'marca',
        'descripcion',
        'imagen',
        'precio',
    ]

    template_name = 'productos/editar.html'

    success_url = reverse_lazy('pages')


# BORRAR

class ProductoDeleteView(LoginRequiredMixin, DeleteView):

    model = Producto

    template_name = 'productos/borrar.html'

    success_url = reverse_lazy('pages')