from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name


class Photo(models.Model):
    url = models.CharField(max_length=250)
    section = models.ForeignKey(Section, related_name='photos')

    def __str__(self):
        return self.url
