# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0007_contadorpreguntas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='mejor',
            field=models.BooleanField(default=False),
        ),
    ]
