# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20160711_2213'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='grupo',
            index_together=set([('año', 'numero')]),
        ),
    ]
