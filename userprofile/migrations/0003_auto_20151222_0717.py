# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_game_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to='games'),
        ),
        migrations.AlterField(
            model_name='game',
            name='requirements',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
