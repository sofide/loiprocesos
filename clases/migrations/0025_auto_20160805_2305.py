# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0024_auto_20160723_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='fecha',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, unique=True),
        ),
        migrations.AlterField(
            model_name='tp',
            name='numero',
            field=models.IntegerField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterIndexTogether(
            name='exposicion',
            index_together=set([('clase', 'grupo', 'tp')]),
        ),
    ]
