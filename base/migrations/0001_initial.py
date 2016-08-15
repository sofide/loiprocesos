# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('reference', models.CharField(db_index=True, max_length=200)),
                ('edited', models.DateField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
    ]