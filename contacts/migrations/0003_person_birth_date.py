# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20161106_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=1, verbose_name='Birthdate'),
        ),
    ]
