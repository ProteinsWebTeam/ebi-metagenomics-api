# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emgapi', '0028_auto_20200706_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='study_name',
            field=models.CharField(blank=True, db_column='STUDY_NAME', max_length=4000, null=True),
        ),
    ]
