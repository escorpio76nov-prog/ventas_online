from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaFormulario

from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.decorators import login_required

from .forms import OpinionFormulario

from .models import Carrito

from .forms import CategoriaFormulario

from django.contrib import messages

import mercadopago

from django.conf import settings

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
        'categoria',
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
        'categoria',
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

@login_required
def agregar_carrito(request, producto_id):

    producto = Producto.objects.get(id=producto_id)

    item, created = Carrito.objects.get_or_create(
        usuario=request.user,
        producto=producto
    )

    if not created:

        item.cantidad += 1

        item.save()

    return redirect('carrito')

@login_required
def carrito(request):

    items = Carrito.objects.filter(
        usuario=request.user
    )

    total = 0

    for item in items:

        total += item.subtotal()

    return render(
        request,
        'productos/carrito.html',
        {
            'items': items,
            'total': total
        }
    )


@login_required
def eliminar_carrito(request, item_id):

    item = Carrito.objects.get(id=item_id)

    item.delete()

    return redirect('carrito')

@login_required
def pagar(request):

    sdk = mercadopago.SDK(
        settings.MERCADO_PAGO_ACCESS_TOKEN
    )

    items_carrito = Carrito.objects.filter(
        usuario=request.user
    )

    items = []

    for item in items_carrito:

        items.append({
            "title": item.producto.nombre,
            "quantity": item.cantidad,
            "unit_price": float(item.producto.precio),
        })

    preference_data = {

        "items": items,
        "back_urls": {
            "success": "https://stinger-cymbal-unmade.ngrok-free.dev/pago_exitoso/",
            "failure": "https://stinger-cymbal-unmade.ngrok-free.dev/carrito/",
            "pending": "https://stinger-cymbal-unmade.ngrok-free.dev/carrito/"
        },

        "auto_return": "approved",

    }

    preference_response = sdk.preference().create(
    preference_data
    )

    print(preference_response)

    preference = preference_response.get("response", {})

    return render(
        request,
        'productos/pagar.html',
        {
            'preference': preference
        }
    )

def pago_exitoso(request):
    return render(request, 'productos/pago_exitoso.html')

@login_required
def crear_categoria(request):

    if not request.user.is_superuser:

        return redirect('home')

    if request.method == 'POST':

        form = CategoriaFormulario(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
            request,
            'Categoría creada correctamente'
             )

            return redirect('crear_categoria')

    else:

        form = CategoriaFormulario()

    return render(
        request,
        'productos/crear_categoria.html',
        {
            'form': form
        }
    )