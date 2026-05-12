from .models import Carrito

def carrito_total(request):

    cantidad = 0

    if request.user.is_authenticated:

        items = Carrito.objects.filter(
            usuario=request.user
        )

        for item in items:

            cantidad += item.cantidad

    return {
        'cantidad_carrito': cantidad
    }