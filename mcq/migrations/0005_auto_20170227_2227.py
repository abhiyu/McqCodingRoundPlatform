# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0004_auto_20170225_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='endgame',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]
