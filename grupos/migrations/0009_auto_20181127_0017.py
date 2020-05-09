# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-27 03:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0008_evaluacion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='puntuacion',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10, 'El voto no puede ser superior a 10'), django.core.validators.MinValueValidator(1, 'El voto no puede ser menor a 1')]),
        ),
    ]