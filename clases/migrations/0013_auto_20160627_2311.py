# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0012_auto_20160626_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposicion',
            name='finish_expo',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='exposicion',
            name='start_expo',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='exposicion',
            name='start_preg',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
