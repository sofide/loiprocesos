from django.db import models
from django.utils import timezone


class Clase(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.fecha.strftime('%d-%m-%Y')


class Grupo(models.Model):
    año = models.IntegerField()
    numero = models.IntegerField()
    empresa = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {} - {}'.format(str(self.año), self.empresa, self.producto)


class Integrante(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')


class TP(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return nombre


class Exposicion(models.Model):
    clase = models.ForeignKey(Clase)
    grupo = models.ForeignKey('grupos.Grupo', null=True)
    tp = models.ForeignKey(TP)

    class Meta:
        verbose_name_plural = "Exposiciones"


class Pregunta(models.Model):
    exposicion = models.ForeignKey(Exposicion)
    grupo = models.ForeignKey('grupos.Grupo', null=True)
    pregunta = models.TextField()


class ContadorPreguntas(models.Model):
    clase = models.ForeignKey(Clase)
    exposicion = models.ForeignKey(Exposicion)
    preguntador = models.ForeignKey(Grupo)
    cantidad = models.IntegerField()
    primero = models.BooleanField(default=False)
    ultimo = models.BooleanField(default=False)
