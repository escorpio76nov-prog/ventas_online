from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Mensaje

from .forms import MensajeFormulario


# INBOX

@login_required
def inbox(request):

    mensajes = Mensaje.objects.filter(
        destinatario=request.user
    ).order_by('-fecha')

    return render(request,
                  'mensajes/inbox.html',
                  {'mensajes': mensajes})


# ENVIAR MENSAJE

@login_required
def enviar_mensaje(request, user_id):

    destinatario = get_object_or_404(User, id=user_id)

    if request.method == 'POST':

        form = MensajeFormulario(request.POST)

        if form.is_valid():

            mensaje = form.save(commit=False)

            mensaje.remitente = request.user

            mensaje.destinatario = destinatario

            mensaje.save()

            return redirect('inbox')

    else:

        form = MensajeFormulario()

    return render(request,
                  'mensajes/enviar.html',
                  {
                      'form': form,
                      'destinatario': destinatario
                  })


# LISTA USUARIOS

@login_required
def usuarios(request):

    usuarios = User.objects.exclude(id=request.user.id)

    return render(request,
                  'mensajes/usuarios.html',
                  {'usuarios': usuarios})