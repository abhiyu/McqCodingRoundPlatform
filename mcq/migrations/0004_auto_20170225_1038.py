# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 10:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20170225_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 25, 10, 38, 5, 274968, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
