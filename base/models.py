from django.db import models
from django.utils import timezone


class Text(models.Model):
    text = models.TextField()
    reference = models.CharField(max_length=200, db_index=True)
    edited = models.DateField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['edited']
