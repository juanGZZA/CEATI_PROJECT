from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username
    

class Noticias(models.Model):
    encabezado = models.CharField(max_length=264, unique=True)
    texto = models.CharField(max_length=8192, unique=True)

    def __str__(self):
        return self.encabezado


class Dependencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=264, unique=True)
    Dependicia = models.ForeignKey(Dependencia, on_delete=models.PROTECT)
    informacion = models.CharField(max_length=4000, unique=True)


