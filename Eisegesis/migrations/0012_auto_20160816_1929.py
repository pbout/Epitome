# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-16 16:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Eisegesis', '0011_auto_20160816_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposals',
            name='P_CREATION',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 16, 29, 51, 907428, tzinfo=utc)),
        ),
    ]
