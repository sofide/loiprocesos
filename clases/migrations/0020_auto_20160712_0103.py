# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0019_auto_20160712_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tp',
            options={'ordering': ['numero']},
        ),
    ]
