from django.db import models

from django.contrib.auth.models import User


class Mensaje(models.Model):

    remitente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='envia'
    )

    destinatario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recibe'
    )

    contenido = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{self.remitente} -> {self.destinatario}'
