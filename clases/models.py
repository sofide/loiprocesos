from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone


class Clase(models.Model):
    fecha = models.DateTimeField(default=timezone.now)


class Grupo(models.Model):
    año = models.IntegerField()
    numero = models.IntegerField()
    empresa = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)


class Integrante(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')


class TP(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()


class Exposicion(models.Model):
    clase = models.ForeignKey(Clase)
    grupo = models.ForeignKey(Grupo)
    tp = models.ForeignKey(TP)


class Pregunta(models.Model):
    exposici = models.ForeignKey(Exposicion)
    grupo = models.ForeignKey(Grupo)
    pregunta = models.TextField()
