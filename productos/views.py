from django.shortcuts import render

# Create your views here.
def index(request): 
    contexto = {'mensaje': 'Bienvenidos al catalogo de productos'} 
    return render(request, 'productos/index.html', contexto)