from django import forms
from .models import Producto

class ProductoFormulario(forms.ModelForm):

    class Meta:

        model = Producto

        fields = [
            'nombre',
            'marca',
            'descripcion',
            'imagen',
            'precio',
        ]