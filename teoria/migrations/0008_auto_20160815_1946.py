# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 22:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teoria', '0007_auto_20160815_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='usuario',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='usuario',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
