from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaFormulario

from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.decorators import login_required

from .forms import OpinionFormulario

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

class ProductoCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    
    def test_func(self):

        return self.request.user.is_superuser

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

class ProductoUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    def test_func(self):

        return self.request.user.is_superuser

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

class ProductoDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    
    def test_func(self):

        return self.request.user.is_superuser

    model = Producto

    template_name = 'productos/borrar.html'

    success_url = reverse_lazy('pages')

def buscar_producto(request):

    formulario = BusquedaFormulario()

    productos = []

    if request.GET.get('nombre'):

        nombre = request.GET['nombre']

        productos = Producto.objects.filter(
            nombre__icontains=nombre
        )

    return render(
        request,
        'productos/busqueda.html',
        {
            'formulario': formulario,
            'productos': productos
        }
    )

@login_required
def crear_opinion(request, producto_id):

    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':

        form = OpinionFormulario(request.POST)

        if form.is_valid():

            opinion = form.save(commit=False)

            opinion.usuario = request.user

            opinion.producto = producto

            opinion.save()

            return redirect('detalle', pk=producto.id)

    else:

        form = OpinionFormulario()

    return render(
        request,
        'productos/opinion.html',
        {
            'form': form,
            'producto': producto
        }
    )

