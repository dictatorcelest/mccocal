# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('exchange_id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('detail', models.TextField(blank=True, default='N/A')),
                ('attendees', models.TextField(blank=True, default='N/A')),
            ],
        ),
    ]
