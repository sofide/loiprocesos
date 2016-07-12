from django.db import models

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

    def __str__(self):
        return '{} - G{} - {} - {}'.format(str(self.año), self.numero, self.empresa, self.producto)


class Pertenencia(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')

    def __str__(self):
        return '{} en {}'.format(self.usuario, self.grupo)
