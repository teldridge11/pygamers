# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20160102_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='user',
            field=models.CharField(max_length=256),
        ),
    ]
