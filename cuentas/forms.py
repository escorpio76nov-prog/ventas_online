from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Avatar


# REGISTRO

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


# LOGIN

class LoginFormulario(forms.Form):

    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)


# EDITAR PERFIL

class UserEditForm(forms.ModelForm):

    email = forms.EmailField()

    first_name = forms.CharField(required=False)

    last_name = forms.CharField(required=False)

    class Meta:

        model = User

        fields = [
            'email',
            'first_name',
            'last_name',
        ]


# AVATAR

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar

        fields = [
            'imagen',
            'bio',
            'fecha_nacimiento',
        ]