# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-05 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emgapi', '0010_run_assembly_split'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='is_public',
            field=models.BooleanField(db_column='IS_PUBLIC', default=False),
        ),
    ]
