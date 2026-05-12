from django.urls import path

from .views import *

from django.contrib.auth.views import LogoutView

from django.contrib.auth.views import PasswordChangeView

from django.urls import reverse_lazy

urlpatterns = [

    path('signup/', registro, name='signup'),

    path('login/', login_request, name='login'),

    path('logout/', LogoutView.as_view(
        template_name='cuentas/logout.html'
    ), name='logout'),

    path('profile/', profile, name='profile'),

    path('editar-perfil/', editar_perfil, name='editar_perfil'),

    path(
    'password/',
    PasswordChangeView.as_view(
        template_name='cuentas/password.html',
        success_url=reverse_lazy('profile')
    ),
    name='password'
    ),

]