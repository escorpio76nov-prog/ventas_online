from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm, CategoriaForm, ProveedorForm, BusquedaProductoForm

def inicio(request):
    return render(request, "productos/base.html")


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "productos/base.html")
    else:
        form = ProductoForm()

    return render(request, "productos/crear_producto.html", {"form": form})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "productos/base.html")
    else:
        form = CategoriaForm()

    return render(request, "productos/crear_categoria.html", {"form": form})


def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "productos/base.html")
    else:
        form = ProveedorForm()

    return render(request, "productos/crear_proveedor.html", {"form": form})


def buscar_producto(request):
    form = BusquedaProductoForm()
    return render(request, "productos/buscar_producto.html", {"form": form})


def resultados(request):
    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "productos/resultados.html", {"productos": productos})

    return render(request, "productos/base.html")