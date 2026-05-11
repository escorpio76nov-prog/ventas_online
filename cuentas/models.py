from django.db import models

from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares')

    bio = models.TextField(blank=True)

    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):

        return self.user.username