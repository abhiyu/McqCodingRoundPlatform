# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0005_auto_20170227_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='access',
        ),
        migrations.AddField(
            model_name='profile',
            name='lasttimeupdated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reciept',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]