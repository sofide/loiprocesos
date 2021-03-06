# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 01:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0006_auto_20160805_2305'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teoria', '0008_auto_20160815_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voto',
            name='votante',
        ),
        migrations.AddField(
            model_name='voto',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
        ),
        migrations.AddField(
            model_name='voto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voto',
            name='voto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voto',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teoria.Material'),
        ),
        migrations.AlterField(
            model_name='voto',
            name='pregunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teoria.Pregunta'),
        ),
    ]
