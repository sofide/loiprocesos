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
    fecha = models.DateField()
    vigente = models.BooleanField(default=True)
    usuario = models.ForeignKey('auth.User', default=None, null=True)
    class Meta:
        ordering = ['autor', 'pregunta']
        index_together = ['autor', 'pregunta']
    def __str__(self):
        return "{} - {}".format(self.pregunta, self.autor)


class Material(models.Model):
    unidad = models.ForeignKey(Unidad)
    nombre = models.CharField(max_length=200)
    link = models.URLField()
    autor = models.CharField(max_length=200, null=True, verbose_name="Sugerido por")
    fecha = models.DateField()
    vigente = models.BooleanField(default=True)
    usuario = models.ForeignKey('auth.User', default=None, null=True, blank=True)
    class Meta:
        ordering = ['autor', 'nombre']
        index_together = ['autor', 'nombre']
    def __str__(self):
        return "{} - {}".format(self.nombre, self.autor)


class Voto(models.Model):
    votante = models.ForeignKey(Grupo)
    pregunta = models.ForeignKey(Pregunta, null=True)
    material = models.ForeignKey(Material, null=True)
