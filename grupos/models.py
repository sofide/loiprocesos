from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Grupo(models.Model):
    año = models.IntegerField()
    numero = models.IntegerField()
    empresa = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True, default=None)
    id_carpeta_drive = models.CharField(max_length=200, null=True, blank=True,  default=None)
    integrantes = models.ManyToManyField(
        'auth.User',
        through='Pertenencia',
        through_fields=('grupo', 'usuario'),
        related_name='grupos'
    )

    class Meta:
        ordering = ['-año', 'numero']
        index_together = ['año', 'numero']

    def __str__(self):
        return '{} - G{} - {} - {}'.format(str(self.año), self.numero, self.producto, self.empresa)


class Pertenencia(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')

    def __str__(self):
        return '{} en {}'.format(self.usuario, self.grupo)


class Autoevaluacion_grupal(models.Model):
    fecha = models.DateField(default=timezone.now, unique=True, db_index=True)
    año = models.IntegerField()

    def __str__(self):
        return str("Autoevaluación del año {} - {}".format(self.año, self.fecha.strftime(settings.DATE_INPUT_FORMATS[0])))

    class Meta:
        ordering = ['-fecha']


class Criterio_evaluacion(models.Model):
    autoevaluacion = models.ForeignKey(Autoevaluacion_grupal)
    criterio = models.CharField(max_length=200)
    class Meta:
        ordering = ['criterio']
    def __str__(self):
        return str(self.criterio)


class Evaluacion(models.Model):
    fecha = models.DateField(default=timezone.now)
    criterio = models.ForeignKey(Criterio_evaluacion)
    evaluador = models.ForeignKey(Grupo, related_name="evaluador")
    grupo_evaluado = models.ForeignKey(Grupo, related_name="grupo_evaluado")
    puntuacion = models.IntegerField(validators=[MaxValueValidator(5, "El voto no puede ser superior a 5"),
                                                 MinValueValidator(1, "El voto no puede ser menor a 1")])

