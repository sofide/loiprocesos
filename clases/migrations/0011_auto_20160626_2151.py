# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0010_auto_20160626_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contadorpreguntas',
            name='preguntador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
        ),
    ]