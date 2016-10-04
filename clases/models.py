from django.db import models
from django.utils import timezone
from django.conf import settings


class Clase(models.Model):
    fecha = models.DateField(default=timezone.now, unique=True, db_index=True)

    def __str__(self):
        return str(self.fecha.strftime(settings.DATE_INPUT_FORMATS[0]))

    class Meta:
        ordering = ['-fecha']


class TP(models.Model):
    numero = models.IntegerField(null=True, blank=True, default=None, db_index=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        if self.numero:
            return "TP {} - {}".format(self.numero, self.nombre)
        else:
            return self.nombre

    class Meta:
        ordering = ['numero', ]


class Exposicion(models.Model):
    clase = models.ForeignKey(Clase, related_name='exposiciones', db_index=True,
                              null=True, default=None)
    grupo = models.ForeignKey('grupos.Grupo', null=True, db_index=True)
    tp = models.ForeignKey(TP)
    start_expo = models.DateTimeField(null=True, default=None)
    start_ques = models.DateTimeField(null=True, default=None)
    finish_expo = models.DateTimeField(null=True, default=None)
    virtual = models.BooleanField(default=False)
    video = models.CharField(max_length=200, null=True, default=None, blank=True)
    description = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Exposiciones"
        ordering = ['clase', 'grupo', 'tp']
        index_together = ['clase', 'grupo', 'tp']

    def __str__(self):
        if self.virtual:
            clase = "{}/{}/{} VIRTUAL".format(self.start_expo.day,self.start_expo.month, self.start_expo.year)
        else:
            clase = str(self.clase)

        return 'G{} - TP {} - {}'.format(self.grupo.numero, self.tp, clase)

    def short_string(self):
        if self.virtual:
            return str(self)
        else:
            return '{}/{} - G{} - TP {}'.format(self.clase.fecha.day,
                                                self.clase.fecha.month,
                                                self.grupo.numero,
                                                self.tp.numero)


class Pregunta(models.Model):
    exposicion = models.ForeignKey(Exposicion, related_name='preguntas')
    grupo = models.ForeignKey('grupos.Grupo', null=True, blank=True)
    usuario = models.ForeignKey('auth.User', null=True, blank=True, related_name='preg_clases')
    pregunta = models.TextField()
    mejor = models.BooleanField(default=False)

    def __str__(self):
        return self.pregunta

    class Meta:
        ordering = ['exposicion', 'grupo']
        index_together = ['exposicion', 'grupo']


class ContadorPreguntas(models.Model):
    exposicion = models.ForeignKey(Exposicion)
    preguntador = models.ForeignKey('grupos.Grupo',
                                    verbose_name="Grupo que pregunta")
    cantidad = models.IntegerField()
    primero = models.BooleanField(default=False)
    ultimo = models.BooleanField(default=False)
