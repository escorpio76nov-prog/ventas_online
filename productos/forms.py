from django import forms
from .models import Producto
from .models import Opinion

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

class BusquedaFormulario(forms.Form):

    nombre = forms.CharField(
        max_length=100,
        required=False
    )

class OpinionFormulario(forms.ModelForm):

    puntuacion = forms.IntegerField(
    min_value=1,
    max_value=5
    )

    class Meta:

        model = Opinion

        fields = [
            'comentario',
            'puntuacion'
        ]

