# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 15:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Eisegesis', '0014_auto_20160817_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposals',
            name='P_CREATION',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 4, 15, 32, 46, 419402, tzinfo=utc)),
        ),
    ]
