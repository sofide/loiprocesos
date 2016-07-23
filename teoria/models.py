from django.db import models

from grupos.models import Grupo


class Unidad(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, default=None)

    def __str__(self):
        return 'U{} - {}'.format(self.numero, self.titulo)


class Pregunta(models.Model):
    unidad = models.ForeignKey(Unidad)
    pregunta = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, verbose_name="Sugerido por")
    vigente = models.BooleanField(default=True)


class Material(models.Model):
    unidad = models.ForeignKey(Unidad)
    nombre = models.CharField(max_length=200)
    link = models.URLField()
    autor = models.CharField(max_length=200, null=True, verbose_name="Sugerido por")
    vigente = models.BooleanField(default=True)


class Voto(models.Model):
    votante = models.ForeignKey(Grupo)
    pregunta = models.ForeignKey(Pregunta, null=True)
    material = models.ForeignKey(Material, null=True)
