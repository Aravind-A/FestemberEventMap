# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stall_name', models.CharField(max_length=100)),
                ('stall_description', models.CharField(max_length=200)),
            ],
        ),
    ]
