# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0018_tp_nuemero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tp',
            name='nuemero',
        ),
        migrations.AddField(
            model_name='tp',
            name='numero',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]