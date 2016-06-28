from django.db import models
from django.utils import timezone


class Clase(models.Model):
    fecha = models.DateField(default=timezone.now)
    def __str__(self):
        return str(self.fecha)


class TP(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Exposicion(models.Model):
    clase = models.ForeignKey(Clase)
    grupo = models.ForeignKey('grupos.Grupo', null=True)
    tp = models.ForeignKey(TP)
    start_expo = models.DateTimeField(null=True, default=None)
    start_ques = models.DateTimeField(null=True, default=None)
    finish_expo = models.DateTimeField(null=True, default=None)


    class Meta:
        verbose_name_plural = "Exposiciones"

    def __str__(self):
        return '{} - G{} - TP {}'.format(str(self.clase), self.grupo.numero, self.tp)


class Pregunta(models.Model):
    exposicion = models.ForeignKey(Exposicion)
    grupo = models.ForeignKey('grupos.Grupo', null=True)
    pregunta = models.TextField()
    mejor = models.BooleanField(default=False)


class ContadorPreguntas(models.Model):
    exposicion = models.ForeignKey(Exposicion)
    preguntador = models.ForeignKey('grupos.Grupo')
    cantidad = models.IntegerField()
    primero = models.BooleanField(default=False)
    ultimo = models.BooleanField(default=False)
