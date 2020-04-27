from django.db import models
from django.utils import timezone

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
    usuario = models.ForeignKey('auth.User', default=None, null=True,
                                blank=True, )
    grupo_autor = models.ForeignKey(Grupo, blank=True, null=True, related_name='preguntas_teoria')
    orden = models.IntegerField()

    class Meta:
        ordering = ['-vigente', 'orden', 'autor', 'pregunta']
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
    usuario = models.ForeignKey('auth.User', default=None, null=True,
                                blank=True,)
    grupo_autor = models.ForeignKey(Grupo, blank=True, null=True, related_name='material_teoria')
    orden = models.IntegerField()

    class Meta:
        ordering = ['-vigente', 'orden', 'autor', 'nombre']
        index_together = ['autor', 'nombre']
    def __str__(self):
        return "{} - {}".format(self.nombre, self.autor)


class Voto(models.Model):
    grupo = models.ForeignKey(Grupo, null=True, blank=True)
    usuario = models.ForeignKey('auth.User')
    pregunta = models.ForeignKey(Pregunta, null=True, blank=True)
    material = models.ForeignKey(Material, null=True, blank=True)
    voto = models.IntegerField()
    fecha = models.DateField(default=timezone.now)
