# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 04:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teoria', '0002_auto_20160708_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 7, 23, 4, 12, 1, 950318, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 7, 23, 4, 13, 13, 720143, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='autor',
            field=models.CharField(max_length=200, null=True, verbose_name='Sugerido por'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='autor',
            field=models.CharField(max_length=200, verbose_name='Sugerido por'),
        ),
    ]
