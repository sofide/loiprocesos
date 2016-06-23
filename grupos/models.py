from django.db import models

class Grupo(models.Model):
    año = models.IntegerField()
    numero = models.IntegerField()
    empresa = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {} - {}'.format(str(self.año), self.empresa, self.producto)


class Pertenencia(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')
