from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from .forms import *

from .models import Avatar


# REGISTRO

def registro(request):

    if request.method == 'POST':

        form = RegistroFormulario(request.POST)

        if form.is_valid():

            usuario = form.save()

            Avatar.objects.create(user=usuario)

            return redirect('login')

    else:

        form = RegistroFormulario()

    return render(request,
                  'cuentas/signup.html',
                  {'form': form})


# LOGIN

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(
                username=usuario,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('home')

    else:

        form = AuthenticationForm()

    return render(request,
                  'cuentas/login.html',
                  {'form': form})


# PERFIL

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-success') 
    else:
        form = AvatarFormulario()

        avatar = Avatar.objects.filter(user=request.user).first()
 

    return render(request,
                  'cuentas/profile.html',
                  {'avatar': avatar})


# EDITAR PERFIL

@login_required
def editar_perfil(request):

    usuario = request.user

    avatar = Avatar.objects.get(user=usuario)

    if request.method == 'POST':

        miFormulario = UserEditForm(
            request.POST,
            instance=usuario
        )

        avatarForm = AvatarFormulario(
            request.POST,
            request.FILES,
            instance=avatar
        )

        if miFormulario.is_valid() and avatarForm.is_valid():

            miFormulario.save()

            avatarForm.save()

            return redirect('profile')

    else:

        miFormulario = UserEditForm(instance=usuario)

        avatarForm = AvatarFormulario(instance=avatar)

    return render(request,
                  'cuentas/editar_perfil.html',
                  {
                      'miFormulario': miFormulario,
                      'avatarForm': avatarForm
                  })