# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-22 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0030_auto_20160921_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposicion',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
