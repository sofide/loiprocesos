# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0031_exposicion_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposicion',
            name='video',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]