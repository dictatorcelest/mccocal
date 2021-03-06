# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 09:18
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_id', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('detail', models.TextField(blank=True)),
                ('attendees', models.TextField(blank=True)),
            ],
        ),
    ]
