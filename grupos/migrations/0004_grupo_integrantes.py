# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 00:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grupos', '0003_auto_20160708_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='integrantes',
            field=models.ManyToManyField(related_name='grupos', through='grupos.Pertenencia', to=settings.AUTH_USER_MODEL),
        ),
    ]
