# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0009_remove_contadorpreguntas_clase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]