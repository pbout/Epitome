# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-16 15:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PCAT_CAT', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PCHOICE_CHOICE', models.CharField(max_length=100)),
                ('PCHOICE_VOTES', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_CODE', models.CharField(max_length=200)),
                ('P_TITLE', models.CharField(max_length=100)),
                ('P_SHRBODY', models.CharField(max_length=300)),
                ('P_BODY', models.CharField(max_length=1000)),
                ('P_CREATION', models.DateTimeField(default=datetime.datetime(2016, 8, 16, 15, 25, 35, 344556, tzinfo=utc))),
                ('P_STARTDT', models.DateTimeField()),
                ('P_ENDDT', models.DateTimeField()),
                ('P_DURATION', models.IntegerField(default=0)),
                ('P_CODE2', models.CharField(blank=True, max_length=200)),
                ('PCAT_CAT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eisegesis.ProposalCat')),
                ('UGRP_GROUPID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('USER_CREATORID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proposalchoice',
            name='PROPOSAL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eisegesis.Proposals'),
        ),
    ]
