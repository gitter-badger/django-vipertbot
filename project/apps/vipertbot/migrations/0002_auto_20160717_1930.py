# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipertbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regular',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
