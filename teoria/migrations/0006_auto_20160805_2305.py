# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teoria', '0005_auto_20160731_2057'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='material',
            index_together=set([('autor', 'nombre')]),
        ),
        migrations.AlterIndexTogether(
            name='pregunta',
            index_together=set([('autor', 'pregunta')]),
        ),
    ]