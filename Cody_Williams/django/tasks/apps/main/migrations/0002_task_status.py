# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
