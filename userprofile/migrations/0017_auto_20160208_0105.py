# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 01:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20160208_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='delete',
            new_name='deleteGame',
        ),
    ]
